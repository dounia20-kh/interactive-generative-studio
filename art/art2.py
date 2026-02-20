import matplotlib.pyplot as plt
import random
import os


class Shape:
    def __init__(self, x, y, size, color, alpha=0.75):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.alpha = alpha

    def draw(self, ax):
        raise NotImplementedError("Each subclass must implement draw()")

    def reposition(self, dx, dy):
        self.x += dx
        self.y += dy

    def resize(self, factor):
        self.size *= factor

    def set_color(self, color):
        self.color = color


class Circle(Shape):
    def draw(self, ax):
        ax.add_patch(plt.Circle((self.x, self.y), self.size, color=self.color, alpha=self.alpha))


class Square(Shape):
    def draw(self, ax):
        ax.add_patch(plt.Rectangle((self.x - self.size/2, self.y - self.size/2),
                                   self.size, self.size, color=self.color, alpha=self.alpha))


class Triangle(Shape):
    def draw(self, ax):
        ax.add_patch(plt.Polygon(
            [(self.x, self.y),
             (self.x + self.size, self.y),
             (self.x + self.size/2, self.y + self.size)],
            color=self.color, alpha=self.alpha
        ))


def generate_art2(num_shapes=50, palette="sunset"):
    # Create folder if missing
    filename = "static/images/art2.png"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    fig, ax = plt.subplots(figsize=(6,6))

    palettes = {
        "sunset": ["#FF5733", "#FF8D1A", "#FFC300", "#C70039", "#900C3F"],
        "ocean": ["#003f5c", "#2f4b7c", "#008080", "#00b4d8", "#90e0ef"],
        "pastel": ["#FFB3BA", "#FFDFBA", "#FFFFBA", "#BAFFC9", "#BAE1FF"],
        "neon": ["#39FF14", "#FF10F0", "#00FFFF", "#FF3131", "#FFFF33"],
        "dark": ["#1a1a1a", "#333333", "#4d4d4d", "#666666", "#999999"]
    }

    background_colors = {
        "sunset": "#2b0f0f",
        "ocean": "#001f3f",
        "pastel": "#fdf6f0",
        "neon": "#000000",
        "dark": "#111111"
    }
    ax.set_facecolor(background_colors.get(palette, "white"))

    shape_classes = [Circle, Square, Triangle]
    shapes = []

    for _ in range(num_shapes):
        size = random.uniform(0.3, 1.2)
        x = random.uniform(size, 10 - size)
        y = random.uniform(size, 10 - size)

        if palette in palettes:
            color = random.choice(palettes[palette])
        else:
            color = (random.random(), random.random(), random.random())

        ShapeClass = random.choice(shape_classes)
        shapes.append(ShapeClass(x, y, size, color))

  
    for shape in shapes:
        if random.random() < 0.3:
            shape.reposition(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5))
        if random.random() < 0.2:
            shape.resize(random.uniform(0.8, 1.2))


    for shape in shapes:
        shape.draw(ax)


    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis("off")

    plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()

    return filename