# ⚙️ EngCalc Suite

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> A Python toolkit for electromechanical engineering calculations — beam deflection, shaft torque, thermal resistance, and stress analysis.

---

## 📌 Features

- 📐 **Beam Deflection Calculator** — simply supported & cantilever beams
- ⚙️ **Torque & Power Analyzer** — shaft torque, angular velocity, and horsepower
- 🔥 **Thermal Resistance Tool** — series/parallel thermal circuits
- 📊 **Stress & Strain Calculator** — axial, shear, and von Mises stress
- 📈 **Matplotlib plots** for all calculations

---

## 📁 Project Structure

```
engcalc-suite/
├── engcalc/
│   ├── __init__.py
│   ├── beam.py          # Beam deflection calculations
│   ├── torque.py        # Torque and power analysis
│   ├── thermal.py       # Thermal resistance analysis
│   └── stress.py        # Stress and strain calculations
├── examples/
│   └── demo.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Quick Start

```bash
# Clone the repo
git clone https://github.com/TED-E/engcalc-suite.git
cd engcalc-suite

# Install dependencies
pip install -r requirements.txt

# Run the demo
python examples/demo.py
```

---

## 💻 Usage Examples

### Beam Deflection
```python
from engcalc.beam import BeamCalculator

beam = BeamCalculator(length=5.0, load=10000, E=200e9, I=8.33e-6)
print(f"Max deflection: {beam.max_deflection():.4f} m")
beam.plot()
```

### Torque Analysis
```python
from engcalc.torque import TorqueAnalyzer

shaft = TorqueAnalyzer(power_kw=75, rpm=1500)
print(f"Torque: {shaft.torque():.2f} N·m")
print(f"Shear stress: {shaft.shear_stress(diameter=0.05):.2f} MPa")
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| NumPy | Numerical computations |
| Matplotlib | Plots and visualizations |
| SciPy | Advanced engineering math |

---

## 📄 License

MIT License © 2026 [TED-E](https://github.com/TED-E)
