import numpy as np

from yt_calculus.constants import DEFAULT_TOLERANCE

def compute_lateral_limit(
    func: callable,
    x0: float,
    sign: float = 1,
    tol: float = DEFAULT_TOLERANCE,
    max_iter: int = 1000,
):
    
    y_prev = func(x0 + 1)
    n = 1
    max_tol = min(tol**2, 1e-100)

    while True:
        
        if n > max_iter:
            raise ValueError("Algorithm reached max iterations before converge")
        
        xn = x0 + sign*np.exp(-n)

        if abs(xn - x0) < max_tol:
            return y_prev # y_(n-1)
        
        yn = func(xn)
        if abs(yn - y_prev) < tol:
            return yn
        else:
            n += 1
            y_prev = yn

def compute_limit(
    func: callable,
    x0: float,
    tol: float = DEFAULT_TOLERANCE,
    max_iter: int = 1000,
):
    left_limit = compute_lateral_limit(func, x0, -1, tol, max_iter)
    right_limit = compute_lateral_limit(func, x0, 1, tol, max_iter)

    if abs(left_limit - right_limit) < np.sqrt(tol):
        return (left_limit + right_limit) / 2
    else:
        raise ValueError(
            "Bilateral limit does not exists: right limit and left limit are different"
        )
