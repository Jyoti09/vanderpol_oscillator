import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

nu = 0.2

def van_der_pol_oscillator_deriv(x, t):
    """ Function to calculate the vander pol oscillator
    derivate
    
    Take two arguments x,t
    argument x contains the initial condition vector
    argument t is the time
    """
    
    x1 = x[1]
    y = -nu * (x[0] ** 2.0 - 1.0) * x[1] - x[0]
    result = np.array([x1, y])
    return result

t = np.linspace(0.0, 50.0, 500)

soln_x = odeint(van_der_pol_oscillator_deriv, [0.2, 0.2], t)
plt.plot(soln_x[:,0], soln_x[:,1],color = 'red',linestyle = 'dashed',linewidth = 1.5,
marker='o', markerfacecolor='blue',markersize=2)


soln_x = odeint(van_der_pol_oscillator_deriv, [-3.0, -3.0],t)
plt.plot(soln_x[:,0], soln_x[:,1],color = 'blue',linestyle = 'solid',linewidth = 1.5)


xlabel_font = {'fontname':'Helvetica','fontsize':20}
ylabel_font = {'fontname':'Helvetica','fontsize':20}
title_font = {'fontname':'Helvetica','fontsize':20}

plt.xlabel('x',xlabel_font)
plt.ylabel('y',ylabel_font)
plt.title('Plot for phase cycle',title_font)
plt.legend(('x','y'),loc=2,fontsize=20)

plt.gca().set_aspect('equal')
plt.savefig('vanderpol_cycle.png')
plt.grid()

xx = soln_x[:,0]
yy = soln_x[:,1]

plt.figure(2)
plt.plot(t,xx,color = 'red',linestyle = 'solid',linewidth = 1.5,
         marker = 'o',markerfacecolor = 'blue',markersize = 2)
plt.plot(t,yy,color = 'blue',linestyle = 'solid',linewidth = 1.5,
         marker = 'D',markerfacecolor = 'red',markersize = 2)


xlabel_font = {'fontname':'Helvetica','fontsize':20}
ylabel_font = {'fontname':'Helvetica','fontsize':20}
title_font = {'fontname':'Helvetica','fontsize':20}

plt.xlabel('x',xlabel_font)
plt.ylabel('y',ylabel_font)
plt.title('Plot for phase cycle',title_font)
plt.legend(('x','y'),loc='lower right',fontsize=20)
plt.grid()
plt.savefig('vanderpol_input.png')
plt.show() 
