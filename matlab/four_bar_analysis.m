% Four-bar position analysis using circle-circle intersection
clear; clc; close all;
a = 0.06; b = 0.16; c = 0.12; d = 0.18;
theta2 = deg2rad(linspace(15,165,301));
theta4 = nan(size(theta2));
for k = 1:numel(theta2)
    A = [a*cos(theta2(k)); a*sin(theta2(k))];
    O4 = [d;0];
    delta = O4-A; e = norm(delta);
    x = (b^2-c^2+e^2)/(2*e);
    h2 = b^2-x^2;
    if h2 < 0, continue; end
    h = sqrt(max(0,h2));
    ex = delta/e; ey = [-ex(2); ex(1)];
    B = A + x*ex + h*ey;
    theta4(k) = atan2(B(2),B(1)-d);
end
plot(rad2deg(theta2),rad2deg(unwrap(theta4)),'LineWidth',1.5);
grid on; xlabel('Input angle 	heta_2 [deg]'); ylabel('Output angle 	heta_4 [deg]');
title('Four-Bar Input-Output Relationship');
