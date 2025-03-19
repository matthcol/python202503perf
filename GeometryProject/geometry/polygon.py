from dataclasses import dataclass, field
from typing import override
from geometry.point import Point
from geometry.shape import Shape

@dataclass
class Polygon(Shape):
    
    vertices: tuple[Point, ...] = field(
        # default_factory=tuple
        default_factory=lambda: (Point(), Point(), Point())
    )

    @override
    def translate(self, delta_x: float, delta_y: float) -> None:
        for vertix in self.vertices:
            vertix.translate(delta_x, delta_y)

    @override
    def __str__(self) -> str:
        return f"{
                super().__str__()
            }~{
                len(self.vertices)
            }({
                ', '.join(
                    ('?' if vertix.name is None else vertix.name) for vertix in self.vertices
                )
            })"
    
    def is_valid(self):
        return len(self.vertices) >= 3