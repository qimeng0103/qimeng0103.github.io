#!/usr/bin/env python3
"""
Generate SU(3) weight diagrams with precise alignment.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style, COLORS

OUTPUT_DIR = 'docs/images/angular-momentum'


def draw_fundamental_triplet():
    """Draw fundamental representation (3) - quark triplet."""
    setup_style()
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    
    # Exact quark positions
    u_pos = (0.5, 1/3)
    d_pos = (-0.5, 1/3)
    s_pos = (0, -2/3)
    
    colors = {'u': '#d62728', 'd': '#1f77b4', 's': '#2ca02c'}
    
    # Draw lines FIRST (behind circles)
    # Triangle outline
    triangle_x = [u_pos[0], d_pos[0], s_pos[0], u_pos[0]]
    triangle_y = [u_pos[1], d_pos[1], s_pos[1], u_pos[1]]
    ax.plot(triangle_x, triangle_y, 'k-', linewidth=1.5, alpha=0.3, zorder=1)
    
    # Ladder operator arrows - carefully positioned
    # I+/- arrows between u and d
    ax.annotate('', xy=(0.25, 1/3), xytext=(0.05, 1/3),
               arrowprops=dict(arrowstyle='->', color='purple', lw=1.5), zorder=2)
    ax.annotate('', xy=(-0.25, 1/3), xytext=(-0.05, 1/3),
               arrowprops=dict(arrowstyle='->', color='purple', lw=1.5), zorder=2)
    ax.text(0, 1/3 + 0.15, r'$I_\pm$', fontsize=12, ha='center', color='purple', fontweight='bold')
    
    # V+/- arrows from d to s
    ax.annotate('', xy=(-0.25, -0.15), xytext=(-0.08, 0.15),
               arrowprops=dict(arrowstyle='->', color='darkorange', lw=1.5), zorder=2)
    ax.text(-0.4, -0.05, r'$V_\pm$', fontsize=11, ha='center', color='darkorange',
           bbox=dict(boxstyle='round,pad=0.1', facecolor='white', alpha=0.9, edgecolor='none'))
    
    # U+/- arrows from u to s  
    ax.annotate('', xy=(0.25, -0.15), xytext=(0.08, 0.15),
               arrowprops=dict(arrowstyle='->', color='teal', lw=1.5), zorder=2)
    ax.text(0.4, -0.05, r'$U_\pm$', fontsize=11, ha='center', color='teal',
           bbox=dict(boxstyle='round,pad=0.1', facecolor='white', alpha=0.9, edgecolor='none'))
    
    # Draw quark circles ON TOP
    for name, pos in [('u', u_pos), ('d', d_pos), ('s', s_pos)]:
        circle = plt.Circle(pos, 0.18, facecolor=colors[name], edgecolor='black', 
                          linewidth=2, zorder=5)
        ax.add_patch(circle)
        ax.annotate(f'${name}$', pos, fontsize=18, ha='center', va='center',
                   color='white', fontweight='bold', zorder=6)
    
    # Quantum number labels
    ax.text(0.5, 1/3 - 0.28, r'$(+\frac{1}{2}, +\frac{1}{3})$', fontsize=10, ha='center')
    ax.text(-0.5, 1/3 - 0.28, r'$(-\frac{1}{2}, +\frac{1}{3})$', fontsize=10, ha='center')
    ax.text(0, -2/3 - 0.28, r'$(0, -\frac{2}{3})$', fontsize=10, ha='center')
    
    # Axes
    ax.set_xlabel(r'$I_3$ (Isospin)', fontsize=12)
    ax.set_ylabel(r'$Y$ (Hypercharge)', fontsize=12)
    ax.axhline(y=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.axvline(x=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.set_aspect('equal')
    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.2, 0.9)
    ax.set_title(r'Fundamental Representation $\mathbf{3}$ (Quarks)', fontsize=14, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_fundamental_triplet.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()


def draw_octet_baryons():
    """Draw octet representation (8) - baryon octet."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8.5, 6.5))
    
    # Exact positions
    baryons = [
        ('p', 0.5, 1), ('n', -0.5, 1),
        (r'$\Sigma^+$', 1, 0), (r'$\Sigma^0$', 0.1, 0.05), (r'$\Lambda$', -0.1, -0.05), (r'$\Sigma^-$', -1, 0),
        (r'$\Xi^0$', 0.5, -1), (r'$\Xi^-$', -0.5, -1),
    ]
    
    # Define lines connecting the points - using EXACT point coordinates
    connections = [
        # Outer hexagon
        [(-0.5, 1), (0.5, 1)], [(0.5, 1), (1, 0)], [(1, 0), (0.5, -1)],
        [(0.5, -1), (-0.5, -1)], [(-0.5, -1), (-1, 0)], [(-1, 0), (-0.5, 1)],
        # Cross lines
        [(-0.5, 1), (0.5, -1)], [(0.5, 1), (-0.5, -1)],
        # Horizontal through center
        [(-1, 0), (1, 0)],
    ]
    
    # Draw lines FIRST
    for start, end in connections:
        ax.plot([start[0], end[0]], [start[1], end[1]], 'k-', 
               linewidth=1.2, alpha=0.25, zorder=1)
    
    # Draw points ON TOP
    for name, i3, y in baryons:
        is_center = name in [r'$\Sigma^0$', r'$\Lambda$']
        if is_center:
            # Two overlapping circles for center
            offset = 0.06
            for dx, label in [(offset, r'$\Sigma^0$'), (-offset, r'$\Lambda$')]:
                circle = plt.Circle((i3 + dx, y), 0.22, facecolor='#2ca02c', 
                                  edgecolor='black', linewidth=2, zorder=5)
                ax.add_patch(circle)
                ax.text(i3 + dx, y, label, fontsize=10, ha='center', va='center',
                       color='white', fontweight='bold', zorder=6)
        else:
            circle = plt.Circle((i3, y), 0.22, facecolor='#2ca02c', 
                              edgecolor='black', linewidth=2, zorder=5)
            ax.add_patch(circle)
            fs = 12 if len(name) > 3 else 13
            ax.text(i3, y, name, fontsize=fs, ha='center', va='center',
                   color='white', fontweight='bold', zorder=6)
    
    # Legend
    ax.text(1.2, -1.2, r'Center contains 2 states: $\Sigma^0$, $\Lambda$',
           fontsize=10, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    # Axes
    ax.set_xlabel(r'$I_3$ (Isospin)', fontsize=12)
    ax.set_ylabel(r'$Y$ (Hypercharge)', fontsize=12)
    ax.axhline(y=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.axvline(x=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.set_aspect('equal')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.4, 1.3)
    ax.set_title(r'Octet Representation $\mathbf{8}$ (Spin-$\frac{1}{2}$ Baryons)', fontsize=14, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_octet_baryons.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()


def draw_decuplet_baryons():
    """Draw decuplet representation (10) - baryon decuplet."""
    setup_style()
    fig, ax = plt.subplots(figsize=(9.5, 6.5))
    
    # Exact decuplet positions
    decuplet = [
        (r'$\Delta^{++}$', 3/2, 1), (r'$\Delta^{+}$', 1/2, 1),
        (r'$\Delta^{0}$', -1/2, 1), (r'$\Delta^{-}$', -3/2, 1),
        (r'$\Sigma^{*+}$', 1, 0), (r'$\Sigma^{*0}$', 0, 0), (r'$\Sigma^{*-}$', -1, 0),
        (r'$\Xi^{*0}$', 1/2, -1), (r'$\Xi^{*-}$', -1/2, -1),
        (r'$\Omega^{-}$', 0, -2),
    ]
    
    # Draw grid lines FIRST
    # Horizontal lines
    for y, x_start, x_end in [(1, -3/2, 3/2), (0, -1, 1), (-1, -1/2, 1/2)]:
        ax.plot([x_start, x_end], [y, y], 'k-', linewidth=1, alpha=0.3, zorder=1)
    
    # Diagonal lines (left and right slanting)
    diagonals = [
        # Left slanting (down-right)
        [(-3/2, 1), (0, -2)], [(-1/2, 1), (1, -1)], [(1/2, 1), (1, 0)],
        # Right slanting (down-left)  
        [(3/2, 1), (0, -2)], [(1/2, 1), (-1, -1)], [(-1/2, 1), (-1, 0)],
    ]
    for start, end in diagonals:
        ax.plot([start[0], end[0]], [start[1], end[1]], 'k-', 
               linewidth=1, alpha=0.3, zorder=1)
    
    # Draw points ON TOP
    for name, i3, y in decuplet:
        is_omega = r'\Omega' in name
        radius = 0.24 if is_omega else 0.2
        color = '#8B0000' if is_omega else '#d62728'  # Darker red for omega
        
        circle = plt.Circle((i3, y), radius, facecolor=color, 
                          edgecolor='black', linewidth=2, zorder=5)
        ax.add_patch(circle)
        
        fs = 10 if len(name) > 6 else 11
        ax.text(i3, y, name, fontsize=fs, ha='center', va='center',
               color='white', fontweight='bold', zorder=6)
    
    # Axes
    ax.set_xlabel(r'$I_3$ (Isospin)', fontsize=12)
    ax.set_ylabel(r'$Y$ (Hypercharge)', fontsize=12)
    ax.axhline(y=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.axvline(x=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.set_aspect('equal')
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-2.3, 1.4)
    ax.set_title(r'Decuplet Representation $\mathbf{10}$ (Spin-$\frac{3}{2}$ Baryons)', fontsize=14, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_decuplet_baryons.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()


if __name__ == '__main__':
    print("Generating SU(3) weight diagrams v3...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    draw_fundamental_triplet()
    draw_octet_baryons()
    draw_decuplet_baryons()
    
    print("\nAll diagrams generated!")
