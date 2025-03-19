import pytest
from geometry import Point

# this test modify the fixture without impact on another tests
def test_set_x(pointA):
    pointA.x = 4.125
    assert 4.125 == pointA.x

def test_constructor_default():
    p = Point()
    assert p.name is None
    assert 0.0 == p.x
    assert 0.0 == p.y

def test_constructor(pointA):
    assert "A" == pointA.name
    assert 3.5 == pointA.x
    assert 7.25 == pointA.y

def test_distance_same(pointA):
    assert 0.0 == pointA.distance(pointA)

# Exercise:
# - add a test case with an epislon <> 0.0
# - implements method and check tests

@pytest.mark.parametrize(
        "x1, y1, x2, y2, expected_distance, epsilon",
        [
            (4.25, 5.125, 1.25, 9.125, 5.0, 0.0),
            (4.25E-150, 5.125E-150, 1.25E-150, 9.125E-150, 5E-150, 0.0),
            (4.25E-300, 5.125E-300, 1.25E-300, 9.125E-300, 5E-300, 1E-15),
            (4.25E+150, 5.125E+150, 1.25E+150, 9.125E+150, 5E+150, 0.0),
            (4.25E+300, 5.125E+300, 1.25E+300, 9.125E+300, 5E+300, 0.0),
            (3.4, 0.07, 0.1, 5.08, 5.9991749432735, 1E-15)
        ],
        ids=[
            "triangle 345",
            "triangle 345 scale 1E-150",
            "triangle 345 scale 1E-300",
            "triangle 345 scale 1E+150",
            "triangle 345 scale 1E+300",
            "with float imprecision"
        ]
)
def test_distance_different(x1, y1, x2, y2, expected_distance, epsilon):
    p1 = Point(x=x1, y=y1)
    p2 = Point(x=x2, y=y2)
    actual_distance = p1.distance(p2)
    assert expected_distance == pytest.approx(actual_distance, rel=epsilon)

def test_translate(pointA):
    # before:  x=3.5, y=7.25
    pointA.translate(1.0, -1.0)
    assert 4.5 == pointA.x
    assert 6.25 == pointA.y