
import numpy as np


def sin_model(t, a, b, c, d):
    return a * np.sin(b * t + c) + d


def exp_model(t, a, b, c):
    return a * np.exp(b * t) + c


def log_model(t, a, b, c, d):
    return a * np.log(b * t + c + 0.000001) + d


def power_model(t, a, b, c, d, e):
    return a * np.power(b * t + c, d) + e


def even_poly_model(t, a, b, c, d, e):
    return (
        a * np.power(t, 4) +
        b * np.power(t, 3) +
        c * np.power(t, 2) +
        d * t + e
    )


def odd_poly_model(t, a, b, c, d):
    return (
        a * np.power(t, 3) +
        b * np.power(t, 2) +
        c * np.power(t, 1) + d
    )
