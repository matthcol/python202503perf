from collections.abc import Iterable
from geometry import Point, Circle, Polygon, Mesurable2D, Segment
from geometry.shape import Shape


def total_area(mesurables: Iterable[Mesurable2D]) -> float:
    return sum(m.area() for m in mesurables)


pointA = Point(name="A", x=3.5, y=7.25)
circleC = Circle(
        name="C",
        radius=10.0,
        center=pointA
    )
triangla345 = Polygon(
        name="P345",
        vertices=(
            Point(x=1.5, y=6.25),
            Point(x=4.5, y=6.25),
            Point(x=4.5, y=2.25),
        ) 
)
pentagonWiki = Polygon(
        name="PW",
        vertices=(
            Point(x=1.0, y=6.0),
            Point(x=3.0, y=1.0),
            Point(x=7.0, y=2.0),
            Point(x=4.0, y=4.0),
            Point(x=8.0, y=5.0),
        )
)

list_shape: list[Shape] = [pointA, circleC, triangla345, pentagonWiki, Segment()]
list_mesurable2d: list[Mesurable2D] = [
    circleC, triangla345, pentagonWiki,
    # pointA # Point is not Mesurable2D
]

area1 = total_area(list_mesurable2d)
# area2 = total_area(list_shape) # some of them are not Mesurable2D

# exo: extraire les Mesurable2D de la liste de Shape
list_mesurable2d_2 = [s for s in list_shape if isinstance(s, Mesurable2D)]
area2 = total_area(list_mesurable2d_2)

area2 = total_area(s for s in list_shape if isinstance(s, Mesurable2D))