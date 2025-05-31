"""
Functions to generate samples from different distributions.
"""
from typing import Optional, Union

from scipy.stats import skewnorm
import numpy as np


def skewnormal_distribution(
    alpha: float, n_values: int, random_state: Optional[int] = None
) -> Union[float, np.ndarray]:
    """
    Fuction generate sample from skewnormal distribution.

    alpha: skewness parameter.
    n_values: number of values in sample.
    random_state: seed for random number generation.
    """

    return skewnorm.rvs(a=alpha, size=n_values, random_state=random_state)


def normal_distribution(std: float, n_values: int) -> Union[float, np.ndarray]:
    """
    Fuction generate sample from normal distribution.

    std: standard diviation parameter.
    n_values: number of values in sample.
    """

    return np.random.normal(scale=std, size=n_values)


def lognormal_distribution(std: float, n_values: int) -> Union[float, np.ndarray]:
    """
    Fuction generate sample from lognormal distribution.

    std: standard diviation parameter.
    n_values: number of values in sample.
    """

    return np.random.lognormal(mean=0, sigma=std, size=n_values)


def exp_distribution(lmb: float, n_values: int) -> Union[float, np.ndarray]:
    """
    Fuction generate sample from skewnormal distribution.

    lmd: rate parameter.
    n_values: number of values in sample.
    """

    return np.random.exponential(lmb, n_values)
