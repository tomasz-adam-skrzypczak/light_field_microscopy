from sources.parameters import get_simulation_parameters
from sources.point_spread_function.wave_psf_estimator import WavePointSpreadFunctionEstimator    
# if __name__ == "__main__":
    
micro_params, psf_params = get_simulation_parameters("./data/test_psf.yml")
wpfs_estimator = WavePointSpreadFunctionEstimator(micro_params, psf_params)
wpfs_estimator._estimate_psf_size()
print("END")