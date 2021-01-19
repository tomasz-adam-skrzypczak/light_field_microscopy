import yaml
import logging
from collections import namedtuple

import numpy as np


MICROSCOPE_ATTRIBIUTES = [
    "pitch", "fml", "ftl", "n", "magnification", "NA", "wavelength", 
]


PSF_ATTRIBUTES = [
    "osr", "vpix", "k0", "k", "fobj", "fnum_obj",
    "fnum_ml", "pixel_pitch", "subpixel_pitch", "alpha",
    "zmin", "zmax", "zspacing"
]


MicroParams = namedtuple("MicroParams", MICROSCOPE_ATTRIBIUTES)
PSFParams = namedtuple("PSFParams", PSF_ATTRIBUTES)


logger = logging.getLogger(__name__)


def load_settings(settings_path : str) -> dict:
    try:
        with open(settings_path, 'r') as handle:
            return yaml.safe_load(handle)
    except yaml.YAMLError as err:
        logger.error("Error parsing parameters", err)


def calculate_psf_params(microscope_params : MicroParams, psf_sim_dict : dict):
    magni = microscope_params.magnification
    k0 = 2 * np.pi / microscope_params.wavelength
    pixel_pitch = microscope_params.pitch / psf_sim_dict["vpix"]

    return PSFParams(
        psf_sim_dict["osr"], psf_sim_dict["vpix"], 
        k0, k0 * microscope_params.n, 
        microscope_params.ftl / magni, 
        magni / (2 * microscope_params.NA),
        microscope_params.fml / microscope_params.pitch,
        pixel_pitch, pixel_pitch / psf_sim_dict["osr"],
        np.arcsin(microscope_params.NA / microscope_params.n),
        psf_sim_dict["zmin"], psf_sim_dict["zmax"], psf_sim_dict["zspacing"]
    )


def get_simulation_parameters(settings_path : str):
    settings_dict = load_settings(settings_path)

    ml_dict = settings_dict["ml"]
    optics_dict = settings_dict["optics"]
    psf_dict = settings_dict["psf"]

    micro_params_dict = ml_dict
    micro_params_dict.update(optics_dict)

    micro_params = MicroParams(*[micro_params_dict[attr] for attr in MICROSCOPE_ATTRIBIUTES])
    psf_params = calculate_psf_params(micro_params, psf_dict)
    return micro_params, psf_params    
