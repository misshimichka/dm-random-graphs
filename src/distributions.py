"""
Functions to generate samples from different distributions.
"""

from scipy.stats import skewnorm, expon
import numpy as np


def skewnormal_distribution(alpha: float, n: int, random_state: int = None) -> np.ndarray:
    """
    Fuction generate sample from skewnormal distribution.

    alpha: skewness parameter.
    n: number of values in sample.
    random_state: seed for random number generation.
    """

    return skewnorm.rvs(a=alpha, size=n, random_state=random_state)


def normal_distribution(s: float, n: int, rs: int = None) -> np.ndarray:
    """
    Fuction generate sample from skewnormal distribution.

    s: standard diviation parameter.
    n: number of values in sample.
    rs: seed for random number generation.
    """

    return np.random.normal(scale=s, size=n, random_state=rs)


def lognormal_distribution(s: float, n: int, rs: int = None) -> np.ndarray:
    """
    Fuction generate sample from skewnormal distribution.

    s: standard diviation parameter.
    n: number of values in sample.
    rs: seed for random number generation.
    """

    return np.random.lognormal(mean=0, sigma=s, size=n)


def exp_distribution(lmb: float, n: int, rs: int = None) -> np.ndarray:
    """
    Fuction generate sample from skewnormal distribution.

    lmd: rate parameter.
    n: number of values in sample.
    rs: seed for random number generation.
    """

    return expon.rvs(scale=1/lmb, size=n, random_state=rs)
