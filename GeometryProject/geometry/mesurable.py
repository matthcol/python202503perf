"""provides interfaces with measures in 1D, 2D"""

from abc import ABC, abstractmethod

class Mesurable1D(ABC):
    
    @abstractmethod
    def length(self) -> float:
        pass

class Mesurable2D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass