import pytest

def hp(h, *, rho = 1000, g = 9.81):
    """
    Computes the hydrostatic pressure acting on a submerged object given:
        - the height of fluid above the object, h
        - the density of the fluid in which is it submerged, rho
        - the acceleration due to gravity, g

    """
    if h < 0:
        raise ValueError("Height of fluid, h, must be greater than or equal to zero")
    if rho < 0:
        raise ValueError("Density of fluid, rho, must be greater than or equal to zero")
    if g < 0:
        raise ValueError("Acceleration due to gravity, g, must be greater than or equal to zero")

    return rho * g * h


#result = hp(-10)

#assert result == -10 * 1000 * 9.81


# Check that h < zero raises a ValueError
def test_hydrostatic_pressure_returns_error_if_h_less_then_0():
    with pytest.raises(ValueError):
        hp(-10)

def test_hydrostatic_pressure_returns_error_if_rho_less_then_0():
    with pytest.raises(ValueError):
        hp(10, rho=-10)

def test_hydrostatic_pressure_returns_error_if_g_less_then_0():
    with pytest.raises(ValueError):
        hp(10, g=-9.81)

 