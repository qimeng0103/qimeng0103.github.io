#!/usr/bin/env python3
"""
Generate SU(3) weight diagrams (root diagrams and representation weight diagrams).
Fixed version with proper labels and no overlaps.
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
    ax.set_title(title, fontsize=14, pad=15)
    
    # Draw axes through origin
    ax.axhline(y=0, color='gray', linewidth=0.8, linestyle='-', alpha=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.8, linestyle='-', alpha=0.5)
    
    # Set equal aspect ratio
    ax.set_aspect('equal')


def draw_root_diagram():
    """Draw SU(3) root diagram (adjoint representation)."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(9, 8))
    
    # Root vectors - using exact SU(3) root values
    # I roots: horizontal
    # U roots: 60 degrees up-left
    # V roots: 60 degrees up-right
    sqrt3 = np.sqrt(3)
    roots = {
        r'$I_+$': (1, 0),
        r'$I_-$': (-1, 0),
        r'$V_+$': (0.5, sqrt3/2),
        r'$V_-$': (-0.5, -sqrt3/2),
        r'$U_+$': (-0.5, sqrt3/2),
        r'$U_-$': (0.5, -sqrt3/2),
    }
    
    # Draw hexagon outline first (closed)
    hex_r = 1.3
    hex_angles = np.linspace(0, 2*np.pi, 7)  # 7 points to close the loop
    hex_x = hex_r * np.cos(hex_angles)
    hex_y = hex_r * np.sin(hex_angles)
    ax.plot(hex_x, hex_y, 'k-', linewidth=1.5, alpha=0.4)
    
    # Draw root vectors as arrows from origin
    for label, (x, y) in roots.items():
        color = 'darkblue' if '+' in label else 'darkred'
        # Draw arrow
        ax.annotate('', xy=(x*1.15, y*1.15), xytext=(0, 0),
                   arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
        # Label at tip with better positioning
        offset_factor = 1.45
        ax.text(x*offset_factor, y*offset_factor, label, 
               fontsize=14, ha='center', va='center',
               color=color, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                        edgecolor='none', alpha=0.8))
    
    # Mark origin (Cartan subalgebra)
    ax.plot(0, 0, 'ko', markersize=12)
    ax.text(0, -0.35, 'Cartan\n$(I_3, Y)$', ha='center', va='top', fontsize=11,
           bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))
    
    draw_su3_axes(ax, 'SU(3) Root Diagram (Adjoint Representation $\mathbf{8}$)', 
                  xlabel=r'$I_3$ (Isospin projection)', 
                  ylabel=r'$Y$ (Hypercharge)')
    
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.0, 2.0)
    
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
    
    fig, ax = plt.subplots(figsize=(8, 7))
    
    # Quark positions in (I3, Y) space - using exact values
    quarks = {
        'u': (0.5, 1/3),
        'd': (-0.5, 1/3),
        's': (0, -2/3),
    }
    
    colors = {'u': 'red', 'd': 'blue', 's': 'green'}
    
    # Draw quark positions with larger markers
    for name, (i3, y) in quarks.items():
        ax.plot(i3, y, 'o', markersize=22, color=colors[name], 
               markeredgecolor='black', markeredgewidth=2)
        # Add quark name
        ax.annotate(f'${name}$', (i3, y), fontsize=18, ha='center', va='center',
                   color='white', fontweight='bold')
        # Add quantum numbers with proper fractions
        if name == 'u':
            label = r'$(+\frac{1}{2}, +\frac{1}{3})$'
        elif name == 'd':
            label = r'$(-\frac{1}{2}, +\frac{1}{3})$'
        else:  # s
            label = r'$(0, -\frac{2}{3})$'
        ax.annotate(label, (i3, y-0.3), fontsize=11, ha='center', va='top')
    
    # Draw connecting lines showing ladder operations
    # I+/- : horizontal between u and d
    ax.plot([-0.35, 0.35], [1/3, 1/3], 'k-', linewidth=1.5, alpha=0.4)
    ax.annotate('', xy=(0.3, 1/3), xytext=(0.1, 1/3),
               arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax.annotate('', xy=(-0.3, 1/3), xytext=(-0.1, 1/3),
               arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax.text(0, 1/3 + 0.15, r'$I_\pm$', fontsize=12, ha='center', color='purple')
    
    # V ladder: d to s
    mid_x = -0.25
    mid_y = -1/6
    ax.annotate('', xy=(-0.4, 0.15), xytext=(-0.1, -0.5),
               arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax.text(-0.45, -0.2, r'$V_\pm$', fontsize=12, ha='center', color='purple',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
    
    # U ladder: u to s
    ax.annotate('', xy=(0.4, 0.15), xytext=(0.1, -0.5),
               arrowprops=dict(arrowstyle='->', color='purple', lw=2))
    ax.text(0.45, -0.2, r'$U_\pm$', fontsize=12, ha='center', color='purple',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8))
    
    draw_su3_axes(ax, r'Fundamental Representation $\mathbf{3}$ (Quarks)')
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.0)
    
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
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Baryon octet positions - using standard values
    baryons = [
        # Top row (Y=1)
        ('p', 0.5, 1),
        ('n', -0.5, 1),
        # Middle row (Y=0)
        (r'$\Sigma^+$', 1, 0),
        (r'$\Sigma^0$', 0, 0.08),  # Slightly offset up
        (r'$\Lambda$', 0, -0.08),  # Slightly offset down
        (r'$\Sigma^-$', -1, 0),
        # Bottom row (Y=-1)
        (r'$\Xi^0$', 0.5, -1),
        (r'$\Xi^-$', -0.5, -1),
    ]
    
    # Draw hexagon outline
    hex_r = 1.15
    hex_angles = np.linspace(0, 2*np.pi, 7)
    hex_x = hex_r * np.cos(hex_angles)
    hex_y = hex_r * np.sin(hex_angles)
    ax.plot(hex_x, hex_y, 'k-', linewidth=1, alpha=0.3)
    
    # Draw internal lines first
    lines = [
        [(0.5, 1), (1, 0)],
        [(1, 0), (0.5, -1)],
        [(0.5, -1), (-0.5, -1)],
        [(-0.5, -1), (-1, 0)],
        [(-1, 0), (-0.5, 1)],
        [(-0.5, 1), (0.5, 1)],
        [(0.5, 1), (-0.5, -1)],
        [(-0.5, 1), (0.5, -1)],
        [(1, 0), (-1, 0)],
    ]
    
    for line in lines:
        x_coords = [p[0] for p in line]
        y_coords = [p[1] for p in line]
        ax.plot(x_coords, y_coords, 'k-', linewidth=1, alpha=0.3)
    
    # Plot each baryon with larger markers
    for name, i3, y in baryons:
        is_double = name in [r'$\Sigma^0$', r'$\Lambda$']
        size = 600 if is_double else 500
        ax.scatter(i3, y, s=size, c='darkgreen', marker='o', 
                  edgecolors='black', linewidths=2, zorder=5)
        
        # Adjust fontsize based on label length
        fs = 13 if len(name) > 3 else 14
        color = 'white'
        ax.annotate(name, (i3, y), fontsize=fs, 
                   ha='center', va='center', color=color, fontweight='bold',
                   zorder=6)
    
    # Add note about double state
    ax.text(1.3, -1.4, r'Center: $\Sigma^0$, $\Lambda$ (2 states)',
           fontsize=11, ha='right', va='bottom',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
    
    draw_su3_axes(ax, r'Octet Representation $\mathbf{8}$ (Spin-1/2 Baryons)')
    ax.set_xlim(-1.5, 1.6)
    ax.set_ylim(-1.6, 1.4)
    
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
    
    fig, ax = plt.subplots(figsize=(11, 8))
    
    # Decuplet positions
    decuplet = [
        # Y=1 (Delta quartet)
        (r'$\Delta^{++}$', 3/2, 1),
        (r'$\Delta^{+}$', 1/2, 1),
        (r'$\Delta^{0}$', -1/2, 1),
        (r'$\Delta^{-}$', -3/2, 1),
        # Y=0 (Sigma* triplet)
        (r'$\Sigma^{*+}$', 1, 0),
        (r'$\Sigma^{*0}$', 0, 0),
        (r'$\Sigma^{*-}$', -1, 0),
        # Y=-1 (Xi* doublet)
        (r'$\Xi^{*0}$', 1/2, -1),
        (r'$\Xi^{*-}$', -1/2, -1),
        # Y=-2 (Omega singlet)
        (r'$\Omega^{-}$', 0, -2),
    ]
    
    # Draw triangular lattice lines
    # Horizontal lines
    for y, x_range in [(1, [-3/2, 3/2]), (0, [-1, 1]), (-1, [-1/2, 1/2])]:
        ax.plot(x_range, [y, y], 'k-', linewidth=1, alpha=0.3)
    
    # Diagonal lines
    diagonal_lines = [
        [(-3/2, 1), (0, -2)],
        [(-1/2, 1), (1, -1)],
        [(1/2, 1), (1, 0)],
        [(3/2, 1), (0, -2)],
        [(1/2, 1), (-1, -1)],
        [(-1/2, 1), (-1, 0)],
    ]
    
    for line in diagonal_lines:
        x_coords = [p[0] for p in line]
        y_coords = [p[1] for p in line]
        ax.plot(x_coords, y_coords, 'k-', linewidth=1, alpha=0.3)
    
    # Plot each baryon with larger markers and clear labels
    for name, i3, y in decuplet:
        is_omega = r'\Omega' in name
        size = 700 if is_omega else 500
        ax.scatter(i3, y, s=size, c='darkred', marker='o',
                  edgecolors='black', linewidths=2, zorder=5)
        
        fs = 13 if len(name) > 5 else 14
        ax.annotate(name, (i3, y), fontsize=fs,
                   ha='center', va='center', color='white', fontweight='bold',
                   zorder=6)
    
    draw_su3_axes(ax, r'Decuplet Representation $\mathbf{10}$ (Spin-3/2 Baryons)')
    ax.set_xlim(-2.2, 2.2)
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
    
    fig, axes = plt.subplots(2, 2, figsize=(13, 12))
    axes = axes.flatten()
    
    # 1. Triplet (3)
    ax = axes[0]
    quarks = {'u': (0.5, 1/3), 'd': (-0.5, 1/3), 's': (0, -2/3)}
    colors = {'u': 'red', 'd': 'blue', 's': 'green'}
    for name, (i3, y) in quarks.items():
        ax.scatter(i3, y, s=400, c=colors[name], marker='o',
                  edgecolors='black', linewidths=2)
        ax.annotate(f'${name}$', (i3, y), fontsize=13, ha='center', va='center',
                   color='white', fontweight='bold')
    ax.set_title(r'$\mathbf{3}$ (Quarks)', fontsize=14, pad=10)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-0.9, 0.7)
    ax.axhline(y=0, color='gray', linewidth=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5)
    ax.set_aspect('equal')
    
    # 2. Antitriplet (3bar)
    ax = axes[1]
    antiquarks = {r'$\bar{u}$': (-0.5, -1/3), r'$\bar{d}$': (0.5, -1/3), r'$\bar{s}$': (0, 2/3)}
    for name, (i3, y) in antiquarks.items():
        ax.scatter(i3, y, s=400, c='lightcoral', marker='s',
                  edgecolors='black', linewidths=2)
        ax.annotate(name, (i3, y), fontsize=11, ha='center', va='center',
                   color='black', fontweight='bold')
    ax.set_title(r'$\bar{\mathbf{3}}$ (Antiquarks)', fontsize=14, pad=10)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-0.7, 0.9)
    ax.axhline(y=0, color='gray', linewidth=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5)
    ax.set_aspect('equal')
    
    # 3. Octet (8)
    ax = axes[2]
    octet = [('p', 0.5, 1), ('n', -0.5, 1), (r'$\Sigma^+$', 1, 0), 
             (r'$\Sigma^0$', 0, 0.06), (r'$\Lambda$', 0, -0.06),
             (r'$\Sigma^-$', -1, 0), (r'$\Xi^0$', 0.5, -1), (r'$\Xi^-$', -0.5, -1)]
    for name, i3, y in octet:
        is_double = name in [r'$\Sigma^0$', r'$\Lambda$']
        size = 350 if is_double else 300
        ax.scatter(i3, y, s=size, c='darkgreen', marker='o',
                  edgecolors='black', linewidths=1.5)
        fs = 9 if len(name) > 3 else 10
        ax.annotate(name, (i3, y), fontsize=fs, ha='center', va='center',
                   color='white', fontweight='bold')
    ax.set_title(r'$\mathbf{8}$ (Baryon Octet)', fontsize=14, pad=10)
    ax.set_xlim(-1.3, 1.3)
    ax.set_ylim(-1.3, 1.2)
    ax.axhline(y=0, color='gray', linewidth=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5)
    ax.set_aspect('equal')
    
    # 4. Decuplet (10)
    ax = axes[3]
    decuplet = [
        (r'$\Delta^{++}$', 3/2, 1), (r'$\Delta^{+}$', 1/2, 1),
        (r'$\Delta^{0}$', -1/2, 1), (r'$\Delta^{-}$', -3/2, 1),
        (r'$\Sigma^{*+}$', 1, 0), (r'$\Sigma^{*0}$', 0, 0), (r'$\Sigma^{*-}$', -1, 0),
        (r'$\Xi^{*0}$', 1/2, -1), (r'$\Xi^{*-}$', -1/2, -1),
        (r'$\Omega^{-}$', 0, -2),
    ]
    for name, i3, y in decuplet:
        is_omega = r'\Omega' in name
        size = 400 if is_omega else 300
        ax.scatter(i3, y, s=size, c='darkred', marker='o',
                  edgecolors='black', linewidths=1.5)
        fs = 8 if len(name) > 5 else 9
        ax.annotate(name, (i3, y), fontsize=fs, ha='center', va='center',
                   color='white', fontweight='bold')
    ax.set_title(r'$\mathbf{10}$ (Baryon Decuplet)', fontsize=14, pad=10)
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2.3, 1.3)
    ax.axhline(y=0, color='gray', linewidth=0.5)
    ax.axvline(x=0, color='gray', linewidth=0.5)
    ax.set_aspect('equal')
    
    # Add common labels
    for ax in axes:
        ax.set_xlabel(r'$I_3$', fontsize=10)
        ax.set_ylabel(r'$Y$', fontsize=10)
    
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
