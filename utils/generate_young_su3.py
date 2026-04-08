#!/usr/bin/env python3
"""
Generate Young diagrams for SU(3) tensor products.
Clean, minimal diagrams for article.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style

OUTPUT_DIR = 'docs/images/angular-momentum'


def draw_single_box(ax, x, y, box_size=1.0, linewidth=1.5, fill_color='white'):
    """Draw a single box."""
    rect = patches.Rectangle(
        (x, y), box_size, box_size,
        linewidth=linewidth,
        edgecolor='black',
        facecolor=fill_color,
        joinstyle='miter'
    )
    ax.add_patch(rect)


def draw_young_partition(ax, partition, start_x=0, start_y=0, box_size=1.0, 
                         linewidth=1.5, fill_colors=None):
    """Draw a Young diagram from partition."""
    if fill_colors is None:
        fill_colors = ['white'] * sum(partition)
    
    color_idx = 0
    for i, row_len in enumerate(partition):
        for j in range(row_len):
            color = fill_colors[color_idx] if color_idx < len(fill_colors) else 'white'
            draw_single_box(ax, start_x + j*box_size, start_y - i*box_size, 
                          box_size, linewidth, color)
            color_idx += 1


def draw_tensor_product_3x3():
    """Draw 3 x 3 = 6 + 3bar tensor product."""
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 3.5))
    
    box_size = 0.8
    
    # First box (3)
    draw_young_partition(ax, [1], start_x=0, start_y=0, box_size=box_size)
    ax.text(0.4, -1.3, r'$\mathbf{3}$', fontsize=14, ha='center', fontweight='bold')
    
    # Times symbol
    ax.text(1.2, -0.4, r'$\otimes$', fontsize=16, ha='center', va='center')
    
    # Second box (3)
    draw_young_partition(ax, [1], start_x=1.8, start_y=0, box_size=box_size)
    ax.text(2.2, -1.3, r'$\mathbf{3}$', fontsize=14, ha='center', fontweight='bold')
    
    # Equals
    ax.text(3.0, -0.4, r'$=$', fontsize=16, ha='center', va='center')
    
    # Symmetric (6) - two boxes in a row
    draw_young_partition(ax, [2], start_x=3.8, start_y=0, box_size=box_size)
    ax.text(4.4, -1.3, r'$\mathbf{6}$ (symmetric)', fontsize=12, ha='center')
    
    # Plus
    ax.text(5.6, -0.4, r'$\oplus$', fontsize=16, ha='center', va='center')
    
    # Antisymmetric (3bar) - two stacked boxes
    draw_young_partition(ax, [1, 1], start_x=6.4, start_y=0, box_size=box_size)
    ax.text(6.8, -2.1, r'$\bar{\mathbf{3}}$ (antisymmetric)', fontsize=12, ha='center')
    
    ax.set_xlim(-0.3, 8.5)
    ax.set_ylim(-2.5, 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'$\mathbf{3} \otimes \mathbf{3} = \mathbf{6} \oplus \bar{\mathbf{3}}$', 
                fontsize=14, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'young_3x3_product.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def draw_tensor_product_3x3bar():
    """Draw 3 x 3bar = 8 + 1 tensor product."""
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 3.5))
    
    box_size = 0.8
    
    # First box (3)
    draw_young_partition(ax, [1], start_x=0, start_y=0, box_size=box_size)
    ax.text(0.4, -1.3, r'$\mathbf{3}$', fontsize=14, ha='center', fontweight='bold')
    
    # Times symbol
    ax.text(1.2, -0.4, r'$\otimes$', fontsize=16, ha='center', va='center')
    
    # 3bar - stacked boxes
    draw_young_partition(ax, [1, 1], start_x=1.8, start_y=0, box_size=box_size)
    ax.text(2.2, -2.1, r'$\bar{\mathbf{3}}$', fontsize=14, ha='center', fontweight='bold')
    
    # Equals
    ax.text(3.0, -0.4, r'$=$', fontsize=16, ha='center', va='center')
    
    # Octet (8) - mixed symmetry
    draw_young_partition(ax, [2, 1], start_x=3.8, start_y=0, box_size=box_size)
    ax.text(4.4, -2.1, r'$\mathbf{8}$ (octet)', fontsize=12, ha='center')
    
    # Plus
    ax.text(5.6, -0.4, r'$\oplus$', fontsize=16, ha='center', va='center')
    
    # Singlet (1) - empty
    circle = plt.Circle((6.8, -0.4), 0.3, fill=False, edgecolor='black', linewidth=2)
    ax.add_patch(circle)
    ax.text(6.8, -1.3, r'$\mathbf{1}$ (singlet)', fontsize=12, ha='center')
    
    ax.set_xlim(-0.3, 8.0)
    ax.set_ylim(-2.5, 0.5)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(r'$\mathbf{3} \otimes \bar{\mathbf{3}} = \mathbf{8} \oplus \mathbf{1}$', 
                fontsize=14, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'young_3x3bar_product.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def draw_su3_representations():
    """Draw all basic SU(3) representations."""
    setup_style()
    fig, axes = plt.subplots(2, 3, figsize=(11, 6))
    axes = axes.flatten()
    
    box_size = 0.7
    
    diagrams = [
        ([1], r'$\mathbf{3}$', 'Fundamental\n(covariant)'),
        ([1, 1], r'$\bar{\mathbf{3}}$', 'Anti-fundamental\n(contravariant)'),
        ([2], r'$\mathbf{6}$', 'Symmetric'),
        ([2, 1], r'$\mathbf{8}$', 'Octet\n(adjoint)'),
        ([3], r'$\mathbf{10}$', 'Decuplet\n(totally symmetric)'),
        ([], r'$\mathbf{1}$', 'Singlet\n(trivial)'),
    ]
    
    for ax, (partition, label, desc) in zip(axes, diagrams):
        if partition:  # Non-empty diagrams
            draw_young_partition(ax, partition, start_x=-0.35*max(partition), 
                               start_y=0.35*len(partition), box_size=box_size)
            ax.set_xlim(-0.8, 0.8)
            ax.set_ylim(-1.0, 0.8)
        else:  # Singlet - draw circle
            circle = plt.Circle((0, 0), 0.25, fill=False, edgecolor='black', linewidth=2)
            ax.add_patch(circle)
            ax.set_xlim(-0.8, 0.8)
            ax.set_ylim(-1.0, 0.8)
        
        ax.set_aspect('equal')
        ax.axis('off')
        ax.text(0, -0.7, f'{label}\n{desc}', fontsize=11, ha='center', va='top')
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'young_su3_all.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating Young diagrams for SU(3)...")
    
    draw_tensor_product_3x3()
    draw_tensor_product_3x3bar()
    draw_su3_representations()
    
    print("\nAll Young diagrams generated!")
