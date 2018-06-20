# Lorenz Model

using PyPlot

function move(dt)
    t = collect(0:dt:60)

    x = zeros(length(t))
    y = zeros(length(t))
    z = zeros(length(t))

    # initial conditions
    x[1] = 1

    # constants
    sigma = 10
    b = 8/3
    r = 25

    for i in collect(1:1:length(t)-1)
        x[i+1] = x[i] + (sigma*(y[i]-x[i]))*dt
        y[i+1] = y[i] + (-x[i]*z[i] + r*x[i] - y[i])*dt
        z[i+1] = z[i] + (x[i]*y[i] - b*z[i])*dt
    end

    plot(x,z)
    show()
end

TIME_STEP = 0.0001
move(TIME_STEP)