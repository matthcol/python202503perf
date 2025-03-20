from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import override
from geometry.mesurable import Mesurable2D
from geometry.point import Point
from geometry.shape import Shape

@dataclass
class Polygon(Shape, Mesurable2D):
    
    vertices: tuple[Point, ...] = field(
        # default_factory=tuple
        default_factory=lambda: (Point(), Point(), Point()),
        repr=False
    )

    @staticmethod
    def from_iterable_vertices(vertices: Iterable[Point]):
        """
        Returns a new Polygon from a series of points

        Example:
            poly = Polygon.from_vertices([p1, p2, p3, p4])

        """
        return Polygon(vertices = tuple(vertices))
    
    @staticmethod
    def from_vertices(*vertices: Point):
        """
        Returns a new Polygon from a series of points

        Example:
            poly = Polygon.from_vertices(p1, p2, p3, p4)

        """
        return Polygon(vertices = vertices)

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
    
    @override
    def area(self) -> float:
        prev = self.vertices[-1]
        res = 0.0
        for vertix in self.vertices:
            res += vertix.x * prev.y - vertix.y * prev.x
            prev = vertix
        return abs(res) / 2.0

    @override
    def perimeter(self) -> float:
        prev = self.vertices[-1]
        res = 0.0
        for vertix in self.vertices:
            res += vertix.distance(prev)
            prev = vertix
        return res