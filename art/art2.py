import matplotlib.pyplot as plt
import random

class Shape:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color

class Circle(Shape):
    def draw(self, ax):
        ax.add_patch(plt.Circle((self.x, self.y), self.size, color=self.color, alpha=0.6))

class Square(Shape):
    def draw(self, ax):
        ax.add_patch(plt.Rectangle((self.x, self.y), self.size, self.size, color=self.color, alpha=0.6))

class Triangle(Shape):
    def draw(self, ax):
        ax.add_patch(plt.Polygon(
            [(self.x, self.y),
             (self.x + self.size, self.y),
             (self.x + self.size/2, self.y + self.size)],
            color=self.color,
            alpha=0.6
        ))

def generate_art2(num_shapes=50):
    fig, ax = plt.subplots()
    shapes = [Circle, Square, Triangle]

    for _ in range(num_shapes):
        ShapeClass = random.choice(shapes)
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        size = random.uniform(0.2, 1.5)
        color = (random.random(), random.random(), random.random())
        shape = ShapeClass(x, y, size, color)
        shape.draw(ax)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis("off")

    filename = "static/images/art2.png"
    plt.savefig(filename)
    plt.close()
    return filename
