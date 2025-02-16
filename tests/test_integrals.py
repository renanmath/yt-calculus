import numpy as np
import pytest

from yt_calculus.src.integral import compute_riemann_integral


TOL = 1e-6

def test_riemann_integral_linear_function():
    linear_func = lambda x:x
    value = compute_riemann_integral(
        func=linear_func,
        interval=(0,3)
    )

    assert abs(value - 9/2) < TOL

def test_riemann_integral_quadratic_function():
    quadratic_func = lambda x:x**2 + 1
    value = compute_riemann_integral(
        func=quadratic_func,
        interval=(0,1)
    )

    assert abs(value - 4/3) < TOL

def test_riemann_integral_odd_function_in_symmetrical_interval():
    cubic_func = lambda x:x**3 - 2*x
    value = compute_riemann_integral(
        func=cubic_func,
        interval=(-1,1),
    )

    assert abs(value - 0) < TOL

def test_riemann_integral_cosine_function():
    trig_func = lambda x:np.cos(x)
    value = compute_riemann_integral(
        func=trig_func,
        interval=(np.pi/2,np.pi)
    )

    assert abs(value + 1) < TOL

def test_riemann_integral_exponential_function():
    exp_func = lambda x:np.exp(x)
    value = compute_riemann_integral(
        func=exp_func,
        interval=(0,np.log(3))
    )

    assert abs(value - 2) < TOL

def test_riemann_integral_logarithm_function():
    log_func = lambda x:np.log(x)
    value = compute_riemann_integral(
        func=log_func,
        interval=(1,np.e**2)
    )

    assert abs(value - np.e**2 - 1) < TOL

def test_riemann_integral_rational_function():
    rational_func = lambda x: 1 / (x+1)
    value = compute_riemann_integral(
        func=rational_func,
        interval=(1,2)
    )

    assert abs(value - np.log(3/2)) < TOL

def test_riemann_integral_cosine_identity_01():
    rational_func = lambda x: np.cos(x)**2
    value = compute_riemann_integral(
        func=rational_func,
        interval=(0,np.pi)
    )

    assert abs(value - np.pi/2) < TOL

def test_riemann_integral_cosine_identity_02():
    rational_func = lambda x: np.cos(2*x)*np.cos(3*x)
    value = compute_riemann_integral(
        func=rational_func,
        interval=(0,np.pi)
    )

    assert abs(value - 0) < TOL


def test_riemann_integral_sophomore_dream_01():
    func = lambda x: x**(-x)
    value = compute_riemann_integral(
        func=func,
        interval=(0,1)
    )

    assert abs(value - 1.29128599706266) < TOL


def test_riemann_integral_sophomore_dream_02():
    func = lambda x: x**x
    value = compute_riemann_integral(
        func=func,
        interval=(0,1)
    )

    assert abs(value - 0.78343051071213) < TOL
