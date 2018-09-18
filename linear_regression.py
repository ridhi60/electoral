import numpy as np
import pandas as pd
from collections import deque
import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
def len_reg(x,y):
    n = len(x)
    sigma_x = np.sum(x)
    sigma_xsq = np.sum(x ** 2)
    sigma_y = np.sum(y)
    sigma_xy = np.sum(x * y)
    A = np.array([[n, sigma_x], [sigma_x, sigma_xsq]])
    B = np.array([[sigma_y], [sigma_xy]])
    sol = np.linalg.solve(A, B)
    # print(n, sigma_x, sigma_xsq, sigma_xy, sigma_y)
    print(sol)

    x_values = x
    y_values = deque(map(lambda b: sol[0] + sol[1] * b, x_values))
    # print(y_values[0:100])
    plt.plot(x_values, y_values)
    plt.scatter(x, y)
    plt.xlabel("% of economic class")
    plt.ylabel("Vote gained")
    plt.show()

