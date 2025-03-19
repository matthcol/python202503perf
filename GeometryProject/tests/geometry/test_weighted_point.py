import pytest
from geometry.point import WeightedPoint

@pytest.fixture
def weightedPointC() -> WeightedPoint:
    return WeightedPoint(name="C", x=8.5, y=10.25, weight=1.5E3)

def test_constructor_default():
    p = WeightedPoint()
    assert p.name is None
    assert 0.0 == p.x
    assert 0.0 == p.y
    assert 1.0 == p.weight

def test_constructor_all_args(weightedPointC):
    assert "C" == weightedPointC.name
    assert 8.5 == weightedPointC.x
    assert 10.25 == weightedPointC.y
    assert 1.5E3 == weightedPointC.weight