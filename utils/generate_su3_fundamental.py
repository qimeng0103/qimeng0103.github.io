#!/usr/bin/env python3
"""
Generate SU(3) Fundamental Representation (Quark Triplet) - Professional Version
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style

OUTPUT_DIR = 'docs/images/angular-momentum'


def draw_fundamental_triplet_professional():
    """Draw professional quark triplet weight diagram."""
    setup_style()
    
    # Use a clean, professional figure size
    fig, ax = plt.subplots(figsize=(8, 7))
    
    # Define exact positions
    u_pos = np.array([0.5, 1/3])
    d_pos = np.array([-0.5, 1/3])
    s_pos = np.array([0, -2/3])
    
    # Colors - using clean, distinct colors
    u_color = '#E74C3C'  # Red for u
    d_color = '#3498DB'  # Blue for d
    s_color = '#2ECC71'  # Green for s
    
    # ===== DRAW CONNECTION LINES FIRST (behind circles) =====
    # Triangle outline
    triangle = plt.Polygon([u_pos, d_pos, s_pos], 
                          fill=False, 
                          edgecolor='#7F8C8D', 
                          linewidth=2, 
                          alpha=0.6,
                          zorder=1)
    ax.add_patch(triangle)
    
    # ===== DRAW LADDER OPERATOR ARROWS =====
    arrow_style = dict(arrowstyle='->', color='#8E44AD', lw=2.5, 
                      connectionstyle='arc3,rad=0')
    
    # I+/- : horizontal arrows between u and d
    # Bidirectional arrow with labels
    arrow_y = 1/3
    # Left arrow (I-)
    ax.annotate('', xy=(-0.15, arrow_y), xytext=(0.15, arrow_y),
               arrowprops=dict(arrowstyle='->', color='#8E44AD', lw=2), zorder=2)
    # Right arrow (I+)
    ax.annotate('', xy=(0.15, arrow_y), xytext=(-0.15, arrow_y),
               arrowprops=dict(arrowstyle='->', color='#8E44AD', lw=2), zorder=2)
    # Label above
    ax.text(0, arrow_y + 0.18, r'$I_\pm$', fontsize=14, ha='center', 
           color='#8E44AD', fontweight='bold')
    
    # V+/- : arrows from d to s (left side)
    # Direction: d (-0.5, 1/3) to s (0, -2/3)
    ax.annotate('', xy=(-0.15, -0.35), xytext=(-0.35, 0.1),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=2), zorder=2)
    ax.annotate('', xy=(-0.35, 0.1), xytext=(-0.15, -0.35),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=2), zorder=2)
    ax.text(-0.55, -0.15, r'$V_\pm$', fontsize=13, ha='center', 
           color='#E67E22', fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                    edgecolor='none', alpha=0.9))
    
    # U+/- : arrows from u to s (right side)
    # Direction: u (0.5, 1/3) to s (0, -2/3)
    ax.annotate('', xy=(0.15, -0.35), xytext=(0.35, 0.1),
               arrowprops=dict(arrowstyle='->', color='#16A085', lw=2), zorder=2)
    ax.annotate('', xy=(0.35, 0.1), xytext=(0.15, -0.35),
               arrowprops=dict(arrowstyle='->', color='#16A085', lw=2), zorder=2)
    ax.text(0.55, -0.15, r'$U_\pm$', fontsize=13, ha='center', 
           color='#16A085', fontweight='bold',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='white', 
                    edgecolor='none', alpha=0.9))
    
    # ===== DRAW QUARK CIRCLES =====
    circle_radius = 0.22
    
    # u quark
    u_circle = plt.Circle(u_pos, circle_radius, facecolor=u_color, 
                         edgecolor='black', linewidth=2.5, zorder=10)
    ax.add_patch(u_circle)
    ax.text(u_pos[0], u_pos[1], r'$u$', fontsize=22, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    
    # d quark
    d_circle = plt.Circle(d_pos, circle_radius, facecolor=d_color, 
                         edgecolor='black', linewidth=2.5, zorder=10)
    ax.add_patch(d_circle)
    ax.text(d_pos[0], d_pos[1], r'$d$', fontsize=22, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    
    # s quark
    s_circle = plt.Circle(s_pos, circle_radius, facecolor=s_color, 
                         edgecolor='black', linewidth=2.5, zorder=10)
    ax.add_patch(s_circle)
    ax.text(s_pos[0], s_pos[1], r'$s$', fontsize=22, ha='center', va='center',
           color='white', fontweight='bold', zorder=11)
    
    # ===== QUANTUM NUMBER LABELS =====
    # Below each quark
    ax.text(u_pos[0], u_pos[1] - 0.38, 
           r'$\left(+,\frac{1}{2}\right)$', fontsize=12, ha='center', color='#333')
    ax.text(d_pos[0], d_pos[1] - 0.38, 
           r'$\left(-,\frac{1}{2}\right)$', fontsize=12, ha='center', color='#333')
    ax.text(s_pos[0], s_pos[1] - 0.38, 
           r'$\left(0,-\frac{2}{3}\right)$', fontsize=12, ha='center', color='#333')
    
    # Small labels for I3 and Y
    ax.text(0.95, 0.05, r'$I_3$', fontsize=11, ha='center', color='#666')
    ax.text(0.05, 0.95, r'$Y$', fontsize=11, ha='center', color='#666')
    
    # ===== AXES SETUP =====
    ax.set_xlabel(r'$I_3$ (Isospin projection)', fontsize=13, labelpad=10)
    ax.set_ylabel(r'$Y$ (Hypercharge)', fontsize=13, labelpad=10)
    
    # Light gray axes
    ax.axhline(y=0, color='#BDC3C7', linewidth=1, linestyle='-', alpha=0.7)
    ax.axvline(x=0, color='#BDC3C7', linewidth=1, linestyle='-', alpha=0.7)
    
    # Ticks
    ax.set_xticks([-0.5, 0, 0.5])
    ax.set_xticklabels([r'$-\frac{1}{2}$', r'$0$', r'$+\frac{1}{2}$'])
    ax.set_yticks([-2/3, 0, 1/3])
    ax.set_yticklabels([r'$-\frac{2}{3}$', r'$0$', r'$+\frac{1}{3}$'])
    
    # Aspect and limits
    ax.set_aspect('equal')
    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(-1.1, 0.8)
    
    # Title
    ax.set_title(r'Fundamental Representation $\mathbf{3}$ (Quarks)', 
                fontsize=15, pad=15, fontweight='bold')
    
    # Remove top and right spines for cleaner look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#BDC3C7')
    ax.spines['bottom'].set_color('#BDC3C7')
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'su3_fundamental_triplet.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight', 
               facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()


if __name__ == '__main__':
    print("Generating professional SU(3) fundamental representation...")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    draw_fundamental_triplet_professional()
    print("Done!")
