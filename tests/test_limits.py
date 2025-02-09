import pytest
import numpy as np
from random import random

from yt_calculus.src.limit import compute_lateral_limit, compute_limit

TOL = 1e-10


def test_left_lateral_limit_quadratic_function():
    poly = lambda x: x**2
    limit = compute_lateral_limit(
        func=poly,
        x0=1,
        sign=-1,
    )

    assert abs(limit - 1) < TOL


def test_right_lateral_limit_quadratic_function():
    poly = lambda x: x**2
    limit = compute_lateral_limit(
        func=poly,
        x0=1,
    )

    assert abs(limit - 1) < TOL


def test_bilateral_lateral_limit_quadratic_function():
    poly = lambda x: x**2
    limit = compute_limit(
        func=poly,
        x0=1,
        tol=1e-10
    )

    assert abs(limit - 1) < TOL


def test_left_lateral_limit_trigonometric_function():
    trig = lambda x: np.sin(x)
    limit = compute_lateral_limit(
        func=trig,
        x0=np.pi,
        sign=-1,
    )

    assert abs(limit - 0) < TOL


def test_right_lateral_limit_trigonometric_function():
    trig = lambda x: np.sin(x)
    limit = compute_lateral_limit(
        func=trig,
        x0=np.pi,
    )

    assert abs(limit - 0) < TOL


def test_bilateral_lateral_limit_trigonometric_function():
    trig = lambda x: np.sin(x)
    limit = compute_limit(func=trig, x0=np.pi, tol=1e-30)

    assert abs(limit - 0) < TOL


def test_left_lateral_limit_trigonometric_fundamental_limit():
    trig = lambda x: np.sin(x) / x
    limit = compute_lateral_limit(
        func=trig,
        x0=0,
        sign=-1,
    )

    assert abs(limit - 1) < TOL


def test_right_lateral_limit_trigonometric_fundamental_limit():
    trig = lambda x: np.sin(x) / x
    limit = compute_lateral_limit(
        func=trig,
        x0=0,
    )

    assert abs(limit - 1) < TOL


def test_bilateral_lateral_limit_trigonometric_fundamental_limit():
    trig = lambda x: np.sin(x) / x
    limit = compute_limit(
        func=trig,
        x0=0,
    )

    assert abs(limit - 1) < TOL


def test_right_lateral_limit_log():
    func = lambda x: x * np.log(x)
    limit = compute_lateral_limit(
        func=func,
        x0=0,
    )

    assert abs(limit - 0) < TOL


def test_lateral_limits_exists_but_are_different():
    func = lambda x: x**2 - x if x < 0 else np.exp(x)

    right = compute_lateral_limit(func=func, x0=0, sign=1)
    left = compute_lateral_limit(func=func, x0=0, sign=-1)

    assert abs(right - 1) < TOL
    assert abs(left - 0) < TOL


def test_lateral_limits_exists_but_are_different_raises_exception():
    func = lambda x: x**2 - x if x < 0 else np.exp(x)

    with pytest.raises(
        ValueError,
        match="Bilateral limit does not exists: right limit and left limit are different",
    ):
        _ = compute_limit(
            func=func,
            x0=0,
        )


def test_limit_bounded_random_function():
    func = lambda x: (np.sin(3 * x) if random() > 0.5 else x**2 + x)
    limit = compute_limit(
        func=func,
        x0=0,
    )

    assert abs(limit - 0) < TOL


def test_limit_discontinuous_function():
    func = lambda x: x + np.tan(x) if x != 0 else np.pi + np.e
    limit = compute_limit(
        func=func,
        x0=0,
    )

    assert abs(limit - 0) < TOL
    