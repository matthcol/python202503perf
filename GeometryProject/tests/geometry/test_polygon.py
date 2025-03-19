import pytest
from geometry.point import Point
from geometry.polygon import Polygon


@pytest.fixture
def triangle345() -> Polygon:
    return Polygon(
        name="P345",
        vertices=(
            Point(x=1.5, y=6.25),
            Point(x=4.5, y=6.25),
            Point(x=4.5, y=2.25),
        )
    )


@pytest.fixture
def pentagon_wikipedia() -> Polygon:
    return Polygon(
        name="PW",
        vertices=(
            Point(x=1.0, y=6.0),
            Point(x=3.0, y=1.0),
            Point(x=7.0, y=2.0),
            Point(x=4.0, y=4.0),
            Point(x=8.0, y=5.0),
        )
    )  


@pytest.mark.parametrize(
        "polygon_fixture_name, expected_area",
        [
            ("triangle345", 6.0),
            ("pentagon_wikipedia", 16.5),
        ]
)
def test_area(polygon_fixture_name, expected_area, request):
    polygon = request.getfixturevalue(polygon_fixture_name)
    actual_area = polygon.area()
    assert expected_area == actual_area
    

@pytest.mark.parametrize(
        "polygon_fixture_name, expected_perimeter",
        [
            ("triangle345", 12.0),
            ("pentagon_wikipedia", pytest.approx(24.308, 1E-3)),
        ],
)
def test_perimeter(polygon_fixture_name, expected_perimeter, request):
    polygon = request.getfixturevalue(polygon_fixture_name)
    actual_perimeter = polygon.perimeter()
    assert expected_perimeter == actual_perimeter

def test_constructor_default():
    poly = Polygon()
    assert 3 == len(poly.vertices)
    p0 = Point()
    for vertix in poly.vertices:
        assert p0 == vertix

def test_constructor_all_args(pentagon_wikipedia):
    assert 5 == len(pentagon_wikipedia.vertices)
    assert Point(x=1.0, y=6.0) == pentagon_wikipedia.vertices[0]
    assert Point(x=3.0, y=1.0) == pentagon_wikipedia.vertices[1]
    assert Point(x=7.0, y=2.0) == pentagon_wikipedia.vertices[2]
    assert Point(x=4.0, y=4.0)     == pentagon_wikipedia.vertices[3]
    assert Point(x=8.0, y=5.0) == pentagon_wikipedia.vertices[4]