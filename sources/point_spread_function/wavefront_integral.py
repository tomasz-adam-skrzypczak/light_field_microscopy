import numpy as np
from scipy.special import jn


class WavefrontIntegral:

    def __init__(self, microscope_params, psf_params):

        self.wave_len = microscope_params.wavelength
        self.m = microscope_params.magnification

        self.alpha = psf_params.alpha 
        self.fobj = psf_params.fobj
        self.k = psf_params.k

    def get_integral(self, x_point: np.array, p_source: np.array):
        x_norm = np.linalg.norm((x_point - p_source[:2]), ord=2) / self.m
        print(x_norm.shape)
        v = (self.k * x_norm * np.sin(self.alpha)).reshape((-1, 1))
        u = 4 * self.k * p_source[2] * np.sin(self.alpha / 2) ** 2 

        coeff = self.m / ( (self.fobj * self.wave_len) ** 2) * np.exp( -1j * u / (4 * (np.sin(self.alpha / 2) ** 2) ) )

        def _integral(theta):
            result = np.sqrt(np.cos(theta)) * \
                   np.exp(-(1j * u / 2) * (np.sin(theta / 2) / np.sin(self.alpha / 2)) ** 2) * \
                   jn(0, v * (np.sin(theta) / np.sin(self.alpha))) * np.sin(theta) * (1 + np.cos(theta))
            return coeff * result

        return _integral
