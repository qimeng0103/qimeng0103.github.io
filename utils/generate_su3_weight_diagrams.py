#!/usr/bin/env python3
"""
Generate SU(3) weight diagrams (root diagrams and representation weight diagrams).
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os
import sys

# Add utils to path for import
sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style, COLORS

# Output directory
OUTPUT_DIR = 'docs/images/angular-momentum'


def draw_su3_axes(ax, title='', xlabel='$I_3$ (Isospin)', ylabel='$Y$ (Hypercharge)'):
    """Draw standard SU(3) weight diagram axes."""
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, pad=10)
    
    # Draw axes through origin
    ax.axhline(y=0, color='gray', linewidth=0.8, linestyle='-')
    ax.axvline(x=0, color='gray', linewidth=0.8, linestyle='-')
    
    # Set equal aspect ratio
    ax.set_aspect('equal')


def draw_root_diagram():
    """Draw SU(3) root diagram (adjoint representation)."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(8, 7))
    
    # Root vectors (6 non-zero roots)
    roots = {
        r'$I_+$': (1, 0),
        r'$I_-$': (-1, 0),
        r'$U_+$': (-0.5, np.sqrt(3)/2),
        r'$U_-$': (0.5, -np.sqrt(3)/2),
        r'$V_+$': (0.5, np.sqrt(3)/2),
        r'$V_-$': (-0.5, -np.sqrt(3)/2),
    }
    
    # Draw root vectors as arrows from origin
    for label, (x, y) in roots.items():
        color = 'darkblue' if '+' in label else 'darkred'
        ax.annotate('', xy=(x*1.3, y*1.3), xytext=(0, 0),
                   arrowprops=dict(arrowstyle='->', color=color, lw=2))
        # Label at tip
        offset_x = 0.15 if x >= 0 else -0.15
        offset_y = 0.15 if y >= 0 else -0.15
        ax.text(x*1.4 + offset_x, y*1.4 + offset_y, label, 
               fontsize=12, ha='center', va='center',
               color=color, fontweight='bold')
    
    # Mark origin (Cartan subalgebra)
    ax.plot(0, 0, 'ko', markersize=15, label='Cartan generators\n$I_3$, $Y$')
    ax.text(0, -0.3, 'Cartan\n(2 generators)', ha='center', va='top', fontsize=10)
    
    # Draw hexagon outline
    hex_r = 1.3
    hex_angles = np.linspace(0, 2*np.pi, 7)[:-1]
    hex_x = hex_r * np.cos(hex_angles)
    hex_y = hex_r * np.sin(hex_angles)
    ax.plot(hex_x, hex_y, 'k--', linewidth=1, alpha=0.3)
    
    draw_su3_axes(ax, 'SU(3) Root Diagram (Adjoint Representation)', 
                  xlabel=r'$I_3$ (Isospin projection)', 
                  ylabel=r'$Y$ (Hypercharge / $\sqrt{3}$)')
    
    ax.set_xlim(-2, 2)
    ax.set_ylim(-1.8, 1.8)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_root_diagram.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def draw_fundamental_triplet():
    """Draw the fundamental representation (3) - quark triplet."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(7, 6))
    
    # Quark positions in (I3, Y) space
    quarks = {
        'u': (0.5, 1/3),
        'd': (-0.5, 1/3),
        's': (0, -2/3),
    }
    
    colors = {'u': 'red', 'd': 'blue', 's': 'green'}
    
    # Draw quark positions
    for name, (i3, y) in quarks.items():
        ax.plot(i3, y, 'o', markersize=20, color=colors[name], 
               markeredgecolor='black', markeredgewidth=2)
        # Add quark name
        ax.annotate(f'${name}$', (i3, y), fontsize=16, ha='center', va='center',
                   color='white', fontweight='bold')
        # Add quantum numbers
        ax.annotate(f'(${i3:g}$, ${y:g}$)', 
                   (i3, y-0.25), fontsize=10, ha='center', va='top')
    
    # Draw connecting lines (showing ladder operations)
    # I+/- : horizontal
    ax.annotate('', xy=(0.4, 1/3), xytext=(-0.4, 1/3),
               arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
    ax.text(0, 0.5, r'$I_\pm$', fontsize=12, ha='center', color='gray')
    
    # V ladder
    ax.annotate('', xy=(0.35, 0.1), xytext=(-0.1, -0.5),
               arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
    ax.text(0.35, -0.25, r'$V_\pm$', fontsize=12, ha='left', color='gray')
    
    # U ladder  
    ax.annotate('', xy=(-0.35, 0.1), xytext=(0.1, -0.5),
               arrowprops=dict(arrowstyle='<->', color='gray', lw=1.5))
    ax.text(-0.35, -0.25, r'$U_\pm$', fontsize=12, ha='right', color='gray')
    
    draw_su3_axes(ax, r'Fundamental Representation $\mathbf{3}$ (Quarks)')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.0)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_fundamental_triplet.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def draw_octet_baryons():
    """Draw the octet representation (8) - baryon octet."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(9, 7))
    
    # Baryon octet positions
    baryons = {
        # Top row (Y=1)
        'p': (0.5, 1),
        'n': (-0.5, 1),
        # Middle row (Y=0)
        r'$\Sigma^+$': (1, 0),
        r'$\Sigma^0$': (0, 0),
        r'$\Lambda$': (0, 0),  # Same position as Sigma0
        r'$\Sigma^-$': (-1, 0),
        # Bottom row (Y=-1)
        r'$\Xi^0$': (0.5, -1),
        r'$\Xi^-$': (-0.5, -1),
    }
    
    # Plot each baryon
    for name, (i3, y) in baryons.items():
        # Special handling for double state at origin
        if name in [r'$\Sigma^0$', r'$\Lambda$']:
            offset = 0.08 if name == r'$\Sigma^0$' else -0.08
            ax.plot(i3, y + offset, 'o', markersize=18, 
                   color='darkgreen', markeredgecolor='black', markeredgewidth=2)
            ax.annotate(name, (i3, y + offset), fontsize=11, 
                       ha='center', va='center', color='white', fontweight='bold')
        else:
            ax.plot(i3, y, 'o', markersize=18,
                   color='darkblue', markeredgecolor='black', markeredgewidth=2)
            ax.annotate(name, (i3, y), fontsize=12,
                       ha='center', va='center', color='white', fontweight='bold')
    
    # Draw connecting lines (the hexagon pattern)
    lines = [
        # Top triangle
        [(0.5, 1), (1, 0)],
        [(1, 0), (0.5, -1)],
        [(0.5, -1), (-0.5, -1)],
        [(-0.5, -1), (-1, 0)],
        [(-1, 0), (-0.5, 1)],
        [(-0.5, 1), (0.5, 1)],
        # Inner lines
        [(0.5, 1), (-0.5, -1)],
        [(-0.5, 1), (0.5, -1)],
        [(1, 0), (-1, 0)],
    ]
    
    for line in lines:
        x_coords = [p[0] for p in line]
        y_coords = [p[1] for p in line]
        ax.plot(x_coords, y_coords, 'k-', linewidth=1, alpha=0.4)
    
    draw_su3_axes(ax, r'Octet Representation $\mathbf{8}$ (Spin-1/2 Baryons)')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.3)
    
    # Add note about double state
    ax.text(1.3, -1.3, r'Center has 2 states: $\Sigma^0$, $\Lambda$',
           fontsize=10, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_octet_baryons.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def draw_decuplet_baryons():
    """Draw the decuplet representation (10) - baryon decuplet."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # Decuplet positions
    decuplet = {
        # Y=1 (Delta quartet)
        r'$\Delta^{++}$': (3/2, 1),
        r'$\Delta^{+}$': (1/2, 1),
        r'$\Delta^{0}$': (-1/2, 1),
        r'$\Delta^{-}$': (-3/2, 1),
        # Y=0 (Sigma* triplet)
        r'$\Sigma^{*+}$': (1, 0),
        r'$\Sigma^{*0}$': (0, 0),
        r'$\Sigma^{*-}$': (-1, 0),
        # Y=-1 (Xi* doublet)
        r'$\Xi^{*0}$': (1/2, -1),
        r'$\Xi^{*-}$': (-1/2, -1),
        # Y=-2 (Omega singlet)
        r'$\Omega^{-}$': (0, -2),
    }
    
    # Plot each baryon
    for name, (i3, y) in decuplet.items():
        size = 22 if r'\Omega' in name else 18
        ax.plot(i3, y, 'o', markersize=size,
               color='darkred', markeredgecolor='black', markeredgewidth=2)
        # Use white text on dark background
        ax.annotate(name, (i3, y), fontsize=11 if len(name) > 5 else 12,
                   ha='center', va='center', color='white', fontweight='bold')
    
    # Draw triangular lattice lines
    # Horizontal lines
    for y in [1, 0, -1]:
        x_range = {
            1: [-3/2, 3/2],
            0: [-1, 1],
            -1: [-1/2, 1/2],
        }
        if y in x_range:
            ax.plot(x_range[y], [y, y], 'k-', linewidth=1, alpha=0.4)
    
    # Diagonal lines (slope sqrt(3))
    diagonal_lines = [
        # Down-right from top
        [(-3/2, 1), (0, -2)],
        [(-1/2, 1), (1, -1)],
        [(1/2, 1), (1, 0)],
        # Down-left from top
        [(3/2, 1), (0, -2)],
        [(1/2, 1), (-1, -1)],
        [(-1/2, 1), (-1, 0)],
    ]
    
    for line in diagonal_lines:
        x_coords = [p[0] for p in line]
        y_coords = [p[1] for p in line]
        ax.plot(x_coords, y_coords, 'k-', linewidth=1, alpha=0.4)
    
    draw_su3_axes(ax, r'Decuplet Representation $\mathbf{10}$ (Spin-3/2 Baryons)')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2.5, 1.5)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_decuplet_baryons.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def draw_all_representations_comparison():
    """Draw a comparison of all SU(3) representations side by side."""
    setup_style()
    
    fig, axes = plt.subplots(2, 2, figsize=(12, 11))
    axes = axes.flatten()
    
    # 1. Triplet (3)
    ax = axes[0]
    quarks = {'u': (0.5, 1/3), 'd': (-0.5, 1/3), 's': (0, -2/3)}
    colors = {'u': 'red', 'd': 'blue', 's': 'green'}
    for name, (i3, y) in quarks.items():
        ax.plot(i3, y, 'o', markersize=18, color=colors[name],
               markeredgecolor='black', markeredgewidth=2)
        ax.annotate(f'${name}$', (i3, y), fontsize=14, ha='center', va='center',
                   color='white', fontweight='bold')
    draw_su3_axes(ax, r'$\mathbf{3}$ (Quarks)')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 0.8)
    
    # 2. Antitriplet (3bar)
    ax = axes[1]
    antiquarks = {r'$\bar{u}$': (-0.5, -1/3), r'$\bar{d}$': (0.5, -1/3), r'$\bar{s}$': (0, 2/3)}
    for name, (i3, y) in antiquarks.items():
        ax.plot(i3, y, 's', markersize=18, color='lightcoral',
               markeredgecolor='black', markeredgewidth=2)
        ax.annotate(name, (i3, y), fontsize=12, ha='center', va='center',
                   color='black', fontweight='bold')
    draw_su3_axes(ax, r'$\bar{\mathbf{3}}$ (Antiquarks)')
    ax.set_xlim(-1, 1)
    ax.set_ylim(-0.8, 1)
    
    # 3. Octet (8) - simplified
    ax = axes[2]
    octet_simple = [
        ('p', 0.5, 1), ('n', -0.5, 1),
        (r'$\Sigma^+$', 1, 0), (r'$\Sigma^0$', 0, 0.1), (r'$\Lambda$', 0, -0.1), (r'$\Sigma^-$', -1, 0),
        (r'$\Xi^0$', 0.5, -1), (r'$\Xi^-$', -0.5, -1),
    ]
    for name, i3, y in octet_simple:
        size = 15 if name in [r'$\Sigma^0$', r'$\Lambda$'] else 16
        ax.plot(i3, y, 'o', markersize=size, color='darkgreen',
               markeredgecolor='black', markeredgewidth=1.5)
        ax.annotate(name, (i3, y), fontsize=9, ha='center', va='center',
                   color='white', fontweight='bold')
    draw_su3_axes(ax, r'$\mathbf{8}$ (Baryon Octet)')
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.3)
    
    # 4. Decuplet (10) - simplified
    ax = axes[3]
    decuplet_simple = [
        (r'$\Delta$', 3/2, 1), (r'$\Delta$', 1/2, 1), (r'$\Delta$', -1/2, 1), (r'$\Delta$', -3/2, 1),
        (r'$\Sigma^*$', 1, 0), (r'$\Sigma^*$', 0, 0), (r'$\Sigma^*$', -1, 0),
        (r'$\Xi^*$', 1/2, -1), (r'$\Xi^*$', -1/2, -1),
        (r'$\Omega$', 0, -2),
    ]
    for name, i3, y in decuplet_simple:
        size = 18 if r'\Omega' in name else 14
        ax.plot(i3, y, 'o', markersize=size, color='darkred',
               markeredgecolor='black', markeredgewidth=1.5)
        label = name if r'\Omega' in name else name + ('+' if i3 > 0 else '' if i3 == 0 else '-')
        ax.annotate(label, (i3, y), fontsize=8, ha='center', va='center',
                   color='white', fontweight='bold')
    draw_su3_axes(ax, r'$\mathbf{10}$ (Baryon Decuplet)')
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2.5, 1.5)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_all_representations.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


if __name__ == '__main__':
    print("Generating SU(3) weight diagrams...")
    
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Generate all diagrams
    draw_root_diagram()
    draw_fundamental_triplet()
    draw_octet_baryons()
    draw_decuplet_baryons()
    draw_all_representations_comparison()
    
    print("\nAll SU(3) weight diagrams generated successfully!")
