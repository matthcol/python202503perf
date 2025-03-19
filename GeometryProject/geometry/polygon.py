from dataclasses import dataclass, field
from geometry.point import Point
from geometry.shape import Shape

@dataclass
class Polygon(Shape):
    
    vertices: tuple[Point, ...] = field(
        # default_factory=tuple
        default_factory=lambda: (Point(), Point(), Point())
    )

    def translate(self, delta_x: float, delta_y: float) -> None:
        for vertix in self.vertices:
            vertix.translate(delta_x, delta_y)

    def __str__(self):
        return f"{
                super().__str__()
            }~{
                len(self.vertices)
            }({
                ', '.join(
                    ('?' if vertix.name is None else vertix.name) for vertix in self.vertices
                )
            })"