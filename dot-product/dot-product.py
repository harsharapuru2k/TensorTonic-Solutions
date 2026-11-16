import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    # Write code her

    return float(sum(xi*yi for xi,yi in zip(x,y)))