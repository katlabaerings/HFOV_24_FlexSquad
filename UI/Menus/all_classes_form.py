import npyscreen


class AllClassesForm(npyscreen.ActionForm):
    def create(self):
        self.add(npyscreen.TitleFixedText, name="Not Implemented Yet!")

    def on_cancel(self):
        self.parentApp.switchForm('MAIN')