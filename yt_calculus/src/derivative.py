
from yt_calculus.constants import DEFAULT_TOLERANCE
from yt_calculus.src.limit import compute_limit


def derive_function(func:callable, x0: float, tol:float=DEFAULT_TOLERANCE, max_iter:int=1000):
    func_expr = lambda x: (func(x) - func(x0)) / (x - x0)
    try:
        derivative = compute_limit(func_expr, x0, tol,max_iter)
        return derivative
    except ValueError:
        raise ValueError(f"Could not differentiate function at point {x0}")