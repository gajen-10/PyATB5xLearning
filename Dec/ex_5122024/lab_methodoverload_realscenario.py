class oldbrowser:

    def startbrowser(self):
        print("IE browser is starting")

    def stopbrowser(self):
        print("IE browser is stopped")

class chromebrowser(oldbrowser):

    super().startbrowser()
    def startbrowser(self):
        print("Better chrome browser is starting")

    def stopbrowser(self):
        print("Better chrome browser is stopping")


c= chromebrowser()
c.startbrowser()
c.stopbrowser()

