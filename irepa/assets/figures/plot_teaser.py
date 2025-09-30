#!/usr/bin/env python3
"""
Generate teaser figure for iREPA project page.

This recreates the main teaser figure with proper formatting for web display.
Ensures no rotation issues, correct dimensions, and professional styling.

Usage:
    python plot_teaser.py

Output:
    teaser.png in current directory (1200x800px)
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Set style for professional look
plt.style.use('seaborn-v0_8-darkgrid')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Arial', 'DejaVu Sans']
plt.rcParams['font.size'] = 11
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10
plt.rcParams['legend.fontsize'] = 10


def create_teaser_figure():
    """
    Create the main teaser figure showing:
    - Spatial structure vs global information comparison
    - Correlation plots
    - Example comparisons

    TODO: Replace with actual data from your experiments
    This is a template - customize with your actual results.
    """

    # Create figure with subplots
    fig = plt.figure(figsize=(16, 10), dpi=100)

    # Define layout: 2 rows, 3 columns
    gs = fig.add_gridspec(2, 3, hspace=0.3, wspace=0.3,
                          left=0.08, right=0.95, bottom=0.08, top=0.92)

    # Title
    fig.suptitle('What Drives Representation Alignment: Global Information or Spatial Structure?',
                 fontsize=16, fontweight='bold', y=0.98)

    # --- SUBPLOT 1: Correlation SSM vs FID ---
    ax1 = fig.add_subplot(gs[0, 0])

    # TODO: Replace with actual data
    # This is example data - replace with your actual encoder data
    np.random.seed(42)
    n_encoders = 27
    fid_scores = np.random.uniform(15, 40, n_encoders)
    ssm_scores = -fid_scores + np.random.normal(0, 3, n_encoders)  # High correlation

    ax1.scatter(ssm_scores, fid_scores, s=100, alpha=0.6, c='#667eea', edgecolors='black', linewidth=0.5)
    ax1.set_xlabel('Spatial Structure Metric (SSM)')
    ax1.set_ylabel('FID Score (↓ better)')
    ax1.set_title('SSM vs FID: |r| = 0.852', fontweight='bold')
    ax1.grid(True, alpha=0.3)

    # Add trend line
    z = np.polyfit(ssm_scores, fid_scores, 1)
    p = np.poly1d(z)
    x_line = np.linspace(ssm_scores.min(), ssm_scores.max(), 100)
    ax1.plot(x_line, p(x_line), "r--", alpha=0.8, linewidth=2)

    # --- SUBPLOT 2: Correlation LP vs FID ---
    ax2 = fig.add_subplot(gs[0, 1])

    # TODO: Replace with actual data
    lp_scores = np.random.uniform(50, 85, n_encoders)  # ImageNet accuracy
    fid_scores_2 = np.random.uniform(15, 40, n_encoders)  # Low correlation

    ax2.scatter(lp_scores, fid_scores_2, s=100, alpha=0.6, c='#999999', edgecolors='black', linewidth=0.5)
    ax2.set_xlabel('Linear Probing Accuracy (%)')
    ax2.set_ylabel('FID Score (↓ better)')
    ax2.set_title('LP Accuracy vs FID: |r| = 0.26', fontweight='bold')
    ax2.grid(True, alpha=0.3)

    # --- SUBPLOT 3: Key Takeaway ---
    ax3 = fig.add_subplot(gs[0, 2])
    ax3.axis('off')

    takeaway_text = """
    KEY FINDING:

    Spatial Structure >> Global Information

    • SSM correlation: |r| = 0.852
    • LP correlation: |r| = 0.26

    ⟹ 3× better predictor

    Encoders with lower ImageNet
    accuracy but better spatial
    structure outperform for REPA.
    """

    ax3.text(0.1, 0.5, takeaway_text, fontsize=11, verticalalignment='center',
             bbox=dict(boxstyle='round', facecolor='#f8f9fa', edgecolor='#667eea', linewidth=2),
             family='monospace')

    # --- SUBPLOT 4: Example Comparison 1 ---
    ax4 = fig.add_subplot(gs[1, 0])

    encoders = ['PE-Spatial-B', 'PE-Core-G', 'WebSSL-1B']
    accuracy = [53.1, 82.8, 76.0]
    fid = [21.0, 32.3, 26.1]

    x = np.arange(len(encoders))
    width = 0.35

    ax4_twin = ax4.twinx()

    bars1 = ax4.bar(x - width/2, accuracy, width, label='ImageNet Acc', color='#999999', alpha=0.7)
    bars2 = ax4_twin.bar(x + width/2, fid, width, label='FID (↓)', color='#667eea', alpha=0.7)

    ax4.set_xlabel('Vision Encoder')
    ax4.set_ylabel('ImageNet Accuracy (%)', color='#999999')
    ax4_twin.set_ylabel('FID Score', color='#667eea')
    ax4.set_title('Example: Lower Accuracy, Better Generation', fontweight='bold')
    ax4.set_xticks(x)
    ax4.set_xticklabels(encoders, rotation=15, ha='right')
    ax4.tick_params(axis='y', labelcolor='#999999')
    ax4_twin.tick_params(axis='y', labelcolor='#667eea')
    ax4.grid(True, alpha=0.2, axis='y')

    # --- SUBPLOT 5: iREPA Improvement ---
    ax5 = fig.add_subplot(gs[1, 1])

    # TODO: Replace with actual convergence data
    iterations = np.array([0, 25, 50, 75, 100])
    repa_fid = np.array([50, 35, 28, 24, 22])
    irepa_fid = np.array([50, 30, 22, 18, 16])

    ax5.plot(iterations, repa_fid, 'o-', label='REPA (baseline)', linewidth=2, markersize=6)
    ax5.plot(iterations, irepa_fid, 's-', label='iREPA (ours)', linewidth=2, markersize=6, color='#667eea')
    ax5.set_xlabel('Training Iterations (K)')
    ax5.set_ylabel('FID Score (↓ better)')
    ax5.set_title('iREPA: Faster Convergence', fontweight='bold')
    ax5.legend()
    ax5.grid(True, alpha=0.3)

    # --- SUBPLOT 6: Method Summary ---
    ax6 = fig.add_subplot(gs[1, 2])
    ax6.axis('off')

    method_text = """
    iREPA METHOD:

    1. Spatial Normalization
       Boosts spatial contrast

    2. Conv Projection
       Preserves spatial structure
       (vs MLP baseline)

    Implementation: <4 lines

    ✓ Works across encoders
    ✓ Works across model sizes
    ✓ Works with REPA variants
    """

    ax6.text(0.1, 0.5, method_text, fontsize=10, verticalalignment='center',
             bbox=dict(boxstyle='round', facecolor='#f8f9fa', edgecolor='#764ba2', linewidth=2),
             family='monospace')

    # Save
    output_path = Path(__file__).parent / 'teaser.png'
    plt.savefig(output_path, dpi=100, bbox_inches='tight', pad_inches=0.2)
    print(f"✓ Teaser figure saved: {output_path}")
    print(f"  Dimensions: 1600x1000 (16:10 aspect ratio)")
    print("\nNext steps:")
    print(f"1. Review the figure: open {output_path}")
    print("2. Copy to static: cp assets/figures/teaser.png static/img/")
    print("3. Replace data with actual experimental results")

    return str(output_path)


if __name__ == "__main__":
    print("Generating teaser figure...")
    print("="*60)
    create_teaser_figure()
    print("="*60)