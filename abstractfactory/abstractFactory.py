import abc


class DedectorFactory(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def create_model(self):
        pass

    @abc.abstractmethod
    def create_datagenerator(self):
        pass


class GpuDedectorFactory(DedectorFactory):


    def create_model(self):
        return GpuModel()

    def create_datagenerator(self):
        return GpuGenerator()


class CpuDedectorFactory(DedectorFactory):


    def create_model(self):
        return CpuModel()

    def create_datagenerator(self):
        return CpuGenerator()


class AbstractModel(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def build_model(self):
        pass


class GpuModel(AbstractModel):


    def build_model(self):
        pass


class CpuModel(AbstractModel):

    def build_model(self):
        pass


class AbstractGenerator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_data(self):
        pass


class GpuGenerator(AbstractGenerator):

    def generate_data(self):
        pass


class CpuGenerator(AbstractGenerator):


    def generate_data(self):
        pass


def main():
    for factory in (GpuDedectorFactory(), CpuDedectorFactory()):
        model = factory.create_model()
        data_generator = factory.create_datagenerator()
        model.build_model()
        data_generator.generate_data()


if __name__ == "__main__":
    main()