"""
Standardized plotting style for blog figures.
Import this module to ensure consistent figure appearance across all posts.
"""

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

# Color scheme - Academic, clean, colorblind-friendly
COLORS = {
    'primary': '#2E5AAC',      # Deep blue
    'secondary': '#C44E52',    # Muted red
    'tertiary': '#4C9F50',     # Green
    'quaternary': '#9B59B6',   # Purple
    'accent': '#F39C12',       # Orange
    'gray': '#7F8C8D',         # Gray
    'lightgray': '#BDC3C7',    # Light gray
    'dark': '#2C3E50',         # Dark text
}

def setup_style():
    """Configure matplotlib with standardized style."""
    plt.style.use('default')
    
    # Figure settings
    mpl.rcParams['figure.dpi'] = 150
    mpl.rcParams['figure.facecolor'] = 'white'
    mpl.rcParams['axes.facecolor'] = 'white'
    mpl.rcParams['savefig.facecolor'] = 'white'
    mpl.rcParams['savefig.dpi'] = 200
    mpl.rcParams['savefig.bbox'] = 'tight'
    mpl.rcParams['savefig.pad_inches'] = 0.1
    
    # Font settings - clean academic look
    mpl.rcParams['font.family'] = 'sans-serif'
    mpl.rcParams['font.sans-serif'] = ['Arial', 'Helvetica', 'DejaVu Sans']
    mpl.rcParams['font.size'] = 11
    mpl.rcParams['axes.titlesize'] = 13
    mpl.rcParams['axes.labelsize'] = 11
    mpl.rcParams['xtick.labelsize'] = 10
    mpl.rcParams['ytick.labelsize'] = 10
    mpl.rcParams['legend.fontsize'] = 10
    
    # Axis settings
    mpl.rcParams['axes.linewidth'] = 1.0
    mpl.rcParams['axes.edgecolor'] = COLORS['dark']
    mpl.rcParams['axes.labelcolor'] = COLORS['dark']
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'
    mpl.rcParams['xtick.major.width'] = 0.8
    mpl.rcParams['ytick.major.width'] = 0.8
    mpl.rcParams['xtick.color'] = COLORS['dark']
    mpl.rcParams['ytick.color'] = COLORS['dark']
    
    # Grid settings
    mpl.rcParams['grid.linewidth'] = 0.5
    mpl.rcParams['grid.alpha'] = 0.3
    
    # Legend settings
    mpl.rcParams['legend.frameon'] = True
    mpl.rcParams['legend.framealpha'] = 0.9
    mpl.rcParams['legend.edgecolor'] = COLORS['lightgray']
    mpl.rcParams['legend.fancybox'] = False
    
    # Line settings
    mpl.rcParams['lines.linewidth'] = 2.0
    mpl.rcParams['lines.markersize'] = 6

def save_figure(fig, filename, output_dir='docs/images/qm-notes'):
    """Save figure with standardized settings."""
    import os
    os.makedirs(output_dir, exist_ok=True)
    filepath = os.path.join(output_dir, filename)
    fig.savefig(filepath, format='png')
    print(f"Saved: {filepath}")
    return filepath

# Convenience function for common plot elements
def add_potential_well(ax, x_center=0, width=2, depth=-1, barrier_height=0, 
                       barrier_thickness=0.5, color='black', linewidth=2):
    """Draw a 1D potential well."""
    # Left region
    x_left = [x_center - width/2 - barrier_thickness - 2, 
              x_center - width/2 - barrier_thickness]
    y_barrier = [barrier_height, barrier_height]
    ax.plot(x_left, y_barrier, color=color, linewidth=linewidth)
    
    # Left barrier
    x_lbarrier = [x_center - width/2 - barrier_thickness, 
                  x_center - width/2 - barrier_thickness,
                  x_center - width/2]
    y_lbarrier = [barrier_height, depth, depth]
    ax.plot(x_lbarrier, y_lbarrier, color=color, linewidth=linewidth)
    
    # Well bottom
    x_well = [x_center - width/2, x_center + width/2]
    y_well = [depth, depth]
    ax.plot(x_well, y_well, color=color, linewidth=linewidth)
    
    # Right barrier
    x_rbarrier = [x_center + width/2, 
                  x_center + width/2 + barrier_thickness,
                  x_center + width/2 + barrier_thickness]
    y_rbarrier = [depth, barrier_height, barrier_height]
    ax.plot(x_rbarrier, y_rbarrier, color=color, linewidth=linewidth)
    
    # Right region
    x_right = [x_center + width/2 + barrier_thickness, 
               x_center + width/2 + barrier_thickness + 2]
    y_barrier = [barrier_height, barrier_height]
    ax.plot(x_right, y_barrier, color=color, linewidth=linewidth)

if __name__ == '__main__':
    setup_style()
    print("Plot style configured successfully.")
    print(f"Available colors: {list(COLORS.keys())}")
