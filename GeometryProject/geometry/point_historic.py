# module geometry.point

# En Python 3, toute classe hérite de la classe 'object'
# conventions de nommage: PEP 8

class Point:
    """represents a 2D point with its coordinates x and y
    """

    # constructor
    def __init__(self, *, x = 0.0, y = 0.0):
        """ initialize a 2D points with its coordinates x and y
        """
        self.x = x
        self.y = y

    # default: overides both str and repr
    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
