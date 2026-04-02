#!/usr/bin/env python3
"""
Generate figures for the Bound States, Resonances, and Scattering article.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
import os
import sys

# Add utils to path for import
sys.path.insert(0, os.path.dirname(__file__))
from plot_style import setup_style, save_figure, COLORS

def finite_well_wavefunctions():
    """Figure 1: Finite square well potential and wave functions."""
    setup_style()
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left panel: Potential
    ax = axes[0]
    a = 1.0
    V0 = 2.0
    
    # Draw potential
    x_left = np.array([-3, -a, -a, a, a, 3])
    V_left = np.array([0, 0, -V0, -V0, 0, 0])
    ax.plot(x_left, V_left, color=COLORS['dark'], linewidth=2.5)
    
    # Energy levels
    E0 = -1.5
    E1 = -0.5
    ax.axhline(y=E0, color=COLORS['secondary'], linestyle='--', linewidth=1.5, alpha=0.8)
    ax.axhline(y=E1, color=COLORS['tertiary'], linestyle='--', linewidth=1.5, alpha=0.8)
    
    # Labels
    ax.text(1.3, E0, r'$E_0$', fontsize=11, color=COLORS['secondary'], va='center')
    ax.text(1.3, E1, r'$E_1$', fontsize=11, color=COLORS['tertiary'], va='center')
    ax.text(0, -V0-0.25, r'$-V_0$', fontsize=11, ha='center', color=COLORS['dark'])
    ax.text(-a, 0.2, r'$-a$', fontsize=11, ha='center', color=COLORS['dark'])
    ax.text(a, 0.2, r'$a$', fontsize=11, ha='center', color=COLORS['dark'])
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2.5, 0.8)
    ax.set_xlabel(r'$x/a$', fontsize=12)
    ax.set_ylabel(r'$V(x)/V_0$', fontsize=12)
    ax.set_title('Finite Square Well Potential', fontsize=13, fontweight='bold')
    ax.axhline(y=0, color=COLORS['gray'], linewidth=0.5, linestyle='-', alpha=0.5)
    
    # Right panel: Wave functions
    ax = axes[1]
    
    # Parameters for wave functions
    k0 = 0.8 * np.pi / 2  # ground state
    kappa0 = np.sqrt((np.pi/2)**2 - k0**2)
    
    k1 = np.pi  # first excited
    kappa1 = np.sqrt((np.pi/2)**2 - (np.pi/2)**2 + 0.1)  # approximate
    
    # Even parity (ground state)
    x_in = np.linspace(-a, a, 200)
    psi_in_even = 1.2 * np.cos(k0 * x_in)
    
    x_out_left = np.linspace(-3, -a, 100)
    psi_out_left = 1.2 * np.cos(k0 * a) * np.exp(kappa0 * (x_out_left + a))
    
    x_out_right = np.linspace(a, 3, 100)
    psi_out_right = 1.2 * np.cos(k0 * a) * np.exp(-kappa0 * (x_out_right - a))
    
    ax.plot(x_in, psi_in_even, color=COLORS['secondary'], linewidth=2.5, label=r'$\psi_0$ (even)')
    ax.plot(x_out_left, psi_out_left, color=COLORS['secondary'], linewidth=2.5)
    ax.plot(x_out_right, psi_out_right, color=COLORS['secondary'], linewidth=2.5)
    
    # Odd parity (first excited)
    psi_in_odd = 1.5 * np.sin(k1 * x_in)
    psi_out_left_odd = -1.5 * np.sin(k1 * a) * np.exp(kappa1 * (x_out_left + a))
    psi_out_right_odd = 1.5 * np.sin(k1 * a) * np.exp(-kappa1 * (x_out_right - a))
    
    ax.plot(x_in, psi_in_odd, color=COLORS['tertiary'], linewidth=2.5, linestyle='--', label=r'$\psi_1$ (odd)')
    ax.plot(x_out_left, psi_out_left_odd, color=COLORS['tertiary'], linewidth=2.5, linestyle='--')
    ax.plot(x_out_right, psi_out_right_odd, color=COLORS['tertiary'], linewidth=2.5, linestyle='--')
    
    # Well boundaries
    ax.axvline(x=-a, color=COLORS['gray'], linewidth=1, linestyle=':', alpha=0.7)
    ax.axvline(x=a, color=COLORS['gray'], linewidth=1, linestyle=':', alpha=0.7)
    ax.axhline(y=0, color=COLORS['dark'], linewidth=0.5, alpha=0.5)
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-2, 2)
    ax.set_xlabel(r'$x/a$', fontsize=12)
    ax.set_ylabel(r'$\psi(x)$', fontsize=12)
    ax.set_title('Bound State Wave Functions', fontsize=13, fontweight='bold')
    ax.legend(loc='upper right', frameon=True)
    
    plt.tight_layout()
    return fig

def wavefunction_matching():
    """Figure 2: Wave function matching at boundaries."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    a = 1.0
    
    # Draw well boundaries
    ax.axvline(x=-a, color=COLORS['primary'], linewidth=2, linestyle='-')
    ax.axvline(x=a, color=COLORS['primary'], linewidth=2, linestyle='-')
    ax.text(-a, 2.3, r'$-a$', fontsize=11, ha='center', color=COLORS['primary'])
    ax.text(a, 2.3, r'$a$', fontsize=11, ha='center', color=COLORS['primary'])
    
    # Regions
    ax.text(0, 2.3, 'Well', fontsize=11, ha='center', color=COLORS['dark'])
    ax.text(-2, 2.3, 'Outside', fontsize=11, ha='center', color=COLORS['gray'])
    ax.text(2, 2.3, 'Outside', fontsize=11, ha='center', color=COLORS['gray'])
    
    # Even parity wave function
    k = 0.8 * np.pi / 2
    kappa = 1.0
    
    x_in = np.linspace(-a, a, 200)
    psi_even = 1.5 * np.cos(k * x_in)
    
    x_left = np.linspace(-3, -a, 100)
    psi_left = 1.5 * np.cos(k * a) * np.exp(kappa * (x_left + a))
    
    x_right = np.linspace(a, 3, 100)
    psi_right = 1.5 * np.cos(k * a) * np.exp(-kappa * (x_right - a))
    
    ax.plot(x_in, psi_even, color=COLORS['secondary'], linewidth=2.5, label=r'Even: $\psi(-x) = \psi(x)$')
    ax.plot(x_left, psi_left, color=COLORS['secondary'], linewidth=2.5)
    ax.plot(x_right, psi_right, color=COLORS['secondary'], linewidth=2.5)
    
    # Odd parity wave function (shifted up)
    x_in_odd = np.linspace(-a, a, 200)
    psi_in_odd = 1.2 * np.sin(np.pi * x_in_odd) + 3
    
    x_left_odd = np.linspace(-3, -a, 100)
    psi_left_odd = -1.2 * np.sin(np.pi * a) * np.exp(kappa * (x_left_odd + a)) + 3
    
    x_right_odd = np.linspace(a, 3, 100)
    psi_right_odd = 1.2 * np.sin(np.pi * a) * np.exp(-kappa * (x_right_odd - a)) + 3
    
    ax.plot(x_in_odd, psi_in_odd, color=COLORS['tertiary'], linewidth=2.5, 
            linestyle='--', label=r'Odd: $\psi(-x) = -\psi(x)$')
    ax.plot(x_left_odd, psi_left_odd, color=COLORS['tertiary'], linewidth=2.5, linestyle='--')
    ax.plot(x_right_odd, psi_right_odd, color=COLORS['tertiary'], linewidth=2.5, linestyle='--')
    
    # Matching indicators
    ax.plot([-a, -a], [1.5*np.cos(k*a), 1.5*np.cos(k*a)*0.5], 
            'k-', linewidth=1.5, alpha=0.5)
    ax.text(-0.7, 1.0, 'Match', fontsize=9, color=COLORS['dark'])
    
    ax.set_xlim(-3, 3)
    ax.set_ylim(-0.5, 4)
    ax.set_xlabel(r'$x$', fontsize=12)
    ax.set_ylabel(r'$\psi(x)$', fontsize=12)
    ax.set_title('Wave Function Matching at Boundaries', fontsize=13, fontweight='bold')
    ax.legend(loc='upper right', frameon=True)
    ax.axhline(y=0, color=COLORS['gray'], linewidth=0.5, alpha=0.5)
    ax.axhline(y=3, color=COLORS['gray'], linewidth=0.5, alpha=0.3)
    
    return fig

