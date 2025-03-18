import pytest
from geometry import Point

@pytest.fixture
def pointA():
    return Point(x=3.5, y=7.25)

def test_set_x(pointA):
    pointA.x = 4.125
    assert 4.125 == pointA.x

def test_constructor(pointA):
    assert 3.5 == pointA.x
    assert 7.25 == pointA.y

def test_distance_same(pointA):
    assert 0.0 == pointA.distance(pointA)