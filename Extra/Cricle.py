class Circle:

    def __init__(self, r):
        self.radius = r

    def diameter(self):
        d = 2 * self.radius
        return d

    def circumference(self):
        c = 2 * 3.142 * self.radius
        return c

    def area(self):
        a = 3.142 * (self.radius * self.radius)
        return a


radius = float(input("Enter the radius of circle : "))

circle = Circle(radius)

area = circle.area()
circumference = circle.circumference()
diameter = circle.diameter()

print("Area of circle : ", area)
print("Circumference of circle : ", circumference)
print("Diameter of circle : ", diameter)
