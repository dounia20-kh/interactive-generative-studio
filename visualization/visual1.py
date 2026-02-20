import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_visual1(file_path="data/weather.csv"):
    # Charger le CSV
    df = pd.read_csv(file_path)

    # Nettoyer les noms de colonnes
    df.columns = df.columns.str.strip().str.lower()

    # Supprimer les lignes vides
    df = df.dropna(how='all')

    # Convertir toutes les colonnes numériques en float
    for col in df.columns:
        if col != 'location' and col != 'date_time':
            df[col] = df[col].astype(str).str.replace(' ', '').str.replace(',', '.')
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Supprimer les lignes où toutes les colonnes numériques sont NaN
    numeric_cols = [col for col in df.columns if col not in ['location', 'date_time']]
    df = df.dropna(subset=numeric_cols, how='all')

    # Prendre la première colonne numérique comme Y
    y = df[numeric_cols[0]].values
    x = np.arange(len(y))

    # Création de plusieurs vagues pour un effet artistique
    plt.figure(figsize=(12,6))
    colors = ['#ffadad','#ffd6a5','#fdffb6','#caffbf','#9bf6ff','#a0c4ff','#bdb2ff']
    
    for i, color in enumerate(colors):
        offset = i * 1.5  # décalage vertical pour superposer les vagues
        y_wave = y + np.sin(x * (0.3 + i*0.1)) * (2 + i) + offset
        plt.fill_between(x, y_wave, alpha=0.5, color=color)

    # Ligne principale
    y_wave_main = y + np.sin(x * 0.5) * 2
    plt.plot(x, y_wave_main, color='#03045e', linewidth=2)

    # Retirer axes pour un rendu artistique
    plt.axis('off')

    # Sauvegarder
    filename = "static/images/visual1.png"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()

    return filename