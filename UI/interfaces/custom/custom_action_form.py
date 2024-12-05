from npyscreen.fmActionForm import ActionForm


class CustomActionForm(ActionForm):
    """Override the default buttons to rename Cancel to Back."""

    CANCEL_BUTTON_TEXT = "Back"
