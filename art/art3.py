import matplotlib.pyplot as plt
import random
import os

def generate_art3(num_shapes=50, palette="sunset"):
    # Ensure folder exists
    filename = "static/images/art3.png"
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

    
    for _ in range(num_shapes):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        size = random.uniform(0.2, 1.5)

        if palette in palettes:
            color = random.choice(palettes[palette])
        else:
            color = (random.random(), random.random(), random.random())

        circle = plt.Circle((x, y), size, color=color, alpha=0.6)
        ax.add_patch(circle)

   
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_aspect('equal')
    ax.axis("off")

    plt.savefig(filename, bbox_inches='tight', pad_inches=0, dpi=300)
    plt.close()

    return filename
