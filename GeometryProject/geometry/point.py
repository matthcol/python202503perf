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
    """Represents a 2D point with an optional name and its coordinates x and y.
    
    Example:
        p1 = Point(name="A", x=3.5, y=7.25)
    """

    x: float = 0.0
    y: float = 0.0

    # customize a 'str' different from 'repr'
    def __str__(self):
        return f"{
                super().__str__()
            }({
                self.x
            }, {
                self.y
            })"
  
    def distance(self, other: 'Point') -> float:
       # return math.hypot(self.x - other.x, self.y - other.y) 
       return math.dist([self.x, self.y], [other.x, other.y])
    
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.x += delta_x
        self.y += delta_y
        
    
@dataclass(kw_only=True)
class ColoredPoint(Point):
    """Represents a Point with a optional name, its coordinates and a color.
    
    Examples:
        p1 = ColoredPoint(name="A", x=3.5, y=7.25, color="red")
        p2 = ColoredPoint(x=3.5, y=7.25, color="#00af3d") # no name
        p3 = ColoredPoint(x=3.5, y=7.25)                  # no name, default color
        p4 = ColoredPoint(color="green")                  # no name, default coordinates
        p5 = ColoredPoint(name="A")                       # default coordinates and color
        p6 = ColoredPoint()                               # default colored point
    """

    color: str = '#000000'

    def __str__(self):
        return super().__str__() + '@' + self.color 
       

@dataclass(kw_only=True)
class WeightedPoint(Point):
    """Represents a Point with a optional name, its coordinates and a weight.
    
    Example:
        p1 = WeightedPoint(name="A", x=3.5, y=7.25, weight=1.5E6)
    """
    weight: float = 1.0

    def __str__(self):
        return f"{super().__str__()}${self.weight:.3f}" 

@dataclass(kw_only=True)
class ColoredWeightedPoint(ColoredPoint, WeightedPoint):
    """Represents a Point with a optional name, its coordinates, a color and a weight.
    
    Example:
        p1 = ColoredWeightedPoint(name="A", x=3.5, y=7.25, color="red", weight=1.5E6)"""
    