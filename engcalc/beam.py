"""
Beam Deflection Calculator
Author: TED-E
Description: Calculate beam deflection for simply supported and cantilever beams.
"""

import numpy as np
import matplotlib.pyplot as plt


class BeamCalculator:
    """
    Calculate deflection and slope for common beam configurations.

    Parameters
    ----------
    length : float
        Beam length in meters
    load : float
        Applied load in Newtons
    E : float
        Young's modulus in Pa (e.g. 200e9 for steel)
    I : float
        Second moment of area in m^4
    beam_type : str
        'simply_supported' or 'cantilever'
    """

    def __init__(self, length: float, load: float, E: float, I: float,
                 beam_type: str = 'simply_supported'):
        self.L = length
        self.F = load
        self.E = E
        self.I = I
        self.beam_type = beam_type
        self.EI = E * I

    def max_deflection(self) -> float:
        """Return maximum deflection in meters."""
        if self.beam_type == 'simply_supported':
            # delta_max = FL^3 / (48EI)
            return (self.F * self.L ** 3) / (48 * self.EI)
        elif self.beam_type == 'cantilever':
            # delta_max = FL^3 / (3EI)
            return (self.F * self.L ** 3) / (3 * self.EI)
        else:
            raise ValueError(f"Unknown beam type: {self.beam_type}")

    def deflection_profile(self, num_points: int = 200):
        """Return x positions and corresponding deflections."""
        x = np.linspace(0, self.L, num_points)
        if self.beam_type == 'simply_supported':
            # v(x) = Fx(3L^2 - 4x^2) / (48EI)  for x <= L/2
            y = np.where(
                x <= self.L / 2,
                (self.F * x * (3 * self.L ** 2 - 4 * x ** 2)) / (48 * self.EI),
                (self.F * (self.L - x) * (3 * self.L ** 2 - 4 * (self.L - x) ** 2))
                / (48 * self.EI),
            )
        elif self.beam_type == 'cantilever':
            # v(x) = Fx^2(3L - x) / (6EI)
            y = (self.F * x ** 2 * (3 * self.L - x)) / (6 * self.EI)
        else:
            raise ValueError(f"Unknown beam type: {self.beam_type}")
        return x, y

    def plot(self, save_path: str = None):
        """Plot the deflection profile."""
        x, y = self.deflection_profile()
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(x, y * 1000, color='royalblue', linewidth=2.5, label='Deflection')
        ax.fill_between(x, y * 1000, alpha=0.15, color='royalblue')
        ax.set_xlabel('Position along beam (m)', fontsize=12)
        ax.set_ylabel('Deflection (mm)', fontsize=12)
        ax.set_title(
            f'{self.beam_type.replace("_", " ").title()} Beam Deflection\n'
            f'L={self.L}m, F={self.F}N, E={self.E:.0e}Pa',
            fontsize=13,
        )
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend()
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=150)
        else:
            plt.show()
        plt.close()

    def summary(self) -> dict:
        """Return a summary dictionary of results."""
        delta_max = self.max_deflection()
        return {
            'beam_type': self.beam_type,
            'length_m': self.L,
            'load_N': self.F,
            'EI': self.EI,
            'max_deflection_m': delta_max,
            'max_deflection_mm': delta_max * 1000,
        }


if __name__ == '__main__':
    beam = BeamCalculator(length=5.0, load=10_000, E=200e9, I=8.33e-6)
    results = beam.summary()
    print("=== Beam Deflection Results ===")
    for k, v in results.items():
        print(f"  {k}: {v}")
    beam.plot()
