import numpy as np
from sources.point_spread_function.wavefront_integral import WavefrontIntegral
from sources.point_spread_function.integration_methods.quadrature_gauss_legendere import integrate


class WavePointSpreadFunctionEstimator:

    def __init__(self, microscope_params, psf_params):
        self.wavefront_integral = WavefrontIntegral(microscope_params, psf_params)
        self.microscope_params = microscope_params
        self.psf_params = psf_params

    def _estimate_psf_size(self):
        subvpix = self.psf_params.vpix * self.psf_params.osr
        print(self.psf_params)
        subpixel_pitch = self.psf_params.subpixel_pitch

        tmp = subpixel_pitch * np.arange(0, subvpix * 20, 1)
        test_space = np.zeros((tmp.shape[0], 2))
        test_space[:, 1] = tmp

        depth_space = np.arange(self.psf_params.zmin, self.psf_params.zmax, self.psf_params.zspacing)

        source_point = np.array([0, 0, np.max(np.abs(depth_space))])
        

        integral = self.wavefront_integral.get_integral()
        print(integral(test_space[0]))
        # line_projection = self.wavefront_integral.get_integral()
        # self._calculate_wavefron_at_nip(source_point, space)
        # line_projection = np.abs(line_projection ** 2)
        # line_projection = line_projection / np.max(line_projection)

        # threshold_mask = line_projection < 0.1
        # if np.sum(threshold_mask) == 0:
        #     raise Exception
        # else:
        #     print(threshold_mask.argmax())

    def estimate(self):
        pass
