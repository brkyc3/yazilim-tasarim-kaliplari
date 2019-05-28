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
        print('gpuya ozel generator')
        return GpuGenerator()


class CpuDedectorFactory(DedectorFactory):


    def create_model(self):
        return CpuModel()

    def create_datagenerator(self):
        print('cpuya ozel generator')
        return CpuGenerator()


class AbstractModel(metaclass=abc.ABCMeta):


    @abc.abstractmethod
    def build_model(self):
        pass


class GpuModel(AbstractModel):


    def build_model(self):
        print('gpu modeli olusturuludu')
        return 'GPUMODEL'


class CpuModel(AbstractModel):

    def build_model(self):
        print('cpu modeli olusturuludu')
        return 'CPUMODEL'


class AbstractGenerator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def generate_data(self):
        pass


class GpuGenerator(AbstractGenerator):

    def generate_data(self):
        print('veriyi oku ,ayrica gpuya yukle \n\n')
        return "GPUGENERATOR"


class CpuGenerator(AbstractGenerator):


    def generate_data(self):
        print('veriyi oku , geri dondur \n\n')
        return "CPUGENERATOR"


def main():
    for factory in (GpuDedectorFactory(), CpuDedectorFactory()):
        model = factory.create_model()
        data_generator = factory.create_datagenerator()
        model.build_model()
        data_generator.generate_data()


if __name__ == "__main__":
    main()