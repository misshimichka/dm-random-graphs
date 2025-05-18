"""
Functions to generate samples from different distributions.
"""

from scipy.stats import skewnorm, lognorm, expon
import numpy as np

def skewnormal_distribution(alpha: float, n: int, random_state: int = None) \
    -> np.ndarray:
    """
    Fuction generate sample from skewnormal distribution.

    alpha: skewness parameter.
    n: number of values in sample.
    random_state: seed for random number generation.
    """
    
    return skewnorm.rvs(a=0, size=n, random_state=random_state)

def normal_distribution(sigma: float, n: int, random_state: int = None) \
    -> np.ndarray:
    """
    Fuction generate sample from skewnormal distribution.

    sigma: standard diviation parameter.
    n: number of values in sample.
    random_state: seed for random number generation.
    """
    
    return np.random.normal(scale=sigma, size=n, random_state=random_state)

def lognormal_distribution(sigma: float, n: int, random_state: int = None) \
    -> np.ndarray:
    """
    Fuction generate sample from skewnormal distribution.

    sigma: standard diviation parameter.
    n: number of values in sample.
    random_state: seed for random number generation.
    """
    
    return lognorm.rvs(scale=sigma, size=n, random_state=random_state)

def exp_distribution(lambda_: float, n: int, random_state: int = None) \
    -> np.ndarray:
    """
    Fuction generate sample from skewnormal distribution.

    lambda: rate parameter.
    n: number of values in sample.
    random_state: seed for random number generation.
    """
    
    return expon.rvs(scale=1/lambda_, size=n, random_state=random_state)
