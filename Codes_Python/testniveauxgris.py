import numpy as np
import cv2

# Dimensions des images de test (ex: 256x256 pixels)
largeur = 256
hauteur = 256

# ==========================================
# 1. Le Dégradé Linéaire (0 à 255)
# ==========================================
# On crée une ligne de 0 à 255, qu'on répète sur toute la hauteur
ligne_degrade = np.linspace(0, 255, largeur, dtype=np.uint8)
mire_degrade = np.tile(ligne_degrade, (hauteur, 1))

cv2.imwrite('mire_degrade.png', mire_degrade)

# ==========================================
# 2. L'Échelle de Gris à paliers (8 bandes)
# ==========================================
mire_paliers = np.zeros((hauteur, largeur), dtype=np.uint8)
largeur_bande = largeur // 8
valeurs_paliers = np.linspace(0, 255, 8, dtype=np.uint8)

for i in range(8):
    debut_x = i * largeur_bande
    fin_x = debut_x + largeur_bande
    mire_paliers[:, debut_x:fin_x] = valeurs_paliers[i]

cv2.imwrite('mire_paliers.png', mire_paliers)

# ==========================================
# 3. Le Damier (Grille 8x8 cases)
# ==========================================
mire_damier = np.zeros((hauteur, largeur), dtype=np.uint8)
taille_case = largeur // 8

for y in range(8):
    for x in range(8):
        # Si la somme des coordonnées de la case est paire, on met du blanc (255)
        if (x + y) % 2 == 0:
            mire_damier[y*taille_case:(y+1)*taille_case, x*taille_case:(x+1)*taille_case] = 255

cv2.imwrite('mire_damier.png', mire_damier)

print("Les 3 mires synthétiques ont été générées avec succès !")