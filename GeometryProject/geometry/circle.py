from dataclasses import dataclass, field
from typing import override

from geometry.point import Point
from geometry.shape import Shape

@dataclass(kw_only=True)
class Circle(Shape):
    radius: float = 1.0
    center: Point = field(default_factory=Point)

    def __str__(self):
        return f"{
            super().__str__()
        }<{
            self.radius
        }, {
            self.center
        }>"


