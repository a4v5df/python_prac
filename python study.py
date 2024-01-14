import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=np.linspace(-3,3,21)
y=np.linspace(-3,3,21)
z=np.linspace(-3,3,21)
X,Y,Z=np.meshgrid(x,y,z)
#plt.quiver(X,Y,Y**2,np.ones_like(X))
#plt.quiver(X,Y,-(X**2+Y**2),np.zeros_like(X))
#plt.quiver(X,Y,np.cos(X),np.sin(Y))


plt.quiver(X,Y,Z,np.cosh(X),np.sinh(Y),np.zeros_like(z))
#plt.quiver(X,Y,X,np.cosh(X))


plt.grid()
plt.show()

