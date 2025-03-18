# module geometry.point

# En Python 3, toute classe hérite de la classe 'object'
# conventions de nommage: PEP 8

import math

from dataclasses import dataclass
# other possibility: pydantic (lib tierce)


# @dataclass # init, repr/str, equals/hash, ...
@dataclass(kw_only=True)
class Point:
    """represents a 2D point with its coordinates x and y
    """

    x: float = 0.0
    y: float = 0.0

    # customize a 'str' diffedrent from 'repr'
    def __str__(self):
        return f"({self.x}, {self.y})"
  
    def distance(self, other: 'Point') -> float:
       # return math.hypot(self.x - other.x, self.y - other.y) 
       return math.dist([self.x, self.y], [other.x, other.y])