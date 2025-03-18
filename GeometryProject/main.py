# application: main.py

# import v11:
# from geometry.point import Point

# p1 = Point()
# p2 = Point()

# import v2
# import geometry.point as pt

# p1 = pt.Point()
# p2 = pt.Point()

# import v3:
# import geometry.point

# p1 = geometry.point.Point()
# p2 = geometry.point.Point()

# import v4 (using imports in geometry.__init__)
import geometry as geo

p1 = geo.Point() # calls __new__ then __init__
# p2 = geo.Point(2.0, 4.5) # args by position (if enabled)
p3 = geo.Point(x=4.75, y=7.5) # args by keyword
p3bis = geo.Point(x=4.75, y=7.5)
assert p3 == p3bis
assert p3 is not p3bis

for p in p1, p3:
    print(p) # uses str()
    print(str(p))
    print(repr(p))
    print(p.x, p.y)
    print()

d = p1.distance(p3)
print("distance:", d)