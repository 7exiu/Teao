from ._anvil_designer import ProfileTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Profile(ProfileTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    try:
      user_info = anvil.server.call('get_user_info')
      user_email = user_info["user_email"]
      user_info = user_info["user_id"]
      if not user_email or not user_info:
        Notification("Redirection ...", style="info").show()
        get_open_form().load_page('login')
    except Exception as e:
      Notification(f"{e}", style="danger").show()
      
    # Any code you write here will run before the form opens.
