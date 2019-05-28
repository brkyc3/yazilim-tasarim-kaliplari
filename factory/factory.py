from abc import ABC, abstractmethod
import random


class SimilarityMethod:
    LABEL=0
    SIFT=1
    DEEP=2
    DEFAULT=LABEL

class SimilarityTool(ABC):


    @abstractmethod
    def find_similars(self,imageData):
        pass

class LabelSimilarity(SimilarityTool):


    def find_similars(self,imageData):
        print('labela gore benzer goruntuler')

        return [random.randint(0,100) for _ in range(10)]



class DeepSimilarity(SimilarityTool):

    def find_similars(self, imageData):
        print('conv net benzer goruntuler')

        return [random.randint(0,100) for _ in range(10)]

class SiftSimilarity(SimilarityTool):

    def find_similars(self, imageData):
        print('sift benzer goruntuler')

        return [random.randint(0,100) for _ in range(10)]

class SimilarityToolFactory:

    @staticmethod
    def create_similarity_tool(method=SimilarityMethod.SIFT):
        if method is SimilarityMethod.LABEL:
            return LabelSimilarity()
        elif method is SimilarityMethod.DEEP:
            return DeepSimilarity()
        else:
            return SiftSimilarity()



image = None


tool = SimilarityToolFactory.create_similarity_tool(SimilarityMethod.LABEL)
print(tool.find_similars(image))
tool = SimilarityToolFactory.create_similarity_tool(SimilarityMethod.SIFT)
print(tool.find_similars(image))
tool = SimilarityToolFactory.create_similarity_tool(SimilarityMethod.DEEP)
print(tool.find_similars(image))