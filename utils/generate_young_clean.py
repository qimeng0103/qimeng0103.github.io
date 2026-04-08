#!/usr/bin/env python3
"""
Generate clean Young diagrams without annotations
Simple boxes only
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

OUTPUT_DIR = "../docs/images/angular-momentum"
os.makedirs(OUTPUT_DIR, exist_ok=True)

BOX_SIZE = 1.0
LINE_WIDTH = 2.5

def draw_young_clean(shape, filename):
    """Draw clean Young diagram with simple boxes"""
    n_rows = len(shape)
    max_cols = max(shape) if shape else 0
    
    fig_width = max_cols * BOX_SIZE + 0.5
    fig_height = n_rows * BOX_SIZE + 0.5
    
    fig, ax = plt.subplots(1, 1, figsize=(fig_width, fig_height))
    
    for row_idx, n_cols in enumerate(shape):
        y = (n_rows - 1 - row_idx) * BOX_SIZE
        for col_idx in range(n_cols):
            x = col_idx * BOX_SIZE
            rect = patches.Rectangle((x, y), BOX_SIZE, BOX_SIZE,
                                       linewidth=LINE_WIDTH,
                                       edgecolor='black',
                                       facecolor='white')
            ax.add_patch(rect)
    
    ax.set_xlim(-0.15, max_cols * BOX_SIZE + 0.15)
    ax.set_ylim(-0.15, n_rows * BOX_SIZE + 0.15)
    ax.set_aspect('equal')
    ax.axis('off')
    
    plt.tight_layout(pad=0.1)
    
    filepath = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(filepath, dpi=150, bbox_inches='tight', 
               facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()

# Generate clean diagrams
draw_young_clean([1], 'young_1_clean.png')           # Single box (3)
draw_young_clean([2], 'young_2_row_clean.png')       # Two in row (6)
draw_young_clean([1,1], 'young_2_col_clean.png')     # Two in column (3-bar)
draw_young_clean([3], 'young_3_row_clean.png')       # Three in row (10)
draw_young_clean([2,1], 'young_21_clean.png')        # Hook (8)
draw_young_clean([1,1,1], 'young_3_col_clean.png')   # Three in column (1)

print("All clean Young diagrams generated!")
