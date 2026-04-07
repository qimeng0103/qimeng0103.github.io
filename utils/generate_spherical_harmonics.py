#!/usr/bin/env python3
"""
Generate spherical harmonics visualization figures.
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style

OUTPUT_DIR = 'docs/images/angular-momentum'


def spherical_harmonic_Ylm(l, m, theta, phi):
    """Compute spherical harmonic Y_l^m(theta, phi)."""
    from scipy.special import sph_harm_y
    return sph_harm_y(l, m, theta, phi)


def plot_spherical_harmonic_3d(l, m, filename, title=None):
    """Create 3D polar plot of |Y_l^m|^2."""
    setup_style()
    
    theta = np.linspace(0, np.pi, 100)
    phi = np.linspace(0, 2*np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    
    # Calculate spherical harmonic
    from scipy.special import sph_harm_y
    Y = sph_harm_y(l, m, theta, phi)
    r = np.abs(Y)**2
    
    # Convert to Cartesian
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot surface
    surf = ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8, 
                          linewidth=0, antialiased=True)
    
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    if title:
        ax.set_title(title, fontsize=14, pad=10)
    else:
        ax.set_title(f'$|Y_{{{l}}}^{{{m}}}|^2$', fontsize=14, pad=10)
    
    # Set equal aspect ratio
    max_range = np.array([x.max()-x.min(), y.max()-y.min(), z.max()-z.min()]).max() / 2.0
    mid_x = (x.max()+x.min()) * 0.5
    mid_y = (y.max()+y.min()) * 0.5
    mid_z = (z.max()+z.min()) * 0.5
    ax.set_xlim(mid_x - max_range, mid_x + max_range)
    ax.set_ylim(mid_y - max_range, mid_y + max_range)
    ax.set_zlim(mid_z - max_range, mid_z + max_range)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def plot_spherical_harmonic_2d(l, m, filename, title=None):
    """Create 2D polar plot of |Y_l^m|^2."""
    setup_style()
    
    theta = np.linspace(0, 2*np.pi, 200)
    
    from scipy.special import sph_harm_y
    # For 2D plot, we fix phi=0 and plot in x-z plane
    # |Y_l^m(theta, phi=0)|^2 as function of theta
    phi = 0
    Y_vals = []
    for t in theta:
        Y = sph_harm_y(l, m, t, phi)
        Y_vals.append(np.abs(Y)**2)
    Y_vals = np.array(Y_vals)
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection='polar'))
    
    # Fill and outline (axes drawn by matplotlib will be hidden by fill)
    ax.fill_between(theta, 0, Y_vals, alpha=0.3)
    ax.plot(theta, Y_vals, linewidth=2, label=f'$|Y_{{{l}}}^{{{m}}}|^2$')
    
    # Only show outer circle frame, no axis lines
    ax.set_rticks([])
    ax.set_thetagrids([])
    ax.spines['polar'].set_visible(True)
    ax.spines['polar'].set_linewidth(1)
    ax.spines['polar'].set_edgecolor('gray')
    
    if title:
        ax.set_title(title, fontsize=14, pad=20)
    else:
        ax.set_title(f'$|Y_{{{l}}}^{{{m}}}|^2$ (xz-plane)', fontsize=14, pad=20)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


def plot_all_spherical_harmonics():
    """Generate comparison figure for s, p, d orbitals using Cartesian coords."""
    setup_style()
    
    fig, axes = plt.subplots(2, 3, figsize=(14, 9))
    axes = axes.flatten()
    
    # All plotted as |Y_lm|^2 (probability density)
    orbitals = [
        (0, 0, r's ($|Y_0^0|^2$)'),
        (1, 0, r'p$_z$ ($|Y_1^0|^2$)'),
        (1, 1, r'p$_{\pm 1}$ ($|Y_1^1|^2$)'),
        (2, 0, r'd$_{z^2}$ ($|Y_2^0|^2$)'),
        (2, 1, r'd$_{xz}$ ($|Y_2^1|^2$)'),
        (2, 2, r'd$_{x^2-y^2}$ ($|Y_2^2|^2$)'),
    ]
    
    from scipy.special import sph_harm_y
    
    for idx, (l, m, label) in enumerate(orbitals):
        ax = axes[idx]
        theta = np.linspace(0, 2*np.pi, 400)
        phi = 0  # Fix phi=0 for 2D projection
        
        Y_vals = []
        for t in theta:
            Y = sph_harm_y(l, m, t, phi)
            Y_vals.append(np.abs(Y)**2)
        Y_vals = np.array(Y_vals)
        
        # Convert to Cartesian coordinates
        x = Y_vals * np.sin(theta)  # x = r * sin(theta) in spherical
        y = Y_vals * np.cos(theta)  # z = r * cos(theta) in spherical
        
        # Fill and outline
        ax.fill(x, y, alpha=0.3, color='blue')
        ax.plot(x, y, linewidth=2, color='darkblue')
        
        # Draw outer circle reference
        max_r = Y_vals.max()
        circle_theta = np.linspace(0, 2*np.pi, 100)
        ax.plot(max_r * np.sin(circle_theta), max_r * np.cos(circle_theta), 
                'k-', linewidth=0.8, alpha=0.5)
        
        # Add direction labels
        max_r = Y_vals.max()
        offset = max_r * 0.12
        ax.text(0, max_r + offset, 'z', ha='center', va='center', fontsize=11, fontweight='bold')
        ax.text(0, -max_r - offset, '-z', ha='center', va='center', fontsize=11, fontweight='bold')
        ax.text(max_r + offset, 0, 'x', ha='center', va='center', fontsize=11, fontweight='bold')
        ax.text(-max_r - offset, 0, '-x', ha='center', va='center', fontsize=11, fontweight='bold')
        
        # Set equal aspect and remove axes
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_xlim(-max_r*1.25, max_r*1.25)
        ax.set_ylim(-max_r*1.25, max_r*1.25)
        ax.set_title(label, fontsize=12, pad=10)
    
    plt.tight_layout()
    filepath = os.path.join(OUTPUT_DIR, 'spherical_harmonics_overview.png')
    fig.savefig(filepath, dpi=200, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"Saved: {filepath}")
    plt.close()
    return filepath


if __name__ == '__main__':
    print("Generating spherical harmonics figures...")
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # scipy is required
    from scipy.special import sph_harm_y
    
    # Generate 2D polar plots
    plot_spherical_harmonic_2d(0, 0, 'Y00_2d.png', 's-orbital ($l=0$)')
    plot_spherical_harmonic_2d(1, 0, 'Y10_2d.png', 'p$_z$ ($l=1, m=0$)')
    plot_spherical_harmonic_2d(2, 0, 'Y20_2d.png', 'd$_{z^2}$ ($l=2, m=0$)')
    plot_spherical_harmonic_2d(3, 0, 'Y30_2d.png', 'f$_{z^3}$ ($l=3, m=0$)')
    
    # Generate overview
    plot_all_spherical_harmonics()
    
    print("\nAll spherical harmonics figures generated successfully!")
