#!/usr/bin/env python3
"""
Generate SU(3) weight diagrams with proper construction arrows and alignment.
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
    """Draw fundamental representation (3) showing construction from highest weight."""
    setup_style()
    fig, ax = plt.subplots(figsize=(7, 6))
    
    # Exact quark positions
    u_pos = (0.5, 1/3)
    d_pos = (-0.5, 1/3)
    s_pos = (0, -2/3)
    
    colors = {'u': '#d62728', 'd': '#1f77b4', 's': '#2ca02c'}
    
    # Draw triangle outline
    triangle_x = [u_pos[0], d_pos[0], s_pos[0], u_pos[0]]
    triangle_y = [u_pos[1], d_pos[1], s_pos[1], u_pos[1]]
    ax.plot(triangle_x, triangle_y, 'k-', linewidth=1.5, alpha=0.3, zorder=1)
    
    # Draw construction arrows showing the building process
    # Arrow from u to d (I_- lowering)
    ax.annotate('', xy=(d_pos[0] + 0.12, d_pos[1]), xytext=(u_pos[0] - 0.12, u_pos[1]),
               arrowprops=dict(arrowstyle='->', color='purple', lw=2.5),
               zorder=2)
    ax.text(0, 1/3 + 0.15, r'$I_-$', fontsize=13, ha='center', color='purple', fontweight='bold')
    
    # Arrow from u to s (V_- lowering) - precisely aligned along the triangle edge
    # Direction vector from u to s: (0 - 0.5, -2/3 - 1/3) = (-0.5, -1)
    # Normalize and scale
    ax.annotate('', xy=(s_pos[0] + 0.08, s_pos[1] + 0.10), xytext=(u_pos[0] - 0.04, u_pos[1] - 0.08),
               arrowprops=dict(arrowstyle='->', color='darkorange', lw=2.5),
               zorder=2)
    ax.text(0.42, -0.12, r'$V_-$', fontsize=12, ha='center', color='darkorange', fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.15', facecolor='white', alpha=0.9, edgecolor='none'))
    
    # Draw quark circles
    for name, pos in [('u', u_pos), ('d', d_pos), ('s', s_pos)]:
        circle = plt.Circle(pos, 0.12, facecolor=colors[name], edgecolor='black', 
                          linewidth=2, zorder=5)
        ax.add_patch(circle)
        ax.annotate(f'${name}$', pos, fontsize=16, ha='center', va='center',
                   color='white', fontweight='bold', zorder=6)
    
    # Quantum number labels
    ax.text(0.5, 1/3 - 0.22, r'$(\frac{1}{2}, \frac{1}{3})$', fontsize=10, ha='center')
    ax.text(-0.5, 1/3 - 0.22, r'$(-\frac{1}{2}, \frac{1}{3})$', fontsize=10, ha='center')
    ax.text(0, -2/3 - 0.22, r'$(0, -\frac{2}{3})$', fontsize=10, ha='center')
    
    # Label highest weight
    ax.annotate('Highest weight\n(annihilated by $I_+, V_+$)', 
               xy=u_pos, xytext=(0.9, 0.7),
               fontsize=10, ha='center',
               arrowprops=dict(arrowstyle='->', color='gray', lw=1),
               bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))
    
    # Axes
    ax.set_xlabel(r'$I_3$ (Isospin)', fontsize=12)
    ax.set_ylabel(r'$Y$ (Hypercharge)', fontsize=12)
    ax.axhline(y=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.axvline(x=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.set_aspect('equal')
    ax.set_xlim(-1.0, 1.3)
    ax.set_ylim(-1.1, 0.9)
    ax.set_title(r'Fundamental $\mathbf{3}$: Construction from Highest Weight', fontsize=13, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_fundamental_triplet.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()


def draw_octet_baryons():
    """Draw octet representation (8) with proper alignment and construction."""
    setup_style()
    fig, ax = plt.subplots(figsize=(9, 7))
    
    # Define exact positions for hexagon alignment
    # Top edge: p, n at Y=1
    # Middle: Sigma+, Sigma0/Lambda, Sigma- at Y=0  
    # Bottom: Xi0, Xi- at Y=-1
    
    p_pos = (0.5, 1.0)
    n_pos = (-0.5, 1.0)
    sigma_plus = (1.0, 0.0)
    sigma_minus = (-1.0, 0.0)
    xi0_pos = (0.5, -1.0)
    xi_minus = (-0.5, -1.0)
    
    # Double state at origin - offset slightly
    sigma_0 = (0.08, 0.08)
    lambda_0 = (-0.08, -0.08)
    
    baryons = [
        (r'$p$', p_pos, 'darkgreen'),
        (r'$n$', n_pos, 'darkgreen'),
        (r'$\Sigma^+$', sigma_plus, 'darkblue'),
        (r'$\Sigma^0$', sigma_0, 'darkblue'),
        (r'$\Lambda$', lambda_0, 'purple'),
        (r'$\Sigma^-$', sigma_minus, 'darkblue'),
        (r'$\Xi^0$', xi0_pos, 'darkred'),
        (r'$\Xi^-$', xi_minus, 'darkred'),
    ]
    
    # Draw hexagon outline with proper alignment
    hex_vertices = [p_pos, sigma_plus, xi0_pos, xi_minus, sigma_minus, n_pos, p_pos]
    hex_x = [v[0] for v in hex_vertices]
    hex_y = [v[1] for v in hex_vertices]
    ax.plot(hex_x, hex_y, 'k-', linewidth=2, alpha=0.5, zorder=1)
    
    # Draw internal lines (aligned)
    internal_lines = [
        (p_pos, xi_minus),   # diagonal
        (n_pos, xi0_pos),    # diagonal
        (sigma_plus, sigma_minus),  # horizontal through center
    ]
    for start, end in internal_lines:
        ax.plot([start[0], end[0]], [start[1], end[1]], 'k--', linewidth=1, alpha=0.3, zorder=1)
    
    # Vertical lines
    ax.plot([p_pos[0], xi0_pos[0]], [p_pos[1], xi0_pos[1]], 'k--', linewidth=1, alpha=0.3, zorder=1)
    ax.plot([n_pos[0], xi_minus[0]], [n_pos[1], xi_minus[1]], 'k--', linewidth=1, alpha=0.3, zorder=1)
    
    # Draw baryons
    for name, pos, color in baryons:
        is_center = name in [r'$\Sigma^0$', r'$\Lambda$']
        size = 700 if is_center else 550
        ax.scatter(pos[0], pos[1], s=size, c=color, marker='o', 
                  edgecolors='black', linewidths=2, zorder=5)
        
        text_color = 'white'
        fs = 12 if len(name) > 3 else 13
        ax.annotate(name, pos, fontsize=fs, ha='center', va='center',
                   color=text_color, fontweight='bold', zorder=6)
    
    # Add legend for center states
    ax.text(1.35, -0.3, r'Center ($I_3=Y=0$):' + '\n' + 
           r'$\Sigma^0$: isospin triplet' + '\n' + 
           r'$\Lambda$: isospin singlet',
           fontsize=10, ha='left', va='center',
           bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))
    
    # Axes
    ax.set_xlabel(r'$I_3$ (Isospin)', fontsize=12)
    ax.set_ylabel(r'$Y$ (Hypercharge)', fontsize=12)
    ax.axhline(y=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.axvline(x=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.set_aspect('equal')
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.4, 1.3)
    ax.set_title(r'Adjoint $\mathbf{8}$ (Baryon Octet)', fontsize=13, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_octet_baryons.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()


def draw_root_diagram():
    """Draw SU(3) root diagram."""
    setup_style()
    fig, ax = plt.subplots(figsize=(8, 7))
    
    sqrt3 = np.sqrt(3)
    
    # Root vectors - normalized for nice visualization
    scale = 1.2
    roots = {
        r'$I_+$': (scale, 0),
        r'$I_-$': (-scale, 0),
        r'$V_+$': (scale/2, scale*sqrt3/2),
        r'$V_-$': (-scale/2, -scale*sqrt3/2),
        r'$U_+$': (-scale/2, scale*sqrt3/2),
        r'$U_-$': (scale/2, -scale*sqrt3/2),
    }
    
    # Draw hexagon outline
    hex_r = scale * 1.3
    hex_angles = np.linspace(0, 2*np.pi, 7)
    hex_x = hex_r * np.cos(hex_angles)
    hex_y = hex_r * np.sin(hex_angles)
    ax.plot(hex_x, hex_y, 'k-', linewidth=1.5, alpha=0.4)
    
    # Draw root vectors as arrows from origin
    for label, (x, y) in roots.items():
        color = 'darkblue' if '+' in label else 'darkred'
        ax.annotate('', xy=(x*1.1, y*1.1), xytext=(0, 0),
                   arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
        
        offset_factor = 1.4
        ax.text(x*offset_factor, y*offset_factor, label, 
               fontsize=13, ha='center', va='center',
               color=color, fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                        edgecolor='none', alpha=0.8))
    
    # Mark origin
    ax.plot(0, 0, 'ko', markersize=10)
    ax.text(0, -0.35, 'Cartan\n$(I_3, Y)$', ha='center', va='top', fontsize=10,
           bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow', alpha=0.8))
    
    # Axes
    ax.set_xlabel(r'$\Delta I_3$', fontsize=12)
    ax.set_ylabel(r'$\Delta Y$', fontsize=12)
    ax.axhline(y=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.axvline(x=0, color='gray', linewidth=0.8, alpha=0.4)
    ax.set_aspect('equal')
    ax.set_xlim(-2.0, 2.0)
    ax.set_ylim(-1.8, 1.8)
    ax.set_title(r'SU(3) Root Diagram (6 Root Vectors)', fontsize=13, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_root_diagram.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()


if __name__ == '__main__':
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print("Generating SU(3) weight diagrams...")
    
    draw_root_diagram()
    draw_fundamental_triplet()
    draw_octet_baryons()
    
    print("\nAll SU(3) diagrams generated successfully!")
