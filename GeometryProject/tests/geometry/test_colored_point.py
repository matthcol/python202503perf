import pytest
from geometry.point import ColoredPoint

@pytest.fixture
def coloredPointB() -> ColoredPoint:
    return ColoredPoint(name="B", x=8.5, y=10.25, color="red")

def test_constructor_default():
    p = ColoredPoint()
    assert p.name is None
    assert 0.0 == p.x
    assert 0.0 == p.y
    assert "#000000" == p.color

def test_constructor_all_args(coloredPointB):
    assert "B" == coloredPointB.name
    assert 8.5 == coloredPointB.x
    assert 10.25 == coloredPointB.y
    assert "red" == coloredPointB.color