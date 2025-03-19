import pytest

from geometry.point import Point

# common fixtures of the package geometry
# https://docs.pytest.org/en/stable/how-to/fixtures.html
# https://docs.pytest.org/en/stable/reference/fixtures.html#reference-fixtures

@pytest.fixture
def pointA() -> Point:
    return Point(name="A", x=3.5, y=7.25)