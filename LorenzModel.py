"""
Lorenz Model
"""

import numpy as np
import matplotlib.pyplot as plt

def move(dt):
    t = np.arange(0,60,dt)

    x = np.zeros(len(t))
    y = np.zeros(len(t))
    z = np.zeros(len(t))

    # initial conditions
    x[0] = 1

    # constants
    sigma = 10
    b = 8/3
    r = 25 # this value yung nagbibigay ng chaos sa pagkakaintindi ko

    for i in range(len(t)-1):
        x[i+1] = x[i] + (sigma*(y[i]-x[i]))*dt
        y[i+1] = y[i] + (-x[i]*z[i] + r*x[i] - y[i])*dt
        z[i+1] = z[i] + (x[i]*y[i] - b*z[i])*dt

    plt.plot(x, z)
    plt.show()

    return None
    
def main():
    TIME_STEP = 0.0001
    move(TIME_STEP)
    return None

if __name__ == "__main__":
    main()



