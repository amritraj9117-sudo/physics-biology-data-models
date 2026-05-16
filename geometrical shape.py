class Cuboid(object):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height
        
    def volume(self):
        return self.height * self.breadth * self.length
        
    def __str__(self):
        return f"l={self.length} : b={self.breadth} : h={self.height}"

class Coordinate(object):
    def __init__(self, xval, yval):
        self.x = xval
        self.y = yval
        
    def distance(self, other):
        x_diff_sq = (self.x - other.x)**2
        y_diff_sq = (self.y - other.y)**2
        return (x_diff_sq + y_diff_sq)**0.5

class Circle(object):
    def __init__(self, center, radius):
        assert isinstance(center, Coordinate)
        self.center = center
        self.radius = radius
        
    def is_inside(self, point):
        """Returns True if point is inside the circle."""
        return self.center.distance(point) < self.radius
import turtle
he=turtle.Turtle()
he.speed(10)
he.color('red','yellow')
he.begin_fill() 
screen=he.getscreen() 
he.forward(350) 
he.left(90)
he.forward(50)
he.left(90)
he.forward(50) 
he.right(50)
he.forward(70)
he.left(50)
he.forward(70) 
he.left(90)
he.forward(60) 
he.right(90)
he.forward(185)
he.left(90)
he.forward(50) 
he.end_fill()
he.left(90) 
he.penup()
he.forward(40)
he.right(90)
he.forward(25)
he.pendown() 
he.color('red','black')
he.begin_fill()
he.circle(30)
he.end_fill() 
he.penup() 
he.left(90)
he.forward(250)
he.left(90)
he.pendown()
he.color('red','black') 
he.begin_fill()
he.circle(30)
he.end_fill() 
screen.exitonclick()
turtle.done()


# --- Test Code ---
if __name__ == "__main__":
    cube = Cuboid(2, 3, 4)
    print(f"Cuboid Volume: {cube.volume()}")  # Fixed missing ()
    
    p1 = Coordinate(0, 0)
    p2 = Coordinate(3, 4)
    print(f"Distance: {p1.distance(p2)}")