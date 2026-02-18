import matplotlib.pyplot as plt
import random

def generate_art3(num_shapes=50, palette="random"):
    fig, ax = plt.subplots()

    for _ in range(num_shapes):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        size = random.uniform(0.2, 1.5)

        if palette == "random":
            color = (random.random(), random.random(), random.random())
        else:
            color = palette

        circle = plt.Circle((x, y), size, color=color, alpha=0.6)
        ax.add_patch(circle)

    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis("off")

    filename = "static/images/art3.png"
    plt.savefig(filename)
    plt.close()
    return filename
