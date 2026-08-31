import numpy as np
from mechanism_kinematics import FourBar


def test_four_bar_closure():
    mech = FourBar(0.06, 0.16, 0.12, 0.18)
    c = mech.solve(np.deg2rad(60), branch=1)
    assert np.isclose(np.linalg.norm(c.A - c.O2), mech.a)
    assert np.isclose(np.linalg.norm(c.B - c.A), mech.b)
    assert np.isclose(np.linalg.norm(c.B - c.O4), mech.c)
    assert np.isclose(np.linalg.norm(c.O4 - c.O2), mech.d)


def test_coupler_point_midpoint():
    mech = FourBar(0.06, 0.16, 0.12, 0.18)
    c = mech.solve(np.deg2rad(60))
    p = mech.coupler_point(c, along=0.5, offset=0.0)
    assert np.allclose(p, 0.5*(c.A+c.B))


def test_transmission_angle_is_physical():
    mech = FourBar(0.06, 0.16, 0.12, 0.18)
    c = mech.solve(np.deg2rad(60))
    mu = mech.transmission_angle(c)
    assert 0.0 <= mu <= np.pi
