from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

from mechanism_kinematics import FourBar


def main():
    mechanism = FourBar(a=0.06, b=0.16, c=0.12, d=0.18)
    theta2 = np.linspace(np.deg2rad(15), np.deg2rad(165), 301)
    configs = mechanism.sweep(theta2, branch=1)

    input_deg = np.rad2deg([c.theta2 for c in configs])
    output_deg = np.rad2deg(np.unwrap([c.theta4 for c in configs]))
    transmission = []
    coupler_pts = []
    for c in configs:
        mu = mechanism.transmission_angle(c)
        transmission.append(np.rad2deg(mu))
        coupler_pts.append(mechanism.coupler_point(c, along=0.55, offset=0.025))
    coupler_pts = np.asarray(coupler_pts)

    root = Path(__file__).resolve().parents[1]
    assets = root / 'assets'
    assets.mkdir(exist_ok=True)

    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.plot(input_deg, output_deg)
    ax.set_xlabel('Input angle θ₂ [deg]')
    ax.set_ylabel('Output angle θ₄ [deg]')
    ax.set_title('Four-Bar Input–Output Relationship')
    ax.grid(True, alpha=0.25)
    fig.tight_layout()
    fig.savefig(assets / 'four_bar_input_output.png', dpi=180)

    fig2, ax2 = plt.subplots(figsize=(7, 6))
    ax2.plot(coupler_pts[:, 0], coupler_pts[:, 1])
    ax2.set_aspect('equal', adjustable='box')
    ax2.set_xlabel('x [m]')
    ax2.set_ylabel('y [m]')
    ax2.set_title('Coupler Point Path')
    ax2.grid(True, alpha=0.25)
    fig2.tight_layout()
    fig2.savefig(assets / 'coupler_curve.png', dpi=180)

    print(f"Grashof mechanism: {mechanism.grashof}")
    print(f"Solved {len(configs)} configurations")
    print(f"Transmission-angle range: {min(transmission):.2f}° to {max(transmission):.2f}°")


if __name__ == '__main__':
    main()