def breit_wigner_resonance():
    """Figure 3: Breit-Wigner resonance curve."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(9, 6))
    
    E = np.linspace(-0.5, 0.5, 500)
    E0 = 0
    Gamma = 0.1
    
    T = (Gamma**2 / 4) / ((E - E0)**2 + Gamma**2 / 4)
    
    ax.fill_between(E, T, alpha=0.2, color=COLORS['primary'])
    ax.plot(E, T, color=COLORS['primary'], linewidth=2.5)
    
    # Half maximum line
    ax.axhline(y=0.5, color=COLORS['gray'], linewidth=1, linestyle='--', alpha=0.7)
    
    # Gamma markers
    ax.axvline(x=Gamma/2, color=COLORS['secondary'], linewidth=1.5, linestyle=':', alpha=0.8)
    ax.axvline(x=-Gamma/2, color=COLORS['secondary'], linewidth=1.5, linestyle=':', alpha=0.8)
    
    # Annotations
    ax.annotate('FWHM = $\Gamma$', xy=(0, 0.52), fontsize=11, ha='center',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.5, edgecolor='none'))
    ax.text(0.08, 0.15, r'$+\Gamma/2$', fontsize=10, color=COLORS['secondary'])
    ax.text(-0.12, 0.15, r'$-\Gamma/2$', fontsize=10, color=COLORS['secondary'])
    
    ax.set_xlim(-0.5, 0.5)
    ax.set_ylim(0, 1.1)
    ax.set_xlabel(r'$E - E_r$', fontsize=12)
    ax.set_ylabel(r'$T(E)$', fontsize=12)
    ax.set_title('Breit-Wigner Resonance Profile', fontsize=13, fontweight='bold')
    
    return fig

def double_barrier():
    """Figure 4: Double barrier resonance structure."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Potential parameters
    a = 1.0
    b = 0.5
    V0 = 3.0
    
    # Draw potential
    x = np.array([-4, -a-b, -a-b, -a, -a, a, a, a+b, a+b, 4])
    V = np.array([0, 0, V0, V0, 0, 0, V0, V0, 0, 0])
    
    ax.fill_between(x, V, alpha=0.15, color=COLORS['dark'])
    ax.plot(x, V, color=COLORS['dark'], linewidth=2.5)
    
    # Well region fill
    x_well = np.linspace(-a, a, 100)
    V_well = np.zeros_like(x_well)
    ax.fill_between(x_well, V_well, alpha=0.25, color=COLORS['primary'])
    
    # Resonance level
    Er = 0.5
    ax.axhline(y=Er, color=COLORS['secondary'], linewidth=1.5, linestyle='--', alpha=0.8)
    ax.text(3, Er+0.15, r'$E_r$', fontsize=11, color=COLORS['secondary'])
    
    # Schematic wave function amplitude
    x_amp = np.linspace(-3.5, 3.5, 300)
    amp = np.ones_like(x_amp)
    # Enhance in well
    mask = (x_amp >= -a) & (x_amp <= a)
    amp[mask] = 3.5
    # Decay in barriers
    mask_left = (x_amp >= -a-b) & (x_amp < -a)
    mask_right = (x_amp > a) & (x_amp <= a+b)
    amp[mask_left] = 0.5 + 3.0 * np.exp((x_amp[mask_left] + a) / 0.3)
    amp[mask_right] = 0.5 + 3.0 * np.exp(-(x_amp[mask_right] - a) / 0.3)
    
    # Smooth
    from scipy.ndimage import gaussian_filter1d
    amp_smooth = gaussian_filter1d(amp, sigma=2)
    
    ax.plot(x_amp, amp_smooth + 4, color=COLORS['tertiary'], linewidth=2.5, label=r'$|\psi|^2$ (resonance)')
    
    # Labels
    ax.text(0, -0.5, 'Well', fontsize=11, ha='center', color=COLORS['primary'])
    ax.text(-1.25, 1.5, 'Barrier', fontsize=10, ha='center', color=COLORS['dark'])
    ax.text(1.25, 1.5, 'Barrier', fontsize=10, ha='center', color=COLORS['dark'])
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-1, 6)
    ax.set_xlabel(r'$x$', fontsize=12)
    ax.set_ylabel(r'$V(x)$ / $|\psi|^2$ (shifted)', fontsize=12)
    ax.set_title('Double-Barrier Resonance Structure', fontsize=13, fontweight='bold')
    ax.legend(loc='upper right', frameon=True)
    
    return fig

