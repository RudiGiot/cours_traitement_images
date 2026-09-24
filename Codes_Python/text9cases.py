import numpy as np
import matplotlib.pyplot as plt

# 1. Création d'une matrice vide 300x300 avec 3 canaux (RGB)
# Le type uint8 (0 à 255) est le standard pour les images
mire = np.zeros((300, 300, 3), dtype=np.uint8)

# 2. Remplissage de la Ligne 1 : Couleurs primaires (RVB)
mire[0:100, 0:100] = [255, 0, 0]       # Rouge (Red)
mire[0:100, 100:200] = [0, 255, 0]     # Vert (Green)
mire[0:100, 200:300] = [0, 0, 255]     # Bleu (Blue)

# 3. Remplissage de la Ligne 2 : Couleurs secondaires (CMJ)
mire[100:200, 0:100] = [0, 255, 255]   # Cyan (V+B)
mire[100:200, 100:200] = [255, 0, 255] # Magenta (R+B)
mire[100:200, 200:300] = [255, 255, 0] # Jaune (R+V)

# 4. Remplissage de la Ligne 3 : Niveaux de gris
mire[200:300, 0:100] = [0, 0, 0]       # Noir pur
mire[200:300, 100:200] = [255, 255, 255] # Blanc pur
mire[200:300, 200:300] = [128, 128, 128] # Gris moyen

# 5. Sauvegarde de l'image
plt.imsave('mire_couleurs.png', mire)
print("Image 'mire_couleurs.png' de 300x300 pixels générée !")