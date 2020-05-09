% Compensating for the system non-linearity is not always a good idea.
% Here, feedback linearization does much worse than simple feedback control
% that takes advantage of the natural system dynamics.

% Not that this function -x^3 is special in that it naturally drives us 
% towards our reference x_d = 0.
% If the function were x^3, it would have been advisable to cancel the
% non-linearity.

x0 = 10;
tspan = [0 10];
[t, x] = ode45(@free, tspan, x0);
gcf;
hold on;
plot(t, x, '-r');

[t, x] = ode45(@feedback, tspan, x0);
plot(t, x, '-b');

[t, x] = ode45(@feedback_linear, tspan, x0);
plot(t, x, '-g');


function [dxdt] = free(t, x)
    dxdt = -x*x*x;
end

function [dxdt] = feedback(t, x)
    Kp = 1;
    dxdt = -x*x*x - Kp*x;
end

function [dxdt] = feedback_linear(t, x)
    Kp = 1;
    dxdt = - Kp*x;
end