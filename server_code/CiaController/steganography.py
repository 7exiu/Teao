import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from PIL import Image
from datetime import datetime


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#[942276,2704978984]

def get_hidden_message(file):

    im = Image.open(file.name)
    print("🚀 images user")
    r , g , b = im.split()
    r = list( r.getdata() )
    
    # lecture de la longueur de la chaine
    print("✅ lecture de la longueur de la chaine")
    p = [ str(x%2) for x in r[0:8] ]
    q = "".join(p)
    q = int(q,2)
    print(p)
    print(q)

    
    # lecture du message
    print("🎾 lecture du message ")
    n = [ str(x%2) for x in r[8:8*(q+1)] ]
    print(f"✅ {n}")

    b = "".join(n)
    message = ""
  
    for k in range(0,q):
        l = b[8*k:8*k+8]
        message += chr(int(l,2))
        
    return message



def hide_message(file,msg):

    print("HIDE MESSAGE")
    im = Image.open(file)
    # on récupère les dimensions de l'image
    w , h = im.size
    print(w, h)
    r , g , b = im.split()
    r = list( r.getdata() )
    # on calcule la longueur de la chaîne et on la transforme en binaire
    u = len(msg)
    print(f"on calcule la longueur de la chaîne et on la transforme en binaire {u}")
    v = bin( len(msg) )[2:].rjust(8,"0")

    # on transforme la chaîne en une liste de 0 et de 1 
    ascii = [ bin(ord(x))[2:].rjust(8,"0") for x in msg ]
    print(f"🎾 on transforme la chaîne en une liste de 0 et de 1 : {ascii}")

    # transformation de la liste en chaîne
    a = ''.join(ascii)
    print(f"✅ transformation de la liste en chaîne{a}")

    # on code la longueur de la liste dans les 8 premiers pixels rouges
    print("🎾 on code la longueur de la liste dans les 8 premiers pixels rouges")
    for j in range(8):
        r[j] = 2 * int( r[j] // 2 ) + int( v[j] )

    print("🚀on code la chaîne dans les pixels suivants")

 
    for i in range(8*u):
        r[i+8] = 2 * int( r[i+8] // 2 ) + int( a[i] )
        
    # on recrée l'image rouge 
    nr = Image.new("L",(16*w,16*h))
    nr = Image.new("L",(w,h))
    nr.putdata(r)
    print("🚀# on a recrée l'image rouge ")
    # fusion des trois nouvelles images
    imgnew = Image.merge('RGB',(nr,g,b))
    new_name_img = "couv_" + file.name
    imgnew.save(new_name_img)
    return imgnew