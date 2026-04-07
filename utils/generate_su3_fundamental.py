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
    
    fig, ax = plt.subplots(figsize=(7.5, 6.5))
    
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
    
    # I+ : d -> u (rightward)
    ax.annotate('', xy=(0.35, 1/3), xytext=(-0.15, 1/3),
               arrowprops=dict(arrowstyle='->', color='#8E44AD', lw=1.8), zorder=2)
    ax.text(0.10, 1/3 + 0.12, r'$I_+$', fontsize=12, ha='center', 
           va='bottom', color='#8E44AD')
    
    # I- : u -> d (leftward)
    ax.annotate('', xy=(-0.35, 1/3), xytext=(0.15, 1/3),
               arrowprops=dict(arrowstyle='->', color='#8E44AD', lw=1.8), zorder=2)
    ax.text(-0.10, 1/3 + 0.12, r'$I_-$', fontsize=12, ha='center', 
           va='bottom', color='#8E44AD')
    
    # V+ : s -> d (raises I3 and Y, upward-left)
    # V- : d -> s (lowers I3 and Y, downward-right)
    dx, dy = -0.5, 1  # s to d direction
    vlen = np.sqrt(dx**2 + dy**2)
    ux, uy = dx/vlen, dy/vlen
    
    s_edge_v = s_pos + 0.22 * np.array([ux, uy])
    d_edge_v = d_pos - 0.22 * np.array([ux, uy])
    
    # V+ label position (upper part of the line)
    label_v_plus = s_pos + 0.55 * np.array([ux, uy])
    # V- label position (lower part of the line)
    label_v_minus = s_pos + 0.35 * np.array([ux, uy])
    
    # V+ arrow: s -> d
    ax.annotate('', xy=(d_edge_v[0], d_edge_v[1]), 
               xytext=(s_edge_v[0], s_edge_v[1]),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=1.8), zorder=2)
    ax.text(label_v_plus[0] - 0.06, label_v_plus[1], r'$V_+$', fontsize=12, ha='center', 
           va='center', color='#E67E22')
    
    # V- arrow: d -> s
    ax.annotate('', xy=(s_edge_v[0], s_edge_v[1]), 
               xytext=(d_edge_v[0], d_edge_v[1]),
               arrowprops=dict(arrowstyle='->', color='#E67E22', lw=1.8, ls='--'), zorder=2)
    ax.text(label_v_minus[0] - 0.06, label_v_minus[1] - 0.12, r'$V_-$', fontsize=12, ha='center', 
           va='center', color='#E67E22')
    
    # U+ : s -> u (raises I3 and Y, upward-right)
    # U- : u -> s (lowers I3 and Y, downward-left)
    dx, dy = 0.5, 1  # s to u direction
    vlen = np.sqrt(dx**2 + dy**2)
    ux, uy = dx/vlen, dy/vlen
    
    s_edge_u = s_pos + 0.22 * np.array([ux, uy])
    u_edge_u = u_pos - 0.22 * np.array([ux, uy])
    
    # U+ label position (upper part of the line)
    label_u_plus = s_pos + 0.55 * np.array([ux, uy])
    # U- label position (lower part of the line)
    label_u_minus = s_pos + 0.35 * np.array([ux, uy])
    
    # U+ arrow: s -> u
    ax.annotate('', xy=(u_edge_u[0], u_edge_u[1]), 
               xytext=(s_edge_u[0], s_edge_u[1]),
               arrowprops=dict(arrowstyle='->', color='#16A085', lw=1.8), zorder=2)
    ax.text(label_u_plus[0] + 0.06, label_u_plus[1], r'$U_+$', fontsize=12, ha='center', 
           va='center', color='#16A085')
    
    # U- arrow: u -> s
    ax.annotate('', xy=(s_edge_u[0], s_edge_u[1]), 
               xytext=(u_edge_u[0], u_edge_u[1]),
               arrowprops=dict(arrowstyle='->', color='#16A085', lw=1.8, ls='--'), zorder=2)
    ax.text(label_u_minus[0] + 0.06, label_u_minus[1] - 0.12, r'$U_-$', fontsize=12, ha='center', 
           va='center', color='#16A085')
    
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
    
    ax.set_title(r'Fundamental Representation $\mathbf{3}$ (Quarks)', 
                fontsize=14, pad=10)
    
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
