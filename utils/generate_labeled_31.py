#!/usr/bin/env python3
"""Generate labeled Young diagram for (3,1) shape"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

OUTPUT_DIR = "../docs/images/angular-momentum"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BOX_SIZE = 1.2
LINE_WIDTH = 3.0
FONT_SIZE = 28
LABEL_SIZE = 32

def draw_box(ax, x, y, label=None):
    rect = patches.Rectangle((x, y), BOX_SIZE, BOX_SIZE,
                               linewidth=LINE_WIDTH,
                               edgecolor='black',
                               facecolor='white')
    ax.add_patch(rect)
    if label:
        ax.text(x + BOX_SIZE/2, y + BOX_SIZE/2, label,
                ha='center', va='center', fontsize=LABEL_SIZE, 
                fontweight='bold', color='darkblue')

fig, ax = plt.subplots(1, 1, figsize=(5, 3))

# Draw (3,1) shape with labels A, B, C in first row, D in second
# Row 1: A B C
# Row 2: D
labels = [['A', 'B', 'C'], ['D']]
for row_idx, row_labels in enumerate(labels):
    y = (1 - row_idx) * BOX_SIZE
    for col_idx, label in enumerate(row_labels):
        x = col_idx * BOX_SIZE
        draw_box(ax, x, y, label)

ax.set_xlim(-0.15, 3 * BOX_SIZE + 0.15)
ax.set_ylim(-0.15, 2 * BOX_SIZE + 0.15)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout(pad=0.1)
filepath = os.path.join(OUTPUT_DIR, "young_31_labeled.png")
plt.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white')
print(f"Saved: {filepath}")
plt.close()
