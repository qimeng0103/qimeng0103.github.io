#!/usr/bin/env python3
"""
Generate SU(3) weight diagrams with improved layout and positioning.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style, COLORS

OUTPUT_DIR = 'docs/images/angular-momentum'


def draw_su3_axes(ax, title='', xlabel='$I_3$', ylabel='$Y$'):
    """Draw standard SU(3) weight diagram axes."""
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, pad=15)
    ax.axhline(y=0, color='gray', linewidth=0.8, linestyle='-', alpha=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.8, linestyle='-', alpha=0.5)
    ax.set_aspect('equal')


def draw_fundamental_triplet_v2():
    """Draw improved fundamental representation (3) - quark triplet."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 6))
    
    # Quark positions in (I3, Y) space
    quarks = {
        'u': (0.5, 1/3),
        'd': (-0.5, 1/3),
        's': (0, -2/3),
    }
    colors = {'u': '#d62728', 'd': '#1f77b4', 's': '#2ca02c'}  # Red, blue, green
    
    # Draw connecting triangle outline first (behind points)
    triangle = plt.Polygon([(0.5, 1/3), (-0.5, 1/3), (0, -2/3)], 
                          fill=False, edgecolor='black', linewidth=1.5, alpha=0.3)
    ax.add_patch(triangle)
    
    # Draw horizontal line between u and d
    ax.plot([-0.4, 0.4], [1/3, 1/3], 'k-', linewidth=1.5, alpha=0.3)
    
    # Draw ladder arrows with better positioning
    # I+/- : horizontal
    ax.annotate('', xy=(0.35, 1/3), xytext=(0.15, 1/3),
               arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))
    ax.annotate('', xy=(-0.35, 1/3), xytext=(-0.15, 1/3),
               arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))
    ax.text(0, 1/3 + 0.12, r'$I_\pm$', fontsize=11, ha='center', color='purple')
    
    # V ladder: d to s
    ax.annotate('', xy=(-0.35, 0.0), xytext=(-0.15, -0.5),
               arrowprops=dict(arrowstyle='->', color='orange', lw=1.5))
    ax.text(-0.45, -0.25, r'$V_\pm$', fontsize=11, ha='center', color='orange',
           bbox=dict(boxstyle='round,pad=0.15', facecolor='white', alpha=0.9, edgecolor='none'))
    
    # U ladder: u to s
    ax.annotate('', xy=(0.35, 0.0), xytext=(0.15, -0.5),
               arrowprops=dict(arrowstyle='->', color='teal', lw=1.5))
    ax.text(0.45, -0.25, r'$U_\pm$', fontsize=11, ha='center', color='teal',
           bbox=dict(boxstyle='round,pad=0.15', facecolor='white', alpha=0.9, edgecolor='none'))
    
    # Draw quark positions
    for name, (i3, y) in quarks.items():
        ax.scatter(i3, y, s=800, c=colors[name], marker='o', 
                  edgecolors='black', linewidths=2, zorder=5)
        ax.annotate(f'${name}$', (i3, y), fontsize=16, ha='center', va='center',
                   color='white', fontweight='bold', zorder=6)
        # Add quantum numbers below
        if name == 'u':
            label = r'$(+\frac{1}{2}, +\frac{1}{3})$'
        elif name == 'd':
            label = r'$(-\frac{1}{2}, +\frac{1}{3})$'
        else:
            label = r'$(0, -\frac{2}{3})$'
        ax.annotate(label, (i3, y-0.35), fontsize=10, ha='center', va='top')
    
    draw_su3_axes(ax, r'Fundamental Representation $\mathbf{3}$ (Quarks)')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 0.9)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_fundamental_triplet.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def draw_octet_baryons_v2():
    """Draw improved octet representation (8) - baryon octet."""
    setup_style()
    fig, ax = plt.subplots(figsize=(9, 7))
    
    # Baryon octet positions
    baryons = [
        ('p', 0.5, 1), ('n', -0.5, 1),
        (r'$\Sigma^+$', 1, 0), (r'$\Sigma^0$', 0.08, 0), (r'$\Lambda$', -0.08, 0), (r'$\Sigma^-$', -1, 0),
        (r'$\Xi^0$', 0.5, -1), (r'$\Xi^-$', -0.5, -1),
    ]
    
    # Draw hexagon outline
    hex_r = 1.15
    hex_angles = np.linspace(0, 2*np.pi, 7)
    hex_x = hex_r * np.cos(hex_angles)
    hex_y = hex_r * np.sin(hex_angles) * 0.87  # Slightly flatten for Y scaling
    ax.plot(hex_x, hex_y, 'k-', linewidth=1.2, alpha=0.3)
    
    # Draw internal connecting lines
    lines = [
        [(0.5, 1), (1, 0)], [(1, 0), (0.5, -1)], [(0.5, -1), (-0.5, -1)],
        [(-0.5, -1), (-1, 0)], [(-1, 0), (-0.5, 1)], [(-0.5, 1), (0.5, 1)],
        [(0.5, 1), (-0.5, -1)], [(-0.5, 1), (0.5, -1)], [(1, 0), (-1, 0)],
    ]
    for line in lines:
        x_coords = [p[0] for p in line]
        y_coords = [p[1] for p in line]
        ax.plot(x_coords, y_coords, 'k-', linewidth=1, alpha=0.25)
    
    # Plot each baryon
    for name, i3, y in baryons:
        is_double = name in [r'$\Sigma^0$', r'$\Lambda$']
        size = 550 if is_double else 450
        ax.scatter(i3, y, s=size, c='#2ca02c', marker='o', 
                  edgecolors='black', linewidths=1.5, zorder=5)
        fs = 12 if len(name) > 3 else 13
        ax.annotate(name, (i3, y), fontsize=fs, ha='center', va='center', 
                   color='white', fontweight='bold', zorder=6)
    
    # Add note about center
    ax.text(1.1, -1.3, r'Center: $\Sigma^0$, $\Lambda$ (2 states)',
           fontsize=10, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    draw_su3_axes(ax, r'Octet Representation $\mathbf{8}$ (Spin-$\frac{1}{2}$ Baryons)')
    ax.set_xlim(-1.4, 1.4)
    ax.set_ylim(-1.5, 1.3)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_octet_baryons.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def draw_decuplet_baryons_v2():
    """Draw improved decuplet representation (10) - baryon decuplet."""
    setup_style()
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Decuplet positions
    decuplet = [
        (r'$\Delta^{++}$', 3/2, 1), (r'$\Delta^{+}$', 1/2, 1),
        (r'$\Delta^{0}$', -1/2, 1), (r'$\Delta^{-}$', -3/2, 1),
        (r'$\Sigma^{*+}$', 1, 0), (r'$\Sigma^{*0}$', 0, 0), (r'$\Sigma^{*-}$', -1, 0),
        (r'$\Xi^{*0}$', 1/2, -1), (r'$\Xi^{*-}$', -1/2, -1),
        (r'$\Omega^{-}$', 0, -2),
    ]
    
    # Draw triangular grid lines
    for y, x_range in [(1, [-3/2, 3/2]), (0, [-1, 1]), (-1, [-1/2, 1/2])]:
        ax.plot(x_range, [y, y], 'k-', linewidth=1, alpha=0.3)
    
    # Diagonal lines
    diagonal_lines = [
        [(-3/2, 1), (0, -2)], [(-1/2, 1), (1, -1)], [(1/2, 1), (1, 0)],
        [(3/2, 1), (0, -2)], [(1/2, 1), (-1, -1)], [(-1/2, 1), (-1, 0)],
    ]
    for line in diagonal_lines:
        x_coords = [p[0] for p in line]
        y_coords = [p[1] for p in line]
        ax.plot(x_coords, y_coords, 'k-', linewidth=1, alpha=0.3)
    
    # Plot each baryon
    for name, i3, y in decuplet:
        is_omega = r'\Omega' in name
        size = 650 if is_omega else 500
        ax.scatter(i3, y, s=size, c='#d62728', marker='o',
                  edgecolors='black', linewidths=1.5, zorder=5)
        fs = 11 if len(name) > 5 else 12
        ax.annotate(name, (i3, y), fontsize=fs, ha='center', va='center',
                   color='white', fontweight='bold', zorder=6)
    
    draw_su3_axes(ax, r'Decuplet Representation $\mathbf{10}$ (Spin-$\frac{3}{2}$ Baryons)')
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.3, 1.4)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_decuplet_baryons.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


if __name__ == '__main__':
    print("Generating improved SU(3) weight diagrams...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    draw_fundamental_triplet_v2()
    draw_octet_baryons_v2()
    draw_decuplet_baryons_v2()
    
    print("\nAll improved SU(3) weight diagrams generated!")
