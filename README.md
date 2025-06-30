# 🌌 astronomical-toolbox 
#### *The Universe is not only stranger than we imagine — it is stranger than we can imagine.*
---
A modular suite of **Scientific Machine Learning (SciML)** projects focused on solving cutting-edge problems in **astronomy and astrophysics** using deep learning, neural operators, and generative modeling.

Designed and developed by Sashi Ayyalasomayajula, this repository serves as an evolving research sandbox, enabling rapid prototyping and benchmarking of advanced ML architectures across diverse astrophysical domains — from gravitational lensing and galaxy formation to exoplanet transit modeling and cosmological simulations.

---

## 📦 Repository Structure

Each subdirectory is a standalone project with its own dataset pipelines, training logic, models, and visualizations.

Here's a roadmap below: 
```
astronomical-toolbox/
│
├── lensing_inversion/ # 🔭 Neural Operator for Gravitational Lensing Inversion
├── nbody_surrogate/ # 🌌 Surrogate Models for Cosmological N-body Simulations
├── exoplanet_lightcurves/ # 🪐 Forward & Inverse Modeling of Exoplanet Light Curves
├── galaxy_morphology_generation/ # 🌠 Diffusion Models for Galaxy Image Generation
├── pde_discovery_galaxies/ # 🧠 PDE Discovery for Galaxy Formation Processes
├── generative_lensing_modeling/ # 🔁 Physics-Informed Generative Models for Lensing
└── shared/ # 🧰 Utility modules: metrics, plotting, preprocessing
```
---

## 🚀 Project Goals

For each project:
- 📄 **Research Paper**: Formally written and reproducible
- 🛠️ **Prototype**: Functional code with visualizations
- 🎥 **Interactive Demo**: Gradio/Streamlit app + video explainer
- 📊 **Model Comparison**: Evaluate advanced architectures (FNO, DeepONet, DDPMs) vs. traditional solvers
- ♻️ **Hybrid Approaches**: Combine physics-based and learned methods for robust scientific insight

---

## 🧠 Core Themes

- **Operator Learning**: Using neural operators (e.g., FNO, DeepONet) to learn mappings between function spaces governed by astrophysical PDEs.
- **Surrogate Modeling**: Replacing expensive simulation pipelines with lightweight learned surrogates.
- **Generative Modeling**: Leveraging diffusion models and autoencoders for data generation and inversion tasks.
- **Inverse Problems**: Solving ill-posed astrophysical problems (e.g., lensing inversion, orbital reconstruction).
- **Physics-Informed AI**: Embedding conservation laws, constraints, and PDE priors into model training.

---

## 🛠️ Getting Started

```bash
# Clone the repo
git clone https://github.com/sashi8a/astronomical-toolbox.git
cd astronomical-toolbox

# Navigate into a specific project to get started  (example below)
cd lensing_inversion/
pip install -r requirements.txt
```
---

## 🔭 Current Status
- ✅ Project 1: lensing_inversion — in progress

- 🔜 Other projects scaffolding coming soon

---
## 🤝 Contributions
This repo is currently under active development. Open to collaborations in:

- SciML model architecture design

- Physics-based ML evaluation

- Interactive scientific visualizations

---

## 🧑‍🚀 Author
Sashi Ayyalasomayajula  
Researcher | ML Engineer | Astrophysics Enthusiast  
 ✉️ sashi8a@gmail.com • 🧠 [LinkedIn](https://www.linkedin.com/in/sashi8a)
