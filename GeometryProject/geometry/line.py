from dataclasses import dataclass, field
from typing import override

from geometry.mesurable import Mesurable1D
from geometry.point import Point
from geometry.shape import Shape

@dataclass(kw_only=True)
class Segment(Shape, Mesurable1D):
    ends: tuple[Point, Point] = field(
        default_factory=lambda: (Point(), Point())
    )

    def translate(self, delta_x: float, delta_y: float) -> None:
        for end in self.ends:
            end.translate(delta_x, delta_y)

    def __str__(self):
        return f"{
                super().__str__()
            }#[{
                self.ends[0]
            } - {
                self.ends[1]
            }]"
    
    @override
    def length(self) -> float:
        p1, p2 = self.ends
        return p1.distance(p2)
    
    def __len__(self):
        p1, p2 = self.ends
        return p1.distance(p2)
    

