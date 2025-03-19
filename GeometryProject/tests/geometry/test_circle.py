import pytest

from geometry import Circle


@pytest.fixture
def circleC(pointA) -> Circle:
    return Circle(
        name="C",
        radius=10.0,
        center=pointA
    )

def test_constructor_default():
    c = Circle()
    assert c.name is None
    assert 1.0 == c.radius
    assert c.center is not None
    assert c.center.name is None
    assert 0.0 == c.center.x
    assert 0.0 == c.center.y

def test_constructor_all_args(circleC, pointA):
    assert circleC.name == "C"
    assert 10.0 == circleC.radius
    assert circleC.center is not None
    assert pointA is circleC.center

def test_translate(circleC):
    # before: centre: x=3.5, y=7.25
    circleC.translate(1.0, -1.0)
    assert 4.5 == circleC.center.x
    assert 6.25 == circleC.center.y
    
def test_area(circleC):
    assert pytest.approx(314.1592653589793, rel=1E-15) == circleC.area()

def test_perimeter(circleC):
    assert pytest.approx(62.83185307179586, rel=1E-15) == circleC.perimeter()
