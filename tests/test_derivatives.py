import numpy as np
import pytest

from yt_calculus.src.derivative import derive_function



TOL = 1e-10


def test_derivative_quadratic_function():
    quadratic = lambda x: x**2 + x

    value = derive_function(func=quadratic, x0=0, tol=1e-30)

    assert abs(value - 1) < TOL

def test_derivative_polynomial_function():
    quadratic = lambda x: x**5 - 2*x**4 + 3*x**3 - 4*x**2 + 5*x - 6

    value = derive_function(func=quadratic, x0=1,tol=1e-6)

    assert abs(value - 3) < TOL


def test_derivative_sine_function():
    trig = lambda x: np.sin(2 * x)

    value = derive_function(
        func=trig,
        x0=0,
    )

    assert abs(value - 2) < TOL


def test_derivative_tan_function():
    trig = lambda x: np.tan(x)

    value = derive_function(func=trig, x0=np.pi / 6)

    assert abs(value - 4 / 3) < TOL

def test_derivative_log_function():
    log_func = lambda x: np.log(x)

    value = derive_function(func=log_func, x0=13,tol=1e-8)

    assert abs(value - 1/13) < TOL

def test_derivative_sqrt_function():
    sqrt_func = lambda x: np.sqrt(x)

    value = derive_function(func=sqrt_func, x0=2,tol=1e-8)

    assert abs(value - np.sqrt(2)/4) < TOL

def test_derivative_product_function():
    func = lambda x: (x**2)*np.log(x)

    value = derive_function(func=func, x0=np.e,tol=1e-7)

    assert abs(value - 3*np.e) < 100*TOL

def test_derivative_quotient_function():
    func = lambda x: x/np.exp(x)

    value = derive_function(func=func, x0=0,tol=1e-30)

    assert abs(value - 1) < TOL

def test_derivative_composite_function_01():
    func = lambda x: np.exp(np.sin(x))

    value = derive_function(func=func, x0=0,tol=1e-6)

    assert abs(value - 1) < TOL

def test_derivative_composite_function_02():
    func = lambda x: np.sin(np.pi*np.exp(x))

    value = derive_function(func=func, x0=np.log(2),tol=1e-7)

    assert abs(value - 2*np.pi) < 100*TOL

def test_module_function_is_not_differentiable():
    mod_func = lambda x: abs(x)
    with pytest.raises(ValueError, match="Could not differentiate function"):
        derive_function(func=mod_func, x0=0)

def test_discontinuous_function_is_not_differentiable():
    
    discontinuous_func = lambda x: x**2 if x != 0 else 1
    with pytest.raises(ValueError, match="Could not differentiate function"):
        derive_function(func=discontinuous_func, x0=0, tol=1e-6)