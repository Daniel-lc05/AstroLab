# 🚀 AstroLab

**AstroLab** is a modular rocket simulation framework focused on physical consistency and scalable design.

It is built to evolve from simple 1D simulations to full 6DOF dynamics without requiring major rewrites.

VERSION NOTES:
In this version, the structure is clear, but very complex to the beginig. So in the next branch the rocket would be treat as a sounding rocket. A single stage medium rocket to full validate the simulation engine.

---

## ⚙️ Features

* Component-based vehicle modeling (`Part`, `Tank`, `Engine`, etc.)
* Hierarchical assembly system
* 1D simulation with:

  * Variable mass
  * Thrust modeling
  * Gravity and atmospheric effects
  * Aerodynamic drag

---

## 🏗️ Structure

```
AstroLab/
├── main.py
├── vehicle/
├── solver/
├── environment/
└── tools/
```

---

## 🚀 Roadmap

* Multi-stage support
* 2D / 3D simulation
* Guidance and control
* Orbital mechanics

---

## ▶️ Usage

```
python main.py
```

---

## 📌 Notes

* Units must be consistent (mm vs m)
* Designed for engineering accuracy, not shortcuts
