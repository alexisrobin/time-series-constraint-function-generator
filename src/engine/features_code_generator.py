from abc import ABC, abstractmethod

class Feature(ABC):
    
    @staticmethod
    @abstractmethod
    def neutral():
        pass

    @staticmethod
    @abstractmethod
    def min():
        pass

    @staticmethod
    @abstractmethod
    def max():
        pass

    @staticmethod
    @abstractmethod
    def phi(a,b):
        pass

    @staticmethod
    @abstractmethod
    def delta():
        pass

class One(Feature):

    @staticmethod
    def neutral():
        return "1"

    @staticmethod
    def min():
        return "1"

    @staticmethod
    def max():
        return "1"

    @staticmethod
    def phi(a,b):
        return "max(" + a + "," + b + ")"

    @staticmethod
    def delta():
        return "0"

class Width(Feature):

    @staticmethod
    def neutral():
        return "0"

    @staticmethod
    def min():
        return "0"

    @staticmethod
    def max():
        return "n"

    @staticmethod
    def phi(a,b):
        return a + "+" + b

    @staticmethod
    def delta():
        return "1"

class Surface(Feature):

    @staticmethod
    def neutral():
        return "0"

    @staticmethod
    def min():
        return "float('-inf')"

    @staticmethod
    def max():
        return "float('inf')"

    @staticmethod
    def phi(a,b):
        return a + "+" + b

    @staticmethod
    def delta():
        return "sequence[i-1]"

class Max(Feature):

    @staticmethod
    def neutral():
        return "float('-inf')"

    @staticmethod
    def min():
        return "float('-inf')"

    @staticmethod
    def max():
        return "float('inf')"

    @staticmethod
    def phi(a,b):
        return "max(" + a + "," + b + ")"

    @staticmethod
    def delta():
        return "sequence[i-1]"

class Min(Feature):

    @staticmethod
    def neutral():
        return "float('inf')"

    @staticmethod
    def min():
        return "float('-inf')"

    @staticmethod
    def max():
        return "float('inf')"

    @staticmethod
    def phi(a,b):
        return "min(" + a + "," + b + ")"

    @staticmethod
    def delta():
        return "sequence[i-1]"