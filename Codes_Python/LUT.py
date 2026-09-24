import numpy as np
import matplotlib.pyplot as plt

# 1. Création de l'axe des abscisses (les valeurs d'entrée de 0 à 255)
u = np.arange(0, 256)

# 2. Définition des 4 opérations mathématiques (LUTs)
# LUT 1 : Identité (ligne à 45°)
lut_identite = u

# LUT 2 : Négatif (ligne à -45°)
lut_negatif = 255 - u

# LUT 3 : Seuillage (t = 127)
lut_seuillage = np.where(u > 127, 255, 0)

# LUT 4 : Écrêtage / Clip (plancher cf=60, plafond cc=195)
lut_clip = np.clip(u, 60, 195)

# 3. Création de la figure (Grille 2x2)
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
fig.patch.set_facecolor('#ffffff')

luts = [
    (axs[0, 0], lut_identite, "Identité (Aucune modification)", '#1f77b4'),
    (axs[0, 1], lut_negatif, "Négatif (Inversion des couleurs)", '#ff7f0e'),
    (axs[1, 0], lut_seuillage, "Seuillage (Binarisation à t=127)", '#2ca02c'),
    (axs[1, 1], lut_clip, "Écrêtage (Clip entre 60 et 195)", '#d62728')
]

# 4. Tracé et esthétique de chaque graphique
for ax, lut_data, titre, couleur in luts:
    ax.set_facecolor('#fafafa')
    ax.plot(u, lut_data, color=couleur, linewidth=3, zorder=3)
    
    # Paramétrage des axes
    ax.set_title(titre, fontsize=12, fontweight='bold', pad=10)
    ax.set_xlabel("Valeur d'entrée ($u$)", fontsize=10)
    ax.set_ylabel("Valeur de sortie ($v$)", fontsize=10)
    
    # Limites strictes de 0 à 255 pour représenter un octet
    ax.set_xlim(0, 255)
    ax.set_ylim(-5, 260)
    ax.set_xticks([0, 64, 128, 192, 255])
    ax.set_yticks([0, 64, 128, 192, 255])
    
    # Esthétique
    ax.grid(color='white', linewidth=1.5, zorder=0)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#dddddd')
    ax.spines['bottom'].set_color('#333333')

plt.tight_layout(pad=3.0)

# 5. Sauvegarde de l'image
plt.savefig('exemples_lut.png', dpi=300, bbox_inches='tight')
print("Image 'exemples_lut.png' générée !")