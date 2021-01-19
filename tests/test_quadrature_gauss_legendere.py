from sources.point_spread_function.integration_methods.quadrature_gauss_legendere import integrate
import numpy as np
import unittest


class TestQuadratureGaussLegendere(unittest.TestCase):

    def test_integrate_shape(self):

        integrals = np.array([
            lambda x : x + 1, lambda x : x + 2
        ])
        result = integrate(integrals, 10, [0.0, 2.0])
        
        self.assertEqual(result.shape, (2, ))
        self.assertEqual(tuple(result), (4, 6.))

if __name__ == "__main__":
    unittest.main()