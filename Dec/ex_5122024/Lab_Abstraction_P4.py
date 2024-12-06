from abc import ABC,abstractmethod

class ExceReader(ABC):

    @abstractmethod
    def Read_From_Excel(self):
      pass

class browser(ExceReader):

    @abstractmethod
    def startbrowser(self):
       pass

    @abstractmethod
    def stopbrowser(self):
        pass

class TC1():

    def startbrowser(self):
        print("Start the browser")

    def stopbrowser(self):
        print("Stop the browser")

    def readfromexcel(self):
        print("Read the value from excel")

    def runtc(self):
        self.startbrowser()
        self.readfromexcel()
        self.stopbrowser()

tc=TC1()
tc.runtc()


