import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import jwt
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


def code_token(payload):
  encoded_token = jwt.encode(payload,"secret", algorithm="HS256")
  print("🚀 encoded token ", encoded_token)
  return encoded_token
 
def decode_token(encoded_token):
  decoded_token = jwt.decode(encoded_token, "secret", algorithms=["HS256"])
  print("🚀 decoded token", decoded_token)
  return decoded_token
  
