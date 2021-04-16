# simulating least-square method for f(x)=x^2

import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera

fig, ax = plt.subplots()
ax.set_xlim([0,6])
camera = Camera(fig)

# defining x range and y=f(x)
x = np.linspace(0, 8, 8001)
y = x**2
z = x - x + 9

# finding y' at x = p
def deriv(p, x, f):
    n = int(round(p/(8/(len(x)-1))))
    val = y[n]
    return ((f[n+1]-f[n]) + (y[n]-y[n-1]))/(2*(8/(len(x)-1)))

# equation of tangent
def solve_for_x(slope, m):
    if m<=3:
        return ((0,(m**2-slope*m)), ((((9-m**2)*1.0/slope)+m), 9))
    elif m>3:
        return (((((9-m**2)*1.0/slope)+m), 9), (6, (slope*(6-m)+m**2)))

# animating
# we start by taking m_0 = 1, and the final value to reach is 3 (i.e. f(x) = 9)

m = 1
for i in range(5):
    slope = deriv(m, x, y)
    (p1, p2) = solve_for_x(slope, m)
    m_n = ((9-m**2)*1.0/slope)+m
    for j in range(3):
        if j%3 == 0:
            ax.plot((m,m), (0, m**2), 'ro-')
            ax.plot(x, y, 'g-', x, z, 'k--')
            ax.legend([f'Iteration-{i+1}, m_{i}'])
            ax.set_title('Solution of f(x)=x^2=9')
            camera.snap()
        elif j%3 == 1:
            ax.plot(x, y, 'g-', x, z, 'k--')
            ax.plot((m,m), (0, m**2), 'ro-')
            ax.plot((p1[0],p2[0]), (p1[1],p2[1]), 'k-')
            ax.set_title('Solution of f(x)=x^2=9')
            camera.snap()
        elif j%3 == 2:
            ax.plot(x, y, 'g-', x, z, 'k--')
            ax.plot((m,m), (0, m**2), 'ro-')
            ax.plot((p1[0],p2[0]), (p1[1],p2[1]), 'k-', (m_n,m_n), (0,9), 'bo-')
            ax.set_title('Solution of f(x)=x^2=9')
            camera.snap()
    m = m_n


animation = camera.animate(interval= 2500, repeat= True, repeat_delay = 5000)
animation.save('new1.gif')
