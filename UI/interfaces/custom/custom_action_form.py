from npyscreen.fmActionForm import ActionForm
import npyscreen

class CustomActionForm(ActionForm):
    """Override the default buttons to rename Cancel to Back."""

    CANCEL_BUTTON_TEXT = "Back"

    def before_editing(self):
        """Ensure the parent class's lifecycle is maintained."""
        super().before_editing()  # Call the parent ActionForm lifecycle
