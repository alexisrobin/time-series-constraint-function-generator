from abc import ABC, abstractmethod

class Aggregator(ABC):

    @staticmethod
    @abstractmethod
    def aggregate(a,b):
        pass

    @staticmethod
    @abstractmethod
    def default(feature):
        pass

class Max(Aggregator):

    @staticmethod
    def aggregate(a,b):
        return "max(" + a + "," + b + ")"

    @staticmethod
    def default(feature):
        return feature.min()

class Min(Aggregator):

    @staticmethod
    def aggregate(a,b):
        return "min(" + a + "," + b + ")"

    @staticmethod
    def default(feature):
        return feature.max()

class Sum(Aggregator):

    @staticmethod
    def aggregate(a,b):
        return a + "+" + b

    @staticmethod
    def default(feature):
        return "0"