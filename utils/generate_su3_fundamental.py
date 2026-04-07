#!/usr/bin/env python3
"""
Generate SU(3) Fundamental Representation (Quark Triplet) - Clean Professional Version
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style

OUTPUT_DIR = 'docs/images/angular-momentum'


def draw_fundamental_triplet():
    """Draw clean quark triplet weight diagram."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(7.5, 6.5))
    
    # Define positions
    u_pos = np.array([0.5, 1/3])
    d_pos = np.array([-0.5, 1/3])
    s_pos = np.array([0, -2/3])
    
    # Colors
    u_color = '#E74C3C'
    d_color = '#3498DB'
    s_color = '#2ECC71'
    
    # ===== DRAW TRIANGLE OUTLINE =====
    triangle = plt.Polygon([u_pos, d_pos, s_pos], 
                          fill=False, 
                          edgecolor='#95A5A6', 
                          linewidth=2.5, 
                          alpha=0.7,
                          zorder=1)
    ax.add_patch(triangle)
    
    # ===== DRAW LADDER OPERATOR ARROWS =====
    # I+/- : horizontal between u and d - place arrows below the line
    arrow_y = 1/3 - 0.12
    # Double-headed arrow effect
    ax.annotate('', xy=(0.22, arrow_y), xytext=(0.05, arrow_y),
               arrowprops=dict(arrowstyle='->', color='#9B59B6', lw=2), zorder=2)
    ax.annotate('', xy=(-0.22, arrow_y), xytext=(-0.05, arrow_y),
               arrowprops=dict(arrowstyle='->', color='#9B59B6', lw=2), zorder=2)
    # Label below arrows
    ax.text(0, arrow_y - 0.12, r'$I_\pm$', fontsize=13, ha='center', 
           color='#9B59B6', fontweight='bold')
    
    # V+/- : left side arrows (d to s) - place outside triangle
    # Start from left of d, go down-right toward s
    ax.annotate('', xy=(-0.22, -0.25), xytext=(-0.42, 0.15),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=2), zorder=2)
    ax.annotate('', xy=(-0.42, 0.15), xytext=(-0.22, -0.25),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=2), zorder=2)
    # Label to the left
    ax.text(-0.65, -0.05, r'$V_\pm$', fontsize=12, ha='center', 
           color='#E67E22', fontweight='bold')
    
    # U+/- : right side arrows (u to s) - place outside triangle
    ax.annotate('', xy=(0.22, -0.25), xytext=(0.42, 0.15),
               arrowprops=dict(arrowstyle='->', color='#1ABC9C', lw=2), zorder=2)
    ax.annotate('', xy=(0.42, 0.15), xytext=(0.22, -0.25),
               arrowprops=dict(arrowstyle='->', color='#1ABC9C', lw=2), zorder=2)
    # Label to the right
    ax.text(0.65, -0.05, r'$U_\pm$', fontsize=12, ha='center', 
           color='#1ABC9C', fontweight='bold')
    
    # ===== DRAW QUARK CIRCLES =====
    circle_radius = 0.20
    
    # u quark
    u_circle = plt.Circle(u_pos, circle_radius, facecolor=u_color, 
                         edgecolor='black', linewidth=2.5, zorder=10)
    ax.add_patch(u_circle)
    ax.text(u_pos[0], u_pos[1] + 0.02, r'$u$', fontsize=20, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    # I3,Y label below
    ax.text(u_pos[0], u_pos[1] - 0.32, r'$+\frac{1}{2}, +\frac{1}{3}$', 
           fontsize=10, ha='center', color='#555')
    
    # d quark
    d_circle = plt.Circle(d_pos, circle_radius, facecolor=d_color, 
                         edgecolor='black', linewidth=2.5, zorder=10)
    ax.add_patch(d_circle)
    ax.text(d_pos[0], d_pos[1] + 0.02, r'$d$', fontsize=20, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    # I3,Y label below
    ax.text(d_pos[0], d_pos[1] - 0.32, r'$-\frac{1}{2}, +\frac{1}{3}$', 
           fontsize=10, ha='center', color='#555')
    
    # s quark
    s_circle = plt.Circle(s_pos, circle_radius, facecolor=s_color, 
                         edgecolor='black', linewidth=2.5, zorder=10)
    ax.add_patch(s_circle)
    ax.text(s_pos[0], s_pos[1] + 0.02, r'$s$', fontsize=20, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    # I3,Y label below
    ax.text(s_pos[0], s_pos[1] - 0.32, r'$0, -\frac{2}{3}$', 
           fontsize=10, ha='center', color='#555')
    
    # ===== AXES SETUP =====
    ax.set_xlabel(r'$I_3$', fontsize=14, labelpad=5)
    ax.set_ylabel(r'$Y$', fontsize=14, labelpad=5)
    
    # Light axes
    ax.axhline(y=0, color='#BDC3C7', linewidth=1, alpha=0.8)
    ax.axvline(x=0, color='#BDC3C7', linewidth=1, alpha=0.8)
    
    # Set ticks
    ax.set_xticks([-0.5, 0, 0.5])
    ax.set_xticklabels([r'$-\frac{1}{2}$', r'$0$', r'$+\frac{1}{2}$'], fontsize=11)
    ax.set_yticks([-2/3, 0, 1/3])
    ax.set_yticklabels([r'$-\frac{2}{3}$', r'$0$', r'$+\frac{1}{3}$'], fontsize=11)
    
    # Aspect and limits
    ax.set_aspect('equal')
    ax.set_xlim(-0.9, 0.9)
    ax.set_ylim(-1.15, 0.75)
    
    # Title
    ax.set_title(r'Fundamental Representation $\mathbf{3}$ (Quarks)', 
                fontsize=15, pad=15, fontweight='bold')
    
    # Clean spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#95A5A6')
    ax.spines['bottom'].set_color('#95A5A6')
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_fundamental_triplet.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', 
               facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()


if __name__ == '__main__':
    print("Generating SU(3) fundamental representation...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    draw_fundamental_triplet()
    print("Done!")
