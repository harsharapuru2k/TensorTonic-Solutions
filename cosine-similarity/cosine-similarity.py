import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    num= np.array(a)@np.array(b)
    
    if num:
        den=np.linalg.norm(a)*np.linalg.norm(b)
    else:
        return 0.0

    return float(num/den)