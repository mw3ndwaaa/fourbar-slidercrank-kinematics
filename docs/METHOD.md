# Analysis method

## Four-bar linkage

The input crank endpoint is obtained directly from the input angle. The coupler/output joint is then found as the intersection of two circles:

- circle centered at the crank endpoint with radius equal to the coupler length;
- circle centered at the fixed output pivot with radius equal to the rocker length.

The two circle intersections correspond to the two assembly branches. This avoids relying on a single trigonometric branch and provides a direct geometric closure check.

## Slider-crank

For an inline slider-crank,

`x = r cos(theta) + sqrt(l^2 - r^2 sin^2(theta))`.

The implementation supports a full revolution when `l >= r`.
