import numpy as np
from mechanism_kinematics import SliderCrank


def test_slider_crank_dead_centers():
    sc = SliderCrank(0.04, 0.14)
    assert np.isclose(sc.position(0.0), 0.18)
    assert np.isclose(sc.position(np.pi), 0.10)
    assert np.isclose(sc.position(0.0) - sc.position(np.pi), 0.08)
