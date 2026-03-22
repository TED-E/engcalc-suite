"""
Torque & Power Analyzer
Author: TED-E
Description: Shaft torque, power, and shear stress calculations.
"""

import math


class TorqueAnalyzer:
    """
    Analyze torque, power, and shear stress for rotating shafts.

    Parameters
    ----------
    power_kw : float
        Shaft power in kilowatts
    rpm : float
        Rotational speed in RPM
    """

    def __init__(self, power_kw: float, rpm: float):
        self.power_kw = power_kw
        self.power_w = power_kw * 1000
        self.rpm = rpm
        self.omega = (2 * math.pi * rpm) / 60  # rad/s

    def torque(self) -> float:
        """Calculate torque in N*m. T = P / omega"""
        return self.power_w / self.omega

    def shear_stress(self, diameter: float) -> float:
        """
        Calculate maximum shear stress on shaft surface in MPa.

        Parameters
        ----------
        diameter : float
            Shaft outer diameter in meters
        """
        T = self.torque()
        r = diameter / 2
        J = (math.pi * diameter ** 4) / 32  # polar moment of inertia
        tau = (T * r) / J  # Pa
        return tau / 1e6  # MPa

    def angular_velocity_rads(self) -> float:
        """Return angular velocity in rad/s."""
        return self.omega

    def horsepower(self) -> float:
        """Convert power to horsepower."""
        return self.power_kw * 1.34102

    def summary(self, diameter: float = 0.05) -> dict:
        """Return a summary of all shaft calculations."""
        return {
            'power_kw': self.power_kw,
            'rpm': self.rpm,
            'omega_rad_s': round(self.omega, 4),
            'torque_Nm': round(self.torque(), 3),
            'horsepower': round(self.horsepower(), 3),
            'shear_stress_MPa': round(self.shear_stress(diameter), 4),
        }


if __name__ == '__main__':
    shaft = TorqueAnalyzer(power_kw=75, rpm=1500)
    print("=== Shaft Analysis ===")
    for k, v in shaft.summary(diameter=0.05).items():
        print(f"  {k}: {v}")
