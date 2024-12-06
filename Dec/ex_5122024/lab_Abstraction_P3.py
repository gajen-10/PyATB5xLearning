from abc import ABC,abstractmethod

class Gearbox(ABC):

    @abstractmethod
    def setgear(self):
        pass

class engine(Gearbox):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class car(engine):

    def start(self):
        print("start the engine")

    def stop(self):
        print("Stop the engine")

    def setgear(self):
        print("Gearbox is ready")

    def runcar(self):
        self.start()
        self.setgear()
        self.stop()

ca=car()
ca.runcar()
