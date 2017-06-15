from numpy.testing import assert_equal, assert_allclose
import pytest
from quadratic import quadratic
    
def test_distinct_real():
    assert_allclose(quadratic(1, 0, -1), [1, -1], 
                    err_msg="Roots of x^2 - 1 = 0 should be [1, -1]")
    
def test_repeated_real_trivial():
    assert_allclose(quadratic(1, 0, 0), [0, 0], 
                    err_msg="Roots of x^2 = 0 should be [0, 0]")

def test_repeated_real_nontrivial():
    assert_allclose(quadratic(4, -4, 1), [0.5, 0.5], 
                    err_msg="Roots of (2 x - 1)^2 = 0 should be [1/2, 1/2]")

def test_complex():
    assert_equal(quadratic(1, 0, 1), [],
                 err_msg="Roots of x^2 + 1 = 0 should be [], empty list")

def test_linear():
    assert_allclose(quadratic(0, 1, -1), [1],
                    err_msg="Roots of 0 x^2 + x - 1 = 0 should be [1]")

def test_inconsistent():
    assert_equal(quadratic(0, 0, 1), [],
                 err_msg="Roots of 0 x^2 + 0 x + 1 = 0 should be [], empty list")
    
# The following command will run when the file is executed:

pytest.main()
