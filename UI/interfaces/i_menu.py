from abc import ABC, abstractmethod
import npyscreen


class IMenu(ABC, npyscreen.ActionForm):
    @abstractmethod
    def create(self):
        """Create a new menu instance."""
        pass

    def before_editing(self):
        """Optional method. Perform any necessary setup or validation before editing the menu."""
        pass

    @abstractmethod
    def on_ok(self):
        """Handle the logic for when the user confirms an action."""
        pass

    @abstractmethod
    def on_cancel(self):
        """Handle the logic for when the user cancels an action."""
        pass
