clear; clc; close all;
r = 0.04; l = 0.14;
theta = linspace(0,2*pi,361);
x = r*cos(theta) + sqrt(l^2 - (r*sin(theta)).^2);
plot(rad2deg(theta),x*1000,'LineWidth',1.5); grid on;
xlabel('Crank angle [deg]'); ylabel('Slider position [mm]');
title('Slider-Crank Position Analysis');
