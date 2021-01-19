from typing import List
import numpy as np
from numpy.polynomial.legendre import leggauss


def integrate(integrals : np.array, no_nodes : int, interval : List[float]):

    nodes, weights = leggauss(no_nodes)
    
    start_interval = interval[0]
    end_interval = interval[1]

    shifted_nodes = 0.5 * ((end_interval - start_interval) * nodes + (end_interval - start_interval))     
    values = np.array([integral(shifted_nodes) for integral in integrals])

    result = 0.5 * (end_interval - start_interval) * (values * weights).sum(axis = 1)

    return result