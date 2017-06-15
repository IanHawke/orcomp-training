from numpy import sqrt, allclose

def quadratic(a2, a1, a0):
    """
    Compute the real roots of a2 x^2 + a1 x + a0 = 0.
    
    Parameters
    ----------
    
    a2 : real
        Coefficient of x^2
    a1 : real
        Coefficient of x^1
    a0 : real
        Coefficient of x^0
    
    Returns
    -------
    
    roots : list
        Empty if no real roots
    """
    
    if allclose(a2, 0): 
        if allclose(a1, 0): # It's got no unknown x
            roots = []
        else: # It's a linear equation
            roots = [-a0 / a1]
        return roots
    
    discriminant = a1**2 - 4 * a2 * a0
    
    if discriminant < 0: # Complex roots
        roots = []
    else: # Distinct real roots
        roots = [ ( sqrt(discriminant) - a1) / (2 * a2),
                  (-sqrt(discriminant) - a1) / (2 * a2) ]
    return roots