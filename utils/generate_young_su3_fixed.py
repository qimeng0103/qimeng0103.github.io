#!/usr/bin/env python3
"""
Generate Young diagrams for SU(3) representations
High quality output for the angular momentum article
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os

# Set output directory
OUTPUT_DIR = "../docs/images/angular-momentum"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Common styling
BOX_SIZE = 1.0
LINE_WIDTH = 2
FONT_SIZE = 16
ANNOTATION_SIZE = 12

def draw_box(ax, x, y, label=None, color='black', fill_color='white'):
    """Draw a single box in Young diagram"""
    rect = patches.Rectangle((x, y), BOX_SIZE, BOX_SIZE, 
                               linewidth=LINE_WIDTH, 
                               edgecolor=color, 
                               facecolor=fill_color)
    ax.add_patch(rect)
    if label:
        ax.text(x + BOX_SIZE/2, y + BOX_SIZE/2, label, 
                ha='center', va='center', fontsize=FONT_SIZE, fontweight='bold')

def draw_young_diagram(shape, labels=None, filename=None, title=None, annotations=None):
    """
    Draw a Young diagram given a shape
    shape: list of row lengths, e.g., [2,1] for hook, [3] for three in row
    labels: list of labels for each box (row-major order)
    annotations: dict of {box_index: annotation_text} for showing hook calculation
    """
    n_rows = len(shape)
    max_cols = max(shape)
    
    # Calculate figure size
    fig_width = max_cols * BOX_SIZE + 1
    fig_height = n_rows * BOX_SIZE + 1
    
    fig, ax = plt.subplots(1, 1, figsize=(fig_width, fig_height))
    
    # Draw boxes from top to bottom
    box_idx = 0
    for row_idx, n_cols in enumerate(shape):
        y = (n_rows - 1 - row_idx) * BOX_SIZE  # Flip y so row 0 is at top
        for col_idx in range(n_cols):
            x = col_idx * BOX_SIZE
            label = labels[box_idx] if labels and box_idx < len(labels) else None
            draw_box(ax, x, y, label)
            
            # Add annotation if provided
            if annotations and box_idx in annotations:
                ann_text = annotations[box_idx]
                # Position annotation outside the box
                ax.text(x + BOX_SIZE/2, y - 0.3, ann_text, 
                       ha='center', va='top', fontsize=ANNOTATION_SIZE, 
                       color='darkblue', style='italic')
            
            box_idx += 1
    
    # Set limits
    ax.set_xlim(-0.2, max_cols * BOX_SIZE + 0.2)
    ax.set_ylim(-0.5 if annotations else -0.2, n_rows * BOX_SIZE + 0.2)
    ax.set_aspect('equal')
    ax.axis('off')
    
    if title:
        ax.set_title(title, fontsize=14, pad=10)
    
    plt.tight_layout()
    
    if filename:
        filepath = os.path.join(OUTPUT_DIR, filename)
        plt.savefig(filepath, dpi=150, bbox_inches='tight', 
                   facecolor='white', edgecolor='none')
        print(f"Saved: {filepath}")
    
    plt.close()
    return fig, ax

# 1. Single box - Fundamental 3
draw_young_diagram([1], labels=['3'], filename='young_single.png', 
                   title=r'Fundamental $\mathbf{3} = \{u, d, s\}$')

# 2. Two boxes in row - Symmetric 6
draw_young_diagram([2], labels=None, filename='young_two_row.png',
                   title=r'Symmetric $\mathbf{6}$')

# 3. Two boxes in column - Antisymmetric 3-bar
draw_young_diagram([1, 1], labels=None, filename='young_two_col.png',
                   title=r'Antisymmetric $\bar{\mathbf{3}}$')

# 4. Three boxes in row - Decuplet 10
draw_young_diagram([3], labels=None, filename='young_three_row.png',
                   title=r'Fully Symmetric $\mathbf{10}$ (Decuplet)')

# 5. Hook shape {2,1} - Octet 8 with annotations for dimension calculation
hook_annotations = {
    0: 'r=0,c=0\nh=3',
    1: 'r=0,c=1\nh=1', 
    2: 'r=1,c=0\nh=1'
}
draw_young_diagram([2, 1], labels=['A', 'B', 'C'], filename='young_hook.png',
                   title=r'Mixed Symmetry $\mathbf{8}$ (Octet) - Partition $\{2,1\}$',
                   annotations=hook_annotations)

# 6. Three boxes in column - Singlet 1 with annotations
col_annotations = {
    0: 'r=0,c=0\nh=3',
    1: 'r=1,c=0\nh=2',
    2: 'r=2,c=0\nh=1'
}
draw_young_diagram([1, 1, 1], labels=['A', 'B', 'C'], filename='young_three_col.png',
                   title=r'Fully Antisymmetric $\mathbf{1}$ (Singlet) - Partition $\{1,1,1\}$',
                   annotations=col_annotations)

# 7. Tensor product 3 x 3 = 6 + 3-bar (visual summary)
fig, axes = plt.subplots(1, 3, figsize=(10, 3))

# Left: 3
ax = axes[0]
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
draw_box(ax, 0, 0, label=None)
ax.text(0.5, -0.3, r'$\mathbf{3}$', ha='center', fontsize=14)
ax.axis('off')
ax.set_aspect('equal')

# Middle: product symbol
axes[1].text(0.5, 0.5, r'$\otimes$', ha='center', va='center', fontsize=24)
axes[1].axis('off')
axes[1].set_xlim(0, 1)
axes[1].set_ylim(0, 1)

# Right: another 3
ax = axes[2]
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.2, 1.2)
draw_box(ax, 0, 0, label=None)
ax.text(0.5, -0.3, r'$\mathbf{3}$', ha='center', fontsize=14)
ax.axis('off')
ax.set_aspect('equal')

plt.tight_layout()
filepath = os.path.join(OUTPUT_DIR, 'young_3_tensor_3.png')
plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Saved: {filepath}")
plt.close()

# 8. Result: 6 + 3-bar
fig, axes = plt.subplots(1, 3, figsize=(12, 3))

# Left: 6 (row)
ax = axes[0]
ax.set_xlim(-0.2, 2.2)
ax.set_ylim(-0.2, 1.2)
draw_box(ax, 0, 0)
draw_box(ax, 1, 0)
ax.text(1, -0.3, r'$\mathbf{6}$ (symmetric)', ha='center', fontsize=12)
ax.axis('off')
ax.set_aspect('equal')

# Middle: plus symbol
axes[1].text(0.5, 0.5, r'$\oplus$', ha='center', va='center', fontsize=24)
axes[1].axis('off')
axes[1].set_xlim(0, 1)
axes[1].set_ylim(0, 1)

# Right: 3-bar (column)
ax = axes[2]
ax.set_xlim(-0.2, 1.2)
ax.set_ylim(-0.5, 2.2)
draw_box(ax, 0, 1)
draw_box(ax, 0, 0)
ax.text(0.5, -0.3, r'$\bar{\mathbf{3}}$ (antisymmetric)', ha='center', fontsize=12)
ax.axis('off')
ax.set_aspect('equal')

plt.tight_layout()
filepath = os.path.join(OUTPUT_DIR, 'young_3x3_result.png')
plt.savefig(filepath, dpi=150, bbox_inches='tight', facecolor='white')
print(f"Saved: {filepath}")
plt.close()

# 9. Full decomposition 3 x 3 x 3 = 10 + 8 + 8 + 1
fig = plt.figure(figsize=(14, 5))

# Title
fig.suptitle(r'$\mathbf{3} \otimes \mathbf{3} \otimes \mathbf{3} = \mathbf{10} \oplus \mathbf{8} \oplus \mathbf{8} \oplus \mathbf{1}$', 
             fontsize=16, y=0.95)

# Create grid
gs = fig.add_gridspec(2, 4, hspace=0.3, wspace=0.2)

# Row 1: three quarks
ax1 = fig.add_subplot(gs[0, 0])
draw_box(ax1, 0, 0)
ax1.text(0.5, -0.2, r'$\mathbf{3}$', ha='center', fontsize=12)
ax1.axis('off')
ax1.set_aspect('equal')

ax2 = fig.add_subplot(gs[0, 1])
ax2.text(0.5, 0.5, r'$\otimes$', ha='center', va='center', fontsize=20)
ax2.axis('off')

ax3 = fig.add_subplot(gs[0, 2])
draw_box(ax3, 0, 0)
ax3.text(0.5, -0.2, r'$\mathbf{3}$', ha='center', fontsize=12)
ax3.axis('off')
ax3.set_aspect('equal')

ax4 = fig.add_subplot(gs[0, 3])
ax4.text(0.5, 0.5, r'$\otimes$', ha='center', va='center', fontsize=20)
ax4.axis('off')

# Row 2: results
# 10
ax = fig.add_subplot(gs[1, 0])
draw_box(ax, 0, 0)
draw_box(ax, 1, 0)
draw_box(ax, 2, 0)
ax.text(1.5, -0.3, r'$\mathbf{10}$', ha='center', fontsize=14, fontweight='bold')
ax.axis('off')
ax.set_aspect('equal')

# 8 (hook 1)
ax = fig.add_subplot(gs[1, 1])
draw_box(ax, 0, 0.5)
draw_box(ax, 1, 0.5)
draw_box(ax, 0, -0.5)
ax.text(0.5, -1, r'$\mathbf{8}_1$', ha='center', fontsize=14, fontweight='bold')
ax.axis('off')
ax.set_aspect('equal')

# 8 (hook 2)
ax = fig.add_subplot(gs[1, 2])
draw_box(ax, 0, 0.5)
draw_box(ax, 1, 0.5)
draw_box(ax, 0, -0.5)
ax.text(0.5, -1, r'$\mathbf{8}_2$', ha='center', fontsize=14, fontweight='bold')
ax.axis('off')
ax.set_aspect('equal')

# 1
ax = fig.add_subplot(gs[1, 3])
draw_box(ax, 0, 1)
draw_box(ax, 0, 0)
draw_box(ax, 0, -1)
ax.text(0.5, -1.8, r'$\mathbf{1}$', ha='center', fontsize=14, fontweight='bold')
ax.axis('off')
ax.set_aspect('equal')

plt.savefig(os.path.join(OUTPUT_DIR, 'young_baryon_decomposition.png'), 
           dpi=150, bbox_inches='tight', facecolor='white')
print(f"Saved: {os.path.join(OUTPUT_DIR, 'young_baryon_decomposition.png')}")
plt.close()

print("\nAll Young diagrams generated successfully!")
