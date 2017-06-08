from numpy.testing import assert_equal, assert_allclose
import pytest

def divide(x, y):
    """
    Divide two numbers
    
    Parameters
    ----------
    
    x : float
        Numerator
    y : float
        Denominator
    
    Returns
    -------
    
    x / y : float
    """
    return x / y
    
def test_integer_division():
    assert_equal(divide(4, 2), 2, 
                 err_msg="Dividing 4 by 2: answer should be 2")
    
def test_real_division1():
    assert_allclose(divide(1, 3), 0.33333333333333, 
                 err_msg="Dividing 1 by 3: answer should be 1/3")

def test_power_division():
    a = 1.234
    assert_allclose(divide(a**7, a), a**6, 
                 err_msg="Dividing a^7 by a: answer should be a^6")

def test_large_division():
    assert_equal(divide(1, 1e1000), 0,
                 err_msg="Dividing by a large enough number returns zero")
                 
def test_zero_division():
    with pytest.raises(ZeroDivisionError, 
                       message="Dividing by zero should give a ZeroDivisionError"):
        divide(1, 0)
        
# The following command will run when the file is executed:

pytest.main()
