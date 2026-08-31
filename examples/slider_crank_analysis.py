from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from mechanism_kinematics import SliderCrank


def main():
    mechanism = SliderCrank(crank_radius=0.04, rod_length=0.14)
    theta = np.linspace(0, 2*np.pi, 361)
    position = mechanism.sweep(theta)

    fig, ax = plt.subplots(figsize=(8.5, 5))
    ax.plot(np.rad2deg(theta), position * 1000)
    ax.set_xlabel('Crank angle [deg]')
    ax.set_ylabel('Slider position [mm]')
    ax.set_title('Slider-Crank Position Analysis')
    ax.grid(True, alpha=0.25)
    fig.tight_layout()

    out = Path(__file__).resolve().parents[1] / 'assets' / 'slider_crank_position.png'
    out.parent.mkdir(exist_ok=True)
    fig.savefig(out, dpi=180)
    print(f"Stroke: {(position.max()-position.min())*1000:.2f} mm")


if __name__ == '__main__':
    main()
