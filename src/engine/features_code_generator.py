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
    def phi(arg1,arg2):
        pass

    @staticmethod
    @abstractmethod
    def delta(arg):
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
    def phi(arg1,arg2):
        return "max(" + arg1 + "," + arg2 + ")"

    @staticmethod
    def delta(arg):
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
    def phi(arg1,arg2):
        return arg1 + "+" + arg2

    @staticmethod
    def delta(arg):
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
    def phi(arg1, arg2):
        return arg1 + "+" + arg2

    @staticmethod
    def delta(arg):
        return "sequence[" + arg + "]"

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
    def phi(arg1, arg2):
        return "max(" + arg1 + "," + arg2 + ")"

    @staticmethod
    def delta(arg):
        return "sequence[" + arg + "]"

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
    def phi(arg1, arg2):
        return "min(" + arg1 + "," + arg2 + ")"

    @staticmethod
    def delta(arg):
        return "sequence[" + arg + "]"

class Range(Feature):

    @staticmethod
    def neutral():
        return "0"

    @staticmethod
    def min():
        return "0"

    @staticmethod
    def max():
        return "float('inf')"

    @staticmethod
    def phi(arg1, arg2):
        raise NotImplementedError("Should never happened")

    @staticmethod
    def delta(arg):
        return "sequence[" + arg + "]"