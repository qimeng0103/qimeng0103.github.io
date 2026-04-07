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
    
    # I+/- : horizontal arrows between u and d
    arrow_y = 1/3
    # Right arrow (I+)
    ax.annotate('', xy=(0.28, arrow_y), xytext=(0.08, arrow_y),
               arrowprops=dict(arrowstyle='->', color='#8E44AD', lw=1.8), zorder=2)
    # Left arrow (I-)
    ax.annotate('', xy=(-0.28, arrow_y), xytext=(-0.08, arrow_y),
               arrowprops=dict(arrowstyle='->', color='#8E44AD', lw=1.8), zorder=2)
    # Label in middle
    ax.text(0, arrow_y + 0.12, r'$I_\pm$', fontsize=12, ha='center', 
           va='bottom', color='#8E44AD')
    
    # V+/- : diagonal arrows between d and s (left side)
    # Direction: from d (-0.5, 1/3) to s (0, -2/3)
    # Vector: (0.5, -1)
    # Unit vector normalized
    vx, vy = 0.5, -1
    v_len = np.sqrt(vx**2 + vy**2)
    ux, uy = vx/v_len, vy/v_len
    
    # Start from d, go toward s (but stop before reaching)
    d_start = np.array([-0.5 + 0.22*ux, 1/3 + 0.22*uy])
    s_end = np.array([0 - 0.22*ux, -2/3 - 0.22*uy])
    mid = (d_start + s_end) / 2
    
    # Arrow from d toward s
    ax.annotate('', xy=(mid[0] - 0.08*ux, mid[1] - 0.08*uy), 
               xytext=(d_start[0], d_start[1]),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=1.8), zorder=2)
    # Arrow from s toward d
    ax.annotate('', xy=(mid[0] + 0.08*ux, mid[1] + 0.08*uy), 
               xytext=(s_end[0], s_end[1]),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=1.8), zorder=2)
    # Label in middle
    # Offset label slightly to the left of the line
    ax.text(mid[0] - 0.12, mid[1], r'$V_\pm$', fontsize=12, ha='center', 
           va='center', color='#E67E22',
           bbox=dict(boxstyle='round,pad=0.15', facecolor='white', 
                    edgecolor='none', alpha=0.9))
    
    # U+/- : diagonal arrows between u and s (right side)
    # Direction: from u (0.5, 1/3) to s (0, -2/3)
    # Vector: (-0.5, -1)
    vx, vy = -0.5, -1
    v_len = np.sqrt(vx**2 + vy**2)
    ux, uy = vx/v_len, vy/v_len
    
    # Start from u, go toward s
    u_start = np.array([0.5 + 0.22*ux, 1/3 + 0.22*uy])
    s_end = np.array([0 - 0.22*ux, -2/3 - 0.22*uy])
    mid = (u_start + s_end) / 2
    
    # Arrow from u toward s
    ax.annotate('', xy=(mid[0] - 0.08*ux, mid[1] - 0.08*uy), 
               xytext=(u_start[0], u_start[1]),
               arrowprops=dict(arrowstyle='->', color='#16A085', lw=1.8), zorder=2)
    # Arrow from s toward u
    ax.annotate('', xy=(mid[0] + 0.08*ux, mid[1] + 0.08*uy), 
               xytext=(s_end[0], s_end[1]),
               arrowprops=dict(arrowstyle='->', color='#16A085', lw=1.8), zorder=2)
    # Label in middle
    # Offset label slightly to the right of the line
    ax.text(mid[0] + 0.12, mid[1], r'$U_\pm$', fontsize=12, ha='center', 
           va='center', color='#16A085',
           bbox=dict(boxstyle='round,pad=0.15', facecolor='white', 
                    edgecolor='none', alpha=0.9))
    
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
    
    # Full frame
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
