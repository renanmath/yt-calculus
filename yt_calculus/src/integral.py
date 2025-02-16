import numpy as np


def compute_function_in_interval(
    func: callable, interval: tuple[float, float], step: float
):
    num = int((interval[1] - interval[0]) / step)
    x_values = np.linspace(interval[0], interval[1], num)
    v_func = np.vectorize(func)
    y_values = v_func(x_values)

    return y_values


def compute_riemann_integral(
    func: callable, interval: tuple[float, float], step: float = 1e-6
):
    y_values = compute_function_in_interval(func=func, interval=interval, step=step)
    integral_value = np.sum(y_values*step)
    return integral_value


