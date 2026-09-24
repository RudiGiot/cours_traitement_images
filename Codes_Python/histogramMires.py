import cv2
import matplotlib.pyplot as plt
import numpy as np

# Liste des images à analyser et des histogrammes à produire
fichiers = [
    ('mire_degrade.png', 'hist_degrade.png', 'Histogramme : Dégradé Linéaire (Équiprobabilité)'),
    ('mire_paliers.png', 'hist_paliers.png', 'Histogramme : Paliers (Quantification)'),
    ('mire_damier.png', 'hist_damier.png', 'Histogramme : Damier (Bimodal pur)')
]

for img_in, hist_out, titre in fichiers:
    # 1. Lecture de l'image en forçant le mode niveaux de gris
    img = cv2.imread(img_in, cv2.IMREAD_GRAYSCALE)
    
    if img is None:
        print(f"Erreur : Impossible de trouver '{img_in}'. Avez-vous exécuté le script précédent ?")
        continue

    # 2. Extraction des valeurs exactes (idéal pour les mires mathématiques)
    valeurs, occurrences = np.unique(img, return_counts=True)

    # 3. Création du graphique
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_facecolor('#ffffff')
    ax.set_facecolor('#fafafa')

    # Tracé en barres (width=1.5 pour rendre les pics isolés bien visibles)
    ax.bar(valeurs, occurrences, width=1.5, color='#1f77b4', zorder=3)

    # 4. Esthétique et lisibilité
    ax.set_title(titre, fontsize=12, fontweight='bold', pad=10)
    ax.set_xlabel("Niveaux de gris (0 à 255)", fontsize=10, fontweight='bold')
    ax.set_ylabel("Nombre de pixels", fontsize=10, fontweight='bold')
    
    # On force l'axe X de 0 à 255 pour comparer honnêtement les 3 graphiques
    ax.set_xlim(-5, 260)
    ax.set_xticks([0, 50, 100, 150, 200, 255])
    
    # Nettoyage visuel
    ax.grid(color='white', linewidth=1.5, axis='y', zorder=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#dddddd')
    ax.spines['bottom'].set_color('#333333')

    plt.tight_layout()
    plt.savefig(hist_out, dpi=300, bbox_inches='tight')
    plt.close() # Ferme la figure pour libérer la mémoire

print("Les 3 histogrammes ont été générés avec succès !")