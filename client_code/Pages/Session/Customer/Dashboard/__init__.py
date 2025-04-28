from ._anvil_designer import DashboardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Dashboard(DashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    try:
      users = anvil.server.call('get_users')
      print("🎾", users[0])
      self.user_info = anvil.server.call('get_user_info')
      print("✅ CUSTOMER DASHBOARD : ", self.user_info)
      self.user = anvil.server.call('get_user_by_email', self.user_info["user_email"])
      print("-------------------------------------")
      print("🎾 USER DASHBOARD", self.user)
      print("-------------------------------------")
    except Exception as e:
      Notification(f"Error while trying to reach the server : {e}", style="danger").show()

    # Any code you write here will run before the form opens.
