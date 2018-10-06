"""
Simple strange attractors simulation
"""

import numpy as np
from scipy.integrate import odeint
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

class Attractor:

    def __init__(self,x=0.1,y=0.1,z=0.1,dt=0.01):
        self.x = x
        self.y = y
        self.z = z
        self.t = np.arange(0,60,dt)
        self.ic = (x,y,z)

    def lorenz(self,ic,t,sigma=10,rho=28,beta=8/3):
        """
        https://en.wikipedia.org/wiki/Lorenz_system
        """
        x,y,z = ic
        dxdt = sigma*(y-x)
        dydt = x*(rho-z)-y
        dzdt = x*y - beta*z
        return [dxdt,dydt,dzdt]

    def rossler(self,ic,t,a=0.2,b=0.2,c=14):
        """
        https://en.wikipedia.org/wiki/R%C3%B6ssler_attractor
        """
        x,y,z = ic
        dxdt = -y-z
        dydt = x + a*y
        dzdt = b + z*(x-c)
        return [dxdt,dydt,dzdt]

    def luChen(self,ic,t,a=36,b=3,c=20,u=-15.15):
        """
        https://en.wikipedia.org/wiki/Multiscroll_attractor#Lu_Chen_attractor
        """
        x,y,z = ic
        dxdt = a*(y-x)
        dydt = x - x*z + c*y + u
        dzdt = x*y - b*z
        return [dxdt,dydt,dzdt]

    def modifiedLuChen(self,ic,t,a=35,b=3,c=28,d0=1,d1=1,d2=-20.20,tau=0.2):
        """
        https://en.wikipedia.org/wiki/Multiscroll_attractor#Modified_Lu_Chen_attractor
        """
        x,y,z = ic
        f = d0*z + d1*z*(t-tau) - d2*np.sin(z*(t-tau))
        dxdt = a*(y-x)
        dydt = (c-a)*x - x*f + c*y
        dzdt = x*y - b*z
        return [dxdt,dydt,dzdt]

    def modifiedChuaChaotic(self,ic,t,alpha=10.82,beta=14.286,a=1.3,b=0.11,c=7,d=0):
        """
        https://en.wikipedia.org/wiki/Multiscroll_attractor#Modified_Chua_chaotic_attractor
        """
        x,y,z = ic
        h = -b*np.sin((np.pi*x)/(2*a) + d)
        dxdt = alpha*(y-h)
        dydt = x-y+z
        dzdt = -beta*y
        return [dxdt,dydt,dzdt]

    def move(self,function):
        return odeint(function,self.ic,self.t)

    def plotXY(self,function):
        x = self.move(function)[:,0]
        y = self.move(function)[:,1]
        plt.plot(x,y)
        plt.show()

    def plotXZ(self,function):
        x = self.move(function)[:,0]
        z = self.move(function)[:,2]
        plt.plot(x,z)
        plt.show()
    
    def plotYZ(self,function):
        y = self.move(function)[:,1]
        z = self.move(function)[:,2]
        plt.plot(y,z)
        plt.show()

    def plotAll(self,function):
        pos = self.move(function)
        fig = plt.figure()
        ax = plt.axes(projection="3d")
        ax.plot3D(pos[:,0],pos[:,1],pos[:,2])
        plt.show()