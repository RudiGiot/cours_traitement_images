import numpy as np
import matplotlib.pyplot as plt

# 1. Chargement de la matrice du cours
matrice = np.array([
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250, 250, 250, 250, 250, 250, 250, 250],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250, 250, 250, 250, 250, 250, 250, 250],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250, 250, 250, 250, 250, 250, 250, 250],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250, 250, 250, 250, 250, 250, 250, 250],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250, 250, 250, 250,   0, 250, 250, 250],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250, 250, 250, 250, 250, 250, 250, 250],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250,   0, 250, 250, 250, 250, 250, 250],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250, 250, 250, 250, 250, 250, 250, 250],
    [10, 25, 30, 45, 50, 69, 70, 71, 90, 250, 250, 250, 250, 250, 250, 250, 250, 250]
])

# 2. Calcul des fréquences (Histogramme)
valeurs, occurences = np.unique(matrice, return_counts=True)

# 3. Création du graphique
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_facecolor('#fafafa')
fig.patch.set_facecolor('#ffffff')
ax.grid(color='white', linewidth=1.5, axis='y', zorder=0)

# Largeur fine (0.8) pour bien séparer les valeurs 69, 70 et 71
ax.bar(valeurs, occurences, width=0.8, color='#1f77b4', zorder=3)

# Personnalisation des textes
ax.set_title("Histogramme des niveaux de gris de la matrice", fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel("Niveaux de gris (0 à 255)", fontsize=11, fontweight='bold', color='#333333')
ax.set_ylabel("Nombre de pixels", fontsize=11, fontweight='bold', color='#333333')

# Échelle X de 0 à 255
ax.set_xlim(-5, 260)
ax.set_xticks([0, 50, 100, 150, 200, 255])

# Épuration des bordures
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#dddddd')
ax.spines['bottom'].set_color('#333333')

# Ajout du chiffre exact au-dessus de chaque barre pour la clarté pédagogique
for i in range(len(valeurs)):
    ax.text(valeurs[i], occurences[i] + 1.5, str(occurences[i]), 
            ha='center', va='bottom', fontsize=8, color='#555555')

plt.tight_layout()

# Génération du fichier (à exécuter dans Colab ou localement)
plt.savefig('histogramme_exemple.png', dpi=300, bbox_inches='tight')
plt.show()