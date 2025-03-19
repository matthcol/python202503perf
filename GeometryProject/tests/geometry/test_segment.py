# TODO: test constructor + translate

import pytest

from geometry.line import Segment


@pytest.fixture
def segmentAB(pointA, pointB):
    return Segment(name="AB", ends=(pointA, pointB))

def test_constructor_default():
    s = Segment()
    assert s.name is None
    p1, p2 = s.ends
    assert 0.0 == p1.x
    assert 0.0 == p1.y
    assert 0.0 == p2.x
    assert 0.0 == p2.y

def test_constructor_all_args(segmentAB, pointA, pointB):
    assert "AB" == segmentAB.name
    p1, p2 = segmentAB.ends
    assert pointA is p1
    assert pointB is p2

def test_translate(segmentAB):
    # coords before: 
    # - A: x=3.5, y=7.25
    # - B: x=7.5, y=10.25
    previous_length = segmentAB.length()
    segmentAB.translate(1.0, -1.0)
    new_length = segmentAB.length()
    p1, p2 = segmentAB.ends
    assert new_length == pytest.approx(previous_length, 1E-15)
    assert 4.5 == p1.x
    assert 6.25 == p1.y
    assert 8.5 == p2.x
    assert 9.25 == p2.y

def test_length(segmentAB):
    assert 5.0 == segmentAB.length()