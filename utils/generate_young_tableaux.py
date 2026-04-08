#!/usr/bin/env python3
"""
Generate Young tableaux with numbers
Clean style matching young diagrams
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

OUTPUT_DIR = "../docs/images/angular-momentum"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BOX_SIZE = 1.2
LINE_WIDTH = 3.0
FONT_SIZE = 28

def draw_box_with_number(ax, x, y, number=None):
    """Draw a single box with optional number"""
    rect = patches.Rectangle((x, y), BOX_SIZE, BOX_SIZE,
                               linewidth=LINE_WIDTH,
                               edgecolor='black',
                               facecolor='white')
    ax.add_patch(rect)
    if number is not None:
        ax.text(x + BOX_SIZE/2, y + BOX_SIZE/2, str(number),
                ha='center', va='center', fontsize=FONT_SIZE, fontweight='bold')

def draw_tableau(shape, numbers, filename, title=None):
    """Draw a Young tableau with given shape and numbers"""
    n_rows = len(shape)
    max_cols = max(shape)
    
    fig_width = max_cols * BOX_SIZE + 0.5
    fig_height = n_rows * BOX_SIZE + 0.5
    
    fig, ax = plt.subplots(1, 1, figsize=(fig_width, fig_height))
    
    idx = 0
    for row_idx, n_cols in enumerate(shape):
        y = (n_rows - 1 - row_idx) * BOX_SIZE
        for col_idx in range(n_cols):
            x = col_idx * BOX_SIZE
            number = numbers[idx] if idx < len(numbers) else None
            draw_box_with_number(ax, x, y, number)
            idx += 1
    
    ax.set_xlim(-0.15, max_cols * BOX_SIZE + 0.15)
    ax.set_ylim(-0.15, n_rows * BOX_SIZE + 0.15)
    ax.set_aspect('equal')
    ax.axis('off')
    
    if title:
        ax.set_title(title, fontsize=14, pad=10)
    
    plt.tight_layout(pad=0.1)
    
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white')
    print(f"Saved: {filepath}")
    plt.close()

# Two-electron symmetric (triplet) - tableau [12]
draw_tableau([2], [1, 2], 'tableau_2_symmetric.png', 'Symmetric: [12]')

# Two-electron antisymmetric (singlet) - tableau [1/2]
draw_tableau([1, 1], [1, 2], 'tableau_2_antisymmetric.png', 'Antisymmetric: [1|2]')

# Three-electron fully symmetric
draw_tableau([3], [1, 2, 3], 'tableau_3_symmetric.png', 'Fully Symmetric: [123]')

# Three-electron hook (mixed symmetry) - two standard tableaux
draw_tableau([2, 1], [1, 2, 3], 'tableau_3_hook_1.png', 'Mixed: [12|3]')
draw_tableau([2, 1], [1, 3, 2], 'tableau_3_hook_2.png', 'Mixed: [13|2]')

print("\nAll Young tableaux generated!")
