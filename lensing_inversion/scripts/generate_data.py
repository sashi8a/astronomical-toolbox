import numpy as np
import os
import matplotlib.pyplot as plt
from lenstronomy.SimulationAPI.sim_api import SimAPI
from lenstronomy.SimulationAPI.data_api import DataAPI
from lenstronomy.Util import util

import lenstronomy
print(lenstronomy.__version__)

# Create folders
os.makedirs("../data/images", exist_ok=True)
os.makedirs("../data/mass_maps", exist_ok=True)

kwargs_detector = {
    "pixel_scale": 0.05,
    "ccd_gain": 1.0,
    "read_noise": 0.0,
    "exposure_time": 1000,
    "background_rms": 0.05,
    "num_exposures": 1,
    "sky_brightness": None,
    "magnitude_zero_point": 25.0
}

kwargs_psf = {
    "psf_type": "GAUSSIAN",
    "fwhm": 0.09
}

kwargs_model = {
    "lens_model_list": ["SIE"],
    "source_light_model_list": ["SERSIC_ELLIPSE"],
    "lens_light_model_list": ["SERSIC_ELLIPSE"],
    "point_source_model_list": [],
}

data_class = DataAPI(numpix=100, kwargs_detector=kwargs_detector, kwargs_psf=kwargs_psf)
sim_api = SimAPI(data_class=data_class, kwargs_model=kwargs_model)



# Loop to generate samples
for i in range(100):
    data = sim_api.simulate()
    img = data["image_data"]  # 2D image
    kwargs_lens = data["model_data"]["kwargs_lens"][0]
    
    # We'll use theta_E (Einstein radius) as a naive placeholder for mass
    mass_map = kwargs_lens["theta_E"] * np.ones_like(img)

    # Save data
    np.save(f"data/images/image_{i:04d}.npy", img)
    np.save(f"data/mass_maps/mass_{i:04d}.npy", mass_map)

    if i % 10 == 0:
        print(f"Generated {i}/100 samples")