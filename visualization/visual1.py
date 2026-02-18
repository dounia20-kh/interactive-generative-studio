import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generate_visual1():
    
    df = pd.read_csv("data/weather.csv")
    
    # Nettoyer les noms de colonnes (supprime espaces + met en minuscule)
    df.columns = df.columns.str.strip().str.lower()

    # Supprimer les valeurs manquantes
    df = df.dropna()

    # Prendre automatiquement la 2ème colonne comme données principales
    y = df.iloc[:, 1].values
    x = np.arange(len(y))

    # Artistic transformation (wave-like landscape)
    plt.figure(figsize=(10,5))
    plt.fill_between(x, y, alpha=0.5)
    plt.plot(x, y, linewidth=2)

    plt.axis('off') 

    filename = "static/images/visual1.png"
    plt.savefig(filename)
    plt.close()

    return filename

