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

p1 = geo.Point()
p2 = geo.Point()

for p in p1, p2:
    print(p)