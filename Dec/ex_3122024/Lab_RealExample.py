class Basetest:

    def open_browser(self):
        print("Starting the browser")

    def read_from_excel(self):
        print("Read from excel")
    def close_browser(self):
        print("Closing the browser")

class Testcase1(Basetest):

    def test_positive(self):
        self.open_browser()
        print("Testcase1 positive executed !!")
        self.read_from_excel()
        self.close_browser()

    def test_negative(self):
        self.open_browser()
        print("Testcase1 negative executed !!")
        self.read_from_excel()
        self.close_browser()

class Testcase2(Basetest):

    def test_2(self):
        self.open_browser()
        print("Testcase2 executed !!")
        self.read_from_excel()
        self.close_browser()

