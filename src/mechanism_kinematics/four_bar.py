from dataclasses import dataclass
import math
import numpy as np


@dataclass(frozen=True)
class FourBarConfiguration:
    theta2: float
    theta3: float
    theta4: float
    O2: np.ndarray
    A: np.ndarray
    B: np.ndarray
    O4: np.ndarray


class FourBar:
    """Planar four-bar using circle-circle intersection for position analysis.

    Link convention:
      a: input crank O2-A
      b: coupler A-B
      c: output rocker O4-B
      d: ground O2-O4
    """

    def __init__(self, a: float, b: float, c: float, d: float):
        if min(a, b, c, d) <= 0:
            raise ValueError("All link lengths must be positive.")
        self.a, self.b, self.c, self.d = map(float, (a, b, c, d))

    @property
    def grashof(self):
        links = sorted([self.a, self.b, self.c, self.d])
        s, p, q, l = links
        return s + l <= p + q + 1e-12

    def solve(self, theta2: float, branch: int = 1):
        if branch not in (-1, 1):
            raise ValueError("branch must be +1 or -1.")
        O2 = np.array([0.0, 0.0])
        O4 = np.array([self.d, 0.0])
        A = self.a * np.array([math.cos(theta2), math.sin(theta2)])
        delta = O4 - A
        e = float(np.linalg.norm(delta))
        if e > self.b + self.c + 1e-12 or e < abs(self.b - self.c) - 1e-12 or e == 0:
            raise ValueError("No real assembly exists at this input angle.")

        x = (self.b**2 - self.c**2 + e**2) / (2 * e)
        h2 = self.b**2 - x**2
        h = math.sqrt(max(0.0, h2))
        ex = delta / e
        ey = np.array([-ex[1], ex[0]])
        B = A + x * ex + branch * h * ey

        theta3 = math.atan2(B[1] - A[1], B[0] - A[0])
        theta4 = math.atan2(B[1] - O4[1], B[0] - O4[0])
        return FourBarConfiguration(theta2, theta3, theta4, O2, A, B, O4)

    def transmission_angle(self, config: FourBarConfiguration):
        """Included angle between the coupler and rocker at joint B, in radians."""
        ba = config.A - config.B
        bo4 = config.O4 - config.B
        cos_mu = np.dot(ba, bo4) / (np.linalg.norm(ba) * np.linalg.norm(bo4))
        return float(np.arccos(np.clip(cos_mu, -1.0, 1.0)))

    def coupler_point(self, config: FourBarConfiguration, along: float = 0.5, offset: float = 0.0):
        """Point fixed to coupler: along is fraction A->B; offset is normal distance."""
        AB = config.B - config.A
        length = np.linalg.norm(AB)
        tangent = AB / length
        normal = np.array([-tangent[1], tangent[0]])
        return config.A + along * AB + offset * normal

    def sweep(self, theta2_values, branch: int = 1, skip_invalid: bool = True):
        configs = []
        for angle in theta2_values:
            try:
                configs.append(self.solve(float(angle), branch=branch))
            except ValueError:
                if not skip_invalid:
                    raise
        return configs
