import pytest
from geometry.point import ColoredWeightedPoint

@pytest.fixture
def coloredWeightedPointC() -> ColoredWeightedPoint:
    return ColoredWeightedPoint(name="D", x=8.5, y=10.25, weight=1.5E3, color="red")

def test_constructor_default():
    p = ColoredWeightedPoint()
    assert p.name is None
    assert 0.0 == p.x
    assert 0.0 == p.y
    assert "#000000" == p.color
    assert 1.0 == p.weight
    

def test_constructor_all_args(coloredWeightedPointC):
    assert "D" == coloredWeightedPointC.name
    assert 8.5 == coloredWeightedPointC.x
    assert 10.25 == coloredWeightedPointC.y
    assert "red" == coloredWeightedPointC.color
    assert 1.5E3 == coloredWeightedPointC.weight