import numpy as np

def gradient_descent(x, y):
    m = c = 0
    iterations = 10000
    n = len(x)
    learning_rate = 0.01

    for i in range(iterations):
        y_pred = m * x + c
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])
        partial_m_derivative = -(2/n)*sum(x*(y-y_pred))
        partial_b_derivative = -(2/n)*sum(y-y_pred)
        m = m - learning_rate * partial_m_derivative
        c = c - learning_rate * partial_b_derivative
        print("m: {}, c: {}, cost: {}, iteration :{}".format(m , c, cost, i))

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 7, 9, 11, 13])

gradient_descent(x, y)