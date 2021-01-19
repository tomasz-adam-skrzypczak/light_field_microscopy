import unittest

import numpy as np
from sources.parameters import MicroParams, PSFParams
from sources.point_spread_function.wavefront_integral import WavefrontIntegral


class WavefrontIntegralTest(unittest.TestCase):

    def test_vectorized_evaluation(self):
        
        mc_param = MicroParams(0.0, 0.0, 0.0, 0, 1, 0.0, 399)
        psf_param = PSFParams(0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 
                               0.0, 0.0, 1.0, 0.0, 0.0 ,0.0)
        x_point = np.zeros((10, 2))
        x_point[:, 1] = np.arange(0.0, 10., 1.)
        p_source = np.array([0.0, 0.0, 135.0])
        theta = np.zeros((10, 1))
        test_range = np.arange(0, 1.0, 0.1).reshape(1, -1)

        # for i in range():
        print(x_point)
        integrals = WavefrontIntegral(mc_param, psf_param).get_integral(x_point, p_source)
        print(integrals(theta))
        # print(integral)
        # self.assertEqual(len(integral(test_range)), len(test_range))


if __name__ == "__main__":
    unittest.main()
