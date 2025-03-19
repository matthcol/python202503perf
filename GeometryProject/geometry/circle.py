from dataclasses import dataclass, field
from typing import override

from geometry.point import Point
from geometry.shape import Shape

@dataclass(kw_only=True)
class Circle(Shape):
    radius: float = 1.0  # field(default=1.0, repr=False, compare=False)
    center: Point = field(default_factory=Point)

    @override
    def __str__(self) -> str:
        return f"{
            super().__str__()
        }<{
            self.radius
        }, {
            self.center
        }>"

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        self.center.translate(delta_x, delta_y)