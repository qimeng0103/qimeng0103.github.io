#!/usr/bin/env python3
"""
Generate SU(3) Fundamental Representation (Quark Triplet)
"""

import matplotlib.pyplot as plt
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style

OUTPUT_DIR = 'docs/images/angular-momentum'


def draw_fundamental_triplet():
    """Draw quark triplet weight diagram."""
    setup_style()
    
    # Figure with frame
    fig, ax = plt.subplots(figsize=(7, 6.5))
    
    # Positions
    u_pos = np.array([0.5, 1/3])
    d_pos = np.array([-0.5, 1/3])
    s_pos = np.array([0, -2/3])
    
    # Colors
    u_color = '#E74C3C'
    d_color = '#3498DB'
    s_color = '#2ECC71'
    
    # Triangle outline
    triangle = plt.Polygon([u_pos, d_pos, s_pos], 
                          fill=False, 
                          edgecolor='#7F8C8D', 
                          linewidth=2, 
                          alpha=0.7,
                          zorder=1)
    ax.add_patch(triangle)
    
    # ===== LADDER OPERATORS =====
    
    # I+/- : horizontal arrows - label below like original
    arrow_y = 1/3 - 0.08
    ax.annotate('', xy=(0.20, arrow_y), xytext=(0.05, arrow_y),
               arrowprops=dict(arrowstyle='->', color='#8E44AD', lw=1.8), zorder=2)
    ax.annotate('', xy=(-0.20, arrow_y), xytext=(-0.05, arrow_y),
               arrowprops=dict(arrowstyle='->', color='#8E44AD', lw=1.8), zorder=2)
    ax.text(0, arrow_y - 0.10, r'$I_\pm$', fontsize=12, ha='center', color='#8E44AD')
    
    # V+/- : left side - arrows with label below them (like I+/- style)
    # Position between d and s, label below the arrows
    vx = -0.25
    vy_top = 0.05
    vy_bot = -0.40
    # Arrow down-right
    ax.annotate('', xy=(vx + 0.12, vy_bot), xytext=(vx - 0.05, vy_top),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=1.8), zorder=2)
    # Arrow up-left
    ax.annotate('', xy=(vx - 0.05, vy_top), xytext=(vx + 0.12, vy_bot),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=1.8), zorder=2)
    # Label below
    ax.text(vx, vy_bot - 0.10, r'$V_\pm$', fontsize=12, ha='center', color='#E67E22')
    
    # U+/- : right side - arrows with label below them (like I+/- style)
    ux = 0.25
    uy_top = 0.05
    uy_bot = -0.40
    # Arrow down-left
    ax.annotate('', xy=(ux - 0.12, uy_bot), xytext=(ux + 0.05, uy_top),
               arrowprops=dict(arrowstyle='->', color='#16A085', lw=1.8), zorder=2)
    # Arrow up-right
    ax.annotate('', xy=(ux + 0.05, uy_top), xytext=(ux - 0.12, uy_bot),
               arrowprops=dict(arrowstyle='->', color='#16A085', lw=1.8), zorder=2)
    # Label below
    ax.text(ux, uy_bot - 0.10, r'$U_\pm$', fontsize=12, ha='center', color='#16A085')
    
    # ===== QUARK CIRCLES =====
    r = 0.18
    
    # u
    u_circle = plt.Circle(u_pos, r, facecolor=u_color, 
                         edgecolor='black', linewidth=2, zorder=10)
    ax.add_patch(u_circle)
    ax.text(u_pos[0], u_pos[1], r'$u$', fontsize=18, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    
    # d
    d_circle = plt.Circle(d_pos, r, facecolor=d_color, 
                         edgecolor='black', linewidth=2, zorder=10)
    ax.add_patch(d_circle)
    ax.text(d_pos[0], d_pos[1], r'$d$', fontsize=18, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    
    # s
    s_circle = plt.Circle(s_pos, r, facecolor=s_color, 
                         edgecolor='black', linewidth=2, zorder=10)
    ax.add_patch(s_circle)
    ax.text(s_pos[0], s_pos[1], r'$s$', fontsize=18, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    
    # ===== AXES =====
    ax.set_xlabel(r'$I_3$', fontsize=13)
    ax.set_ylabel(r'$Y$', fontsize=13)
    
    ax.axhline(y=0, color='#BDC3C7', linewidth=1, alpha=0.8)
    ax.axvline(x=0, color='#BDC3C7', linewidth=1, alpha=0.8)
    
    ax.set_xticks([-0.5, 0, 0.5])
    ax.set_xticklabels([r'$-\frac{1}{2}$', r'$0$', r'$+\frac{1}{2}$'], fontsize=10)
    ax.set_yticks([-2/3, 0, 1/3])
    ax.set_yticklabels([r'$-\frac{2}{3}$', r'$0$', r'$+\frac{1}{3}$'], fontsize=10)
    
    ax.set_aspect('equal')
    ax.set_xlim(-0.85, 0.85)
    ax.set_ylim(-1.05, 0.65)
    
    # Title - no bold
    ax.set_title(r'Fundamental Representation $\mathbf{3}$ (Quarks)', 
                fontsize=14, pad=10)
    
    # Full frame - all spines visible
    for spine in ax.spines.values():
        spine.set_visible(True)
        spine.set_color('#95A5A6')
    
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
