import math
import numpy as np


class SliderCrank:
    """Inline slider-crank with crank radius r and connecting rod length l."""

    def __init__(self, crank_radius: float, rod_length: float):
        if crank_radius <= 0 or rod_length <= 0:
            raise ValueError("Lengths must be positive.")
        if rod_length < crank_radius:
            raise ValueError("rod_length must be >= crank_radius for a full rotation.")
        self.r = float(crank_radius)
        self.l = float(rod_length)

    def position(self, theta: float):
        s = self.r * math.sin(theta)
        return self.r * math.cos(theta) + math.sqrt(self.l**2 - s**2)

    def connecting_rod_angle(self, theta: float):
        return math.asin((self.r / self.l) * math.sin(theta))

    def sweep(self, theta_values):
        theta_values = np.asarray(theta_values, dtype=float)
        return np.array([self.position(t) for t in theta_values])
