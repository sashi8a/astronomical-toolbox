# Neural Operator for Gravitational Lensing Inversion

This module implements neural operator-based surrogate models to recover mass distributions from lensed images. The goal is to compare modern deep operator architectures against traditional inverse solvers used in astrophysics.

## Goals
- Use FNO / DeepONet / UNet for inverse mapping
- Compare with MCMC/optimization from `lenstronomy`
- Measure speedup and accuracy

## Initial Directory Structure

```bash
astronomical-toolbox/
└── lensing_inversion/
    ├── data/                  # For storing generated lensing images + mass maps
    ├── models/                # Neural operator model definitions
    ├── scripts/               # Training, evaluation, and visualization scripts
    ├── notebooks/             # Jupyter notebooks for prototyping
    ├── utils/                 # Preprocessing, metrics, helper functions
    ├── README.md
    └── requirements.txt
```