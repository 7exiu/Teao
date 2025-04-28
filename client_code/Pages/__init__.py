import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class SharedStateManager:
    def __init__(self):
        self._state = {
          "user_id": "",
          "user_email": "",
          "cart": []
        }
        self._listeners = []

    def get(self, key):
        return self._state.get(key)

    def set(self, key, value):
        self._state[key] = value
        self._notify()

    def _notify(self):
        for callback in self._listeners:
            callback()

    def register(self, callback):
        self._listeners.append(callback)

    def unregister(self, callback):
        self._listeners.remove(callback)


 
state = SharedStateManager()
