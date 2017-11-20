from abc import ABC, abstractmethod

class Aggregator(ABC):

    @staticmethod
    @abstractmethod
    def default(feature):
        pass

class Max(Aggregator):

    @staticmethod
    def default(feature):
        return feature.min()

class Min(Aggregator):

    @staticmethod
    def default(feature):
        return feature.max()

class Sum(Aggregator):

    @staticmethod
    def default(feature):
        return "0"