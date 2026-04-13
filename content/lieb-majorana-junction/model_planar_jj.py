"""
Planar Josephson Junction on the Altermagnetic Square Lattice Model
====================================================================
Based on arXiv:2603.06487v1: "Altermagnets Enable Gate-Switchable Helical 
and Chiral Topological Transport with Spin-Valley-Momentum-Locked Dual Protection"

This script implements the effective low-energy edge model derived from Eq. (2) 
of the paper, constructs a planar Josephson junction on the helical SVML edge,
and computes the Andreev bound state (ABS) spectrum as a function of the 
superconducting phase difference.  In the short-junction limit the analytical 
condition for a Majorana zero mode is derived and compared with the numerical 
solution.
"""

import sys
import os
import numpy as np
from numpy import cos, sin, pi, sqrt, exp
import matplotlib.pyplot as plt
from scipy import linalg

# ---------------------------------------------------------------------------
# Import the blog-wide plot style
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'utils'))
from plot_style import setup_style, COLORS
setup_style()


# ---------------------------------------------------------------------------
# Effective 1D edge Hamiltonian (discretized massive Dirac model)
# ---------------------------------------------------------------------------
def build_junction_hamiltonian(N, a, vF, m, Delta, phi_left, phi_right,
                                x_left=None, x_right=None):
    """
    Build the BdG Hamiltonian for a planar Josephson junction on a single
    helical edge of the AMQSVH phase.

    The continuum Hamiltonian for the edge reads
        H = -i hbar vF sigma_z partial_x  +  m(x) sigma_x  +  Re Delta(x) tau_x
            - Im Delta(x) tau_y
    where sigma acts in spin space and tau acts in particle-hole space.
    The basis is (c_up, c_down, c_up^dagger, c_down^dagger).

    Parameters
    ----------
    N : int
        Number of lattice sites along the junction.
    a : float
        Lattice spacing (in arbitrary length units).
    vF : float
        Fermi velocity (hbar = 1).
    m : float
        Mass gap in the normal region (can be used to model a gapped edge).
    Delta : float
        Superconducting gap amplitude in the leads.
    phi_left, phi_right : float
        Superconducting phase on the left / right lead (radians).
    x_left, x_right : float, optional
        Positions that delimit the normal region.  Defaults to 1/3 and 2/3 of
        the total length.

    Returns
    -------
    H : (4N, 4N) complex array
        Full BdG matrix.
    """
    if x_left is None:
        x_left = (N // 3) * a
    if x_right is None:
        x_right = (2 * N // 3) * a

    H = np.zeros((4 * N, 4 * N), dtype=complex)

    # hopping amplitude from the kinetic term -i vF sigma_z partial_x
    t_hop = -1j * vF / (2.0 * a)

    for i in range(N):
        x = i * a

        # local superconducting parameters
        if x < x_left:
            D_loc = Delta
            phi_loc = phi_left
        elif x < x_right:
            D_loc = 0.0   # normal region
            phi_loc = 0.0
        else:
            D_loc = Delta
            phi_loc = phi_right

        # --- on-site BdG block ---
        h_ii = np.zeros((4, 4), dtype=complex)

        # mass term  m(x) sigma_x tau_z
        h_ii[0, 1] = m
        h_ii[1, 0] = m
        h_ii[2, 3] = -m
        h_ii[3, 2] = -m

        # pairing  Delta(x) [cos(phi) tau_x - sin(phi) tau_y]
        cp = D_loc * cos(phi_loc)
        sp = D_loc * sin(phi_loc)
        h_ii[0, 2] = cp
        h_ii[0, 3] = +1j * sp
        h_ii[1, 2] = +1j * sp
        h_ii[1, 3] = cp
        h_ii[2, 0] = cp
        h_ii[2, 1] = -1j * sp
        h_ii[3, 0] = -1j * sp
        h_ii[3, 1] = cp

        H[4*i:4*i+4, 4*i:4*i+4] = h_ii

        # --- hopping to i+1 ---
        if i < N - 1:
            h_hop = np.zeros((4, 4), dtype=complex)
            # sigma_z tau_z  in the Nambu basis
            h_hop[0, 0] = t_hop
            h_hop[1, 1] = -t_hop
            h_hop[2, 2] = -t_hop   # hole block = -sigma_z
            h_hop[3, 3] = t_hop

            H[4*i:4*i+4, 4*(i+1):4*(i+1)+4] = h_hop
            H[4*(i+1):4*(i+1)+4, 4*i:4*i+4] = h_hop.conj().T

    return H


def diagonalize_junction(N, a, vF, m, Delta, phi_left, phi_right):
    """Return sorted real eigenvalues of the junction Hamiltonian."""
    H = build_junction_hamiltonian(N, a, vF, m, Delta, phi_left, phi_right)
    evals = linalg.eigvalsh(H)
    return np.sort(np.real(evals))


# ---------------------------------------------------------------------------
# Analytical Majorana condition in the short-junction limit
# ---------------------------------------------------------------------------
def majorana_condition_analytical(m, Delta0):
    """
    For the massive Dirac edge coupled to two s-wave superconductors,
    wave-function matching in the short-junction limit (W << xi) gives

        cos(phi) = (m^2 - Delta0^2) / (m^2 + Delta0^2) .

    See the blog post for the full derivation.
    """
    denom = m**2 + Delta0**2
    if denom == 0:
        return None
    cphi = (m**2 - Delta0**2) / denom
    if abs(cphi) > 1.0 + 1e-12:
        return None
    cphi = np.clip(cphi, -1.0, 1.0)
    return np.arccos(cphi)


# ---------------------------------------------------------------------------
# Figures
# ---------------------------------------------------------------------------
def figure_abs_spectrum(N=250, a=0.5, vF=1.0, m=0.0, Delta=0.1,
                        n_phi=101, output_dir='../../docs/images/condensed-matter'):
    """
    Figure 1: Andreev bound state spectrum E(phi) for the planar JJ.
    """
    phi_vals = np.linspace(-pi, pi, n_phi)
    energies = []
    for phi in phi_vals:
        evals = diagonalize_junction(N, a, vF, m, Delta,
                                     phi_left=-phi/2, phi_right=phi/2)
        mask = np.abs(evals) < 2.5 * Delta
        energies.append(evals[mask])

    fig, ax = plt.subplots(figsize=(6, 4.5))
    for i, phi in enumerate(phi_vals):
        ax.scatter(np.full_like(energies[i], phi),
                   np.array(energies[i]) / Delta,
                   s=3, c=COLORS['primary'], alpha=0.5, rasterized=True)

    # mark the analytical Majorana point if m != 0
    if m != 0:
        phi_maj = majorana_condition_analytical(m, Delta)
        if phi_maj is not None:
            for sign in (+1, -1):
                ax.axvline(sign * phi_maj, color=COLORS['secondary'],
                           linestyle='--', linewidth=1.5, alpha=0.7,
                           label='Majorana point' if sign == 1 else None)
            ax.legend(loc='upper right')

    ax.axhline(0, color='black', linestyle='--', linewidth=0.6, alpha=0.5)
    ax.set_xlabel(r'Phase difference $\phi$')
    ax.set_ylabel(r'$E / \Delta_0$')
    ax.set_xlim(-pi, pi)
    ax.set_ylim(-0.4, 0.4)
    ax.set_xticks([-pi, -pi/2, 0, pi/2, pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$',
                        r'$\pi/2$', r'$\pi$'])
    ax.set_title('Andreev Bound States in the Planar Josephson Junction')
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    fig.savefig(os.path.join(output_dir,
                             'planar_jj_abs_spectrum.png'), dpi=300)
    plt.close(fig)
    print("Saved: planar_jj_abs_spectrum.png")
    return phi_vals, energies


def figure_majorana_condition(Delta=0.1, output_dir='../../docs/images/condensed-matter'):
    """
    Figure 2: Phase difference required for a Majorana zero mode as a
    function of the edge mass gap m / Delta0.
    """
    m_vals = np.linspace(-2.5 * Delta, 2.5 * Delta, 500)
    phi_maj = []
    for m in m_vals:
        phi = majorana_condition_analytical(m, Delta)
        phi_maj.append(phi if phi is not None else np.nan)
    phi_maj = np.array(phi_maj)

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(m_vals / Delta, np.degrees(phi_maj),
            color=COLORS['primary'], linewidth=2.2, label=r'$\phi_{\rm M}$')
    ax.plot(m_vals / Delta, -np.degrees(phi_maj),
            color=COLORS['primary'], linewidth=2.2)

    ax.axhline(180, color=COLORS['gray'], linestyle='--', linewidth=1, alpha=0.5)
    ax.axhline(-180, color=COLORS['gray'], linestyle='--', linewidth=1, alpha=0.5)
    ax.set_xlabel(r'Edge mass gap $m / \Delta_0$')
    ax.set_ylabel(r'Majorana phase $\phi_{\rm M}$ (deg)')
    ax.set_xlim(-2.5, 2.5)
    ax.set_ylim(-200, 200)
    ax.set_title(r'Short-Junction Majorana Condition: $\cos\phi = \
        \frac{m^2 - \Delta_0^2}{m^2 + \Delta_0^2}$')
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    fig.savefig(os.path.join(output_dir,
                             'planar_jj_majorana_condition.png'), dpi=300)
    plt.close(fig)
    print("Saved: planar_jj_majorana_condition.png")


def figure_wavefunction(N=250, a=0.5, vF=1.0, m=0.05, Delta=0.1,
                        phi=np.pi, output_dir='../../docs/images/condensed-matter'):
    """
    Figure 3: Spatial profile of the Majorana zero-mode wavefunction.
    """
    H = build_junction_hamiltonian(N, a, vF, m, Delta,
                                   phi_left=-phi/2, phi_right=phi/2)
    evals, evecs = linalg.eigh(H)

    # Find the eigenstate closest to zero energy
    idx = np.argmin(np.abs(evals))
    E0 = evals[idx]
    psi = evecs[:, idx]

    x = np.arange(N) * a
    rho = np.abs(psi)**2
    # sum over the 4 Nambu components
    rho_total = (rho[0::4] + rho[1::4] + rho[2::4] + rho[3::4])

    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.fill_between(x, rho_total, alpha=0.25, color=COLORS['primary'])
    ax.plot(x, rho_total, color=COLORS['primary'], linewidth=1.5)
    ax.axvline((N // 3) * a, color=COLORS['gray'], linestyle='--', linewidth=1)
    ax.axvline((2 * N // 3) * a, color=COLORS['gray'], linestyle='--', linewidth=1)
    ax.text((N // 6) * a, max(rho_total) * 0.85, r'SC$_{L}$',
            ha='center', fontsize=11, color=COLORS['dark'])
    ax.text((N // 2) * a, max(rho_total) * 0.85, r'N',
            ha='center', fontsize=11, color=COLORS['dark'])
    ax.text((5 * N // 6) * a, max(rho_total) * 0.85, r'SC$_{R}$',
            ha='center', fontsize=11, color=COLORS['dark'])
    ax.set_xlabel(r'Position $x$')
    ax.set_ylabel(r'$|\psi(x)|^2$')
    ax.set_title(f'Majorana Zero-Mode Wavefunction  (E = {E0:.2e}, '
                 f'm={m:.2f}, ' + r'$\phi=\pi$)')
    plt.tight_layout()

    os.makedirs(output_dir, exist_ok=True)
    fig.savefig(os.path.join(output_dir,
                             'planar_jj_majorana_wf.png'), dpi=300)
    plt.close(fig)
    print("Saved: planar_jj_majorana_wf.png")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    print("=" * 70)
    print("Planar Josephson Junction on Altermagnetic SVML Edge")
    print("Reference: arXiv:2603.06487v1")
    print("=" * 70)

    # --- Figure 1: ABS spectrum for a gapless edge (m = 0) ---
    print("\n[1/4] Computing ABS spectrum for m = 0 ...")
    phi_vals, energies = figure_abs_spectrum(N=250, a=0.5, vF=1.0,
                                              m=0.0, Delta=0.1, n_phi=101)

    # --- Figure 2: Majorana condition vs mass gap ---
    print("\n[2/4] Plotting analytical Majorana condition ...")
    figure_majorana_condition(Delta=0.1)

    # --- Figure 3: Majorana wavefunction at m = 0.05, phi = pi ---
    print("\n[3/4] Computing Majorana wavefunction ...")
    figure_wavefunction(N=250, a=0.5, vF=1.0, m=0.05, Delta=0.1, phi=np.pi)

    # --- Additional: ABS spectrum for a gapped edge (m = 0.05) ---
    print("\n[4/4] Computing ABS spectrum for m = 0.05 ...")
    phi_vals2, energies2 = figure_abs_spectrum(N=250, a=0.5, vF=1.0,
                                                m=0.05, Delta=0.1, n_phi=101)
    # rename the output so it does not overwrite the m=0 figure
    import shutil
    src = '../../docs/images/condensed-matter/planar_jj_abs_spectrum.png'
    dst = '../../docs/images/condensed-matter/planar_jj_abs_spectrum_m005.png'
    shutil.copy(src, dst)
    print(f"Saved: {dst}")

    # --- Print analytical predictions ---
    print("\n" + "-" * 70)
    print("Analytical Majorana condition (short-junction limit):")
    for m_test in [0.0, 0.05, 0.10, 0.15]:
        phi_maj = majorana_condition_analytical(m_test, 0.1)
        if phi_maj is not None:
            print(f"  m = {m_test:.2f}:  phi_M = {phi_maj:.4f} rad  "
                  f"({np.degrees(phi_maj):.1f} deg)")
        else:
            print(f"  m = {m_test:.2f}:  no real solution")
    print("-" * 70)
