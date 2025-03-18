# module geometry.point

# En Python 3, toute classe hérite de la classe 'object'
# conventions de nommage: PEP 8

import math

from dataclasses import dataclass

from geometry.shape import Shape
# other possibility: pydantic (lib tierce)


# @dataclass # init, repr/str, equals/hash, ...
@dataclass(kw_only=True)
class Point(Shape): # class Point inherits from class Shape
    """represents a 2D point with its coordinates x and y
    """

    x: float = 0.0
    y: float = 0.0

    # customize a 'str' different from 'repr'
    def __str__(self):
        return f"({self.x}, {self.y})"
  
    def distance(self, other: 'Point') -> float:
       # return math.hypot(self.x - other.x, self.y - other.y) 
       return math.dist([self.x, self.y], [other.x, other.y])
    
@dataclass
class ColoredPoint(Point):
    pass

@dataclass
class WeightedPoint(Point):
    pass

@dataclass
class ColoredWeightedPoint(ColoredPoint, WeightedPoint):
    pass