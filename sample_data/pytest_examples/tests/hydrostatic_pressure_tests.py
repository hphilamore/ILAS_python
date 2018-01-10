import pytest
import sys
import os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../program')

import hydrostatic_pressure_program
from hydrostatic_pressure_program import *


def test_hydrostatic_pressure_returns_error_if_h_less_then_0():
    with pytest.raises(ValueError):
        hp(-10)

def test_hydrostatic_pressure_returns_error_if_rho_less_then_0():
    with pytest.raises(ValueError):
        hp(10, rho=-10)

def test_hydrostatic_pressure_returns_error_if_g_less_then_0():
    with pytest.raises(ValueError):
        hp(10, g=-9.81)

 