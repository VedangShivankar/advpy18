import mathlib
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3,5),reason="I dont want to run this test at the moment")
def test_calc_total():
    total = mathlib.calc_total(4,5)
    assert total == 9

def test_clac_multiply():
    result =  mathlib.calc_multipy(10,3)
    assert result == 30 