def levinson_theorem():
    """Figure 5: Levinson's theorem illustration."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(9, 6))
    
    k = np.linspace(0.01, 3, 500)
    
    # Phase shift with one bound state
    delta_1bound = np.pi - np.arctan(k * 1.5)
    
    # Phase shift with no bound state
    delta_0bound = np.arctan(k * 1.5)
    
    ax.plot(k, delta_1bound, color=COLORS['secondary'], linewidth=2.5, 
            label=r'One bound state: $\delta_0(0) = \pi$')
    ax.plot(k, delta_0bound, color=COLORS['tertiary'], linewidth=2.5, linestyle='--',
            label=r'No bound state: $\delta_0(0) = 0$')
    
    # Pi reference
    ax.axhline(y=np.pi, color=COLORS['gray'], linewidth=1, linestyle=':', alpha=0.7)
    ax.text(0.1, np.pi+0.1, r'$\pi$', fontsize=11, color=COLORS['gray'])
    
    # Difference arrow
    ax.annotate('', xy=(0.5, 2.8), xytext=(0.5, 0.6),
                arrowprops=dict(arrowstyle='<->', color=COLORS['accent'], lw=2))
    ax.text(0.7, 1.7, r'$n\pi$', fontsize=12, color=COLORS['accent'])
    
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3.5)
    ax.set_xlabel(r'$ka$', fontsize=12)
    ax.set_ylabel(r'$\delta_0(k)$', fontsize=12)
    ax.set_title('Phase Shift and Levinson\'s Theorem', fontsize=13, fontweight='bold')
    ax.legend(loc='center right', frameon=True)
    
    return fig

def scattering_geometry():
    """Figure 6: Scattering geometry illustration."""
    setup_style()
    
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Draw incident beam
    ax.arrow(-4, 0, 3, 0, head_width=0.2, head_length=0.3, 
             fc=COLORS['primary'], ec=COLORS['primary'], linewidth=2)
    ax.text(-2.5, 0.4, 'Incident', fontsize=11, color=COLORS['primary'])
    ax.text(-2.5, -0.4, r'$e^{ikz}$', fontsize=11, color=COLORS['primary'])
    
    # Draw scattering center
    circle = plt.Circle((0, 0), 0.5, color=COLORS['dark'], fill=True)
    ax.add_patch(circle)
    ax.text(0, 0, r'$V(r)$', fontsize=11, ha='center', va='center', color='white')
    
    # Draw scattered spherical wave (concentric arcs)
    for r in [1.5, 2.5, 3.5]:
        theta = np.linspace(0.3, 2*np.pi-0.3, 100)
        x_arc = r * np.cos(theta)
        y_arc = r * np.sin(theta)
        ax.plot(x_arc, y_arc, color=COLORS['secondary'], linewidth=1.5, alpha=0.7)
    
    # Scattered wave arrows
    angles = [np.pi/6, np.pi/2, 2*np.pi/3, 5*np.pi/6]
    for angle in angles:
        ax.arrow(0.5*np.cos(angle), 0.5*np.sin(angle), 
                2.5*np.cos(angle), 2.5*np.sin(angle),
                head_width=0.15, head_length=0.2,
                fc=COLORS['secondary'], ec=COLORS['secondary'], linewidth=1.5, alpha=0.7)
    
    # Labels
    ax.text(3, 2, r'$f(\theta)\frac{e^{ikr}}{r}$', fontsize=12, color=COLORS['secondary'])
    ax.text(3.5, 0.3, r'$\theta$', fontsize=11, color=COLORS['dark'])
    
    # Angle arc
    theta_arc = np.linspace(0, np.pi/3, 50)
    r_arc = 3.0
    ax.plot(r_arc*np.cos(theta_arc), r_arc*np.sin(theta_arc), 
            'k-', linewidth=1, alpha=0.5)
    
    ax.set_xlim(-5, 5)
    ax.set_ylim(-3, 4)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('Scattering Geometry', fontsize=13, fontweight='bold', pad=20)
    
    return fig

def main():
    """Generate all figures."""
    print("Generating QM figures...")
    
    # Create output directory
    output_dir = 'docs/images/qm-notes'
    os.makedirs(output_dir, exist_ok=True)
    
    figures = [
        (finite_well_wavefunctions, 'finite-well-wavefunctions.png'),
        (wavefunction_matching, 'wavefunction-matching.png'),
        (breit_wigner_resonance, 'breit-wigner-resonance.png'),
        (double_barrier, 'double-barrier.png'),
        (levinson_theorem, 'levinson-theorem.png'),
        (scattering_geometry, 'scattering-geometry.png'),
    ]
    
    for func, filename in figures:
        try:
            fig = func()
            save_figure(fig, filename, output_dir)
            plt.close(fig)
        except Exception as e:
            print(f"Error generating {filename}: {e}")
    
    print("\nAll figures generated successfully!")

if __name__ == '__main__':
    main()
