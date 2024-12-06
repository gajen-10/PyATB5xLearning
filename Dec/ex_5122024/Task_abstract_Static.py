from abc import ABC,abstractmethod
class pc:
    def __init__(self):
        print("PC intiated")

    class motherboard():
        @abstractmethod
        def startmotherboard(self):
            pass
    class RAM:

        @abstractmethod
        def startram(self):
            pass

    class processor:
        @abstractmethod
        def startprocessor(self):
            pass

    class storage:

        @abstractmethod
        def storagedata(self):
            pass
@staticmethod
def loados():
    print("Loading the OS")

def startmouse():
    print("Start using the mouse")

def useheadphone():
    print("Plugin the headphone to hear sound")

