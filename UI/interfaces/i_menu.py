from abc import ABC, abstractmethod
from UI.interfaces.custom.custom_action_form import CustomActionForm
import npyscreen

class IMenu(ABC, CustomActionForm):
    @abstractmethod
    def create(self):
        """Create a new menu instance."""
        pass

    @abstractmethod
    def on_ok(self):
        """Handle the logic for when the user confirms an action."""
        pass

    @abstractmethod
    def on_cancel(self):
        """Handle the logic for when the user cancels an action."""
        pass

    def before_editing(self):
        """Perform any necessary setup or validation before editing the menu."""
        # Call the `CustomActionForm` lifecycle
        CustomActionForm.before_editing(self)
