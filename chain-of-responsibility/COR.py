import abc


class AbstractHardwareHandler(abc.ABC):
    @abc.abstractmethod
    def nextHandler(self):
        pass

    @abc.abstractmethod
    def isAvailable(self):
        pass

    @abc.abstractmethod
    def createModel(self):
        pass

    @abc.abstractmethod
    def setNext(self, next_handler):
        pass


class GpuHandler(AbstractHardwareHandler):

    def nextHandler(self):
        if self.isAvailable():
            print("Gpu ile calistiriliyor")

            return self
        else:
            print("Gpu bulunamadi !")
            if self.nextH is None:
                raise StopIteration
            return self.nextH.nextHandler()

    def __iter__(self):


        if not self.isAvailable():
            yield self.nextHandler()
        else:
            yield self


    def isAvailable(self):
        return True

    def createModel(self):
        print(self.model_type," olusturuluyor ")
        return self.model_type

    def setNext(self, next_handler):
        self.nextH = next_handler

    def __init__(self):
        self.nextH = None
        self.model_type = "GPUMODEL"


class TpuHandler(AbstractHardwareHandler):
    def __iter__(self):

        if not self.isAvailable():


            yield self.nextHandler()
        else:
            yield self

    def nextHandler(self):
        if self.isAvailable():
            print("Tpu ile calistiriliyor")

            return self
        else:
            print("Tpu bulunamadi !")
            if self.nextH is None:
                raise StopIteration
            return self.nextH.nextHandler()




    def isAvailable(self):
        return False

    def createModel(self):
        print(self.model_type," olusturuluyor ")
        return self.model_type

    def setNext(self, next_handler):
        self.nextH = next_handler

    def __init__(self):
        self.nextH = None
        self.model_type = "TPUMODEL"


class CpuHandler(AbstractHardwareHandler):

    def __iter__(self):

        if not self.isAvailable():
            yield self.nextHandler()
        else:
            yield self

    def nextHandler(self):
        if self.isAvailable():
            print("Cpu ile calistiriliyor")
            return self
        else:
            print("Cpu bulunamadi !")
            if self.nextH is None:
                raise StopIteration
            return self.nextH.nextHandler()



    def isAvailable(self):
        return True

    def createModel(self):
        print(self.model_type," olusturuluyor ")
        return self.model_type

    def setNext(self, next_handler):
        self.nextH = next_handler

    def __init__(self):
        self.nextH = None
        self.model_type = "CPUMODEL"


c = CpuHandler()
t = TpuHandler()
g = GpuHandler()

t.setNext(g)
g.setNext(c)

for handler in t:

    print(handler.createModel())
