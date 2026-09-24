import numpy as np
import matplotlib.pyplot as plt

# 1. Chargement de la matrice
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

# 2. Calculs mathématiques des projections
Pv = np.sum(matrice, axis=1) # Somme par ligne
Ph = np.sum(matrice, axis=0) # Somme par colonne

# ==========================================
# GRAPHIQUE 1 : Projection Verticale Pv(n)
# ==========================================
fig1, ax1 = plt.subplots(figsize=(6, 5))
fig1.patch.set_facecolor('#ffffff')
ax1.set_facecolor('#fafafa')

lignes = np.arange(len(Pv))
ax1.barh(lignes, Pv, color='#1f77b4', zorder=3)
ax1.invert_yaxis() # Ligne 0 en haut
ax1.set_title("Projection Verticale $P_v(n)$", fontsize=13, fontweight='bold')
ax1.set_ylabel("Lignes de l'image (n)", fontweight='bold')
ax1.set_xlabel("Somme des intensités", fontweight='bold')
ax1.set_yticks(lignes)

ax1.grid(color='white', linewidth=1.5, axis='both', zorder=0)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_color('#dddddd')
ax1.spines['bottom'].set_color('#333333')

fig1.tight_layout()
fig1.savefig('projection_verticale.png', dpi=300, bbox_inches='tight')

# ==========================================
# GRAPHIQUE 2 : Projection Horizontale Ph(m)
# ==========================================
fig2, ax2 = plt.subplots(figsize=(8, 5))
fig2.patch.set_facecolor('#ffffff')
ax2.set_facecolor('#fafafa')

colonnes = np.arange(len(Ph))
ax2.bar(colonnes, Ph, color='#1f77b4', zorder=3)
ax2.set_title("Projection Horizontale $P_h(m)$", fontsize=13, fontweight='bold')
ax2.set_xlabel("Colonnes de l'image (m)", fontweight='bold')
ax2.set_ylabel("Somme des intensités", fontweight='bold')
ax2.set_xticks(colonnes)

ax2.grid(color='white', linewidth=1.5, axis='both', zorder=0)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_color('#dddddd')
ax2.spines['bottom'].set_color('#333333')

fig2.tight_layout()
fig2.savefig('projection_horizontale.png', dpi=300, bbox_inches='tight')

print("Les deux images ont été générées avec succès !")