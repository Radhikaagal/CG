from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import bezier
import matplotlib.pyplot as plt
import numpy as np
#import seaborn

'''nodes1 = np.asfortranarray([
     [0.0, 0.5, 1.0],
     [0.0, 1.0, 0.0],
])
curve1 = bezier.Curve(nodes1, degree=2)'''

nodes2 = np.asfortranarray([
     [0.0, 0.25,  0.5, 0.75, 1.0],
     [0.0, 2.0 , -2.0, 2.0 , 0.0],
])
curve2 = bezier.Curve.from_nodes(nodes2)
print(curve2)
'''intersections = curve1.intersect(curve2)
intersections
array([[0.31101776, 0.68898224, 0. , 1. ],
       [0.31101776, 0.68898224, 0. , 1. ]])
s_vals = np.asfortranarray(intersections[0, :])
points = curve1.evaluate_multi(s_vals)'''


#seaborn.set()
ax = curve2.plot(num_pts=256)
#_ = curve2.plot(num_pts=256, ax=ax)
'''lines = ax.plot(
     points[0, :], points[1, :],
     marker="o", linestyle="None", color="black")
_ = ax.axis("scaled")
_ = ax.set_xlim(-0.125, 1.125)
_ = ax.set_ylim(-0.0625, 0.625)'''
plt.show()
