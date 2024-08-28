import numpy as np

def gradientDescent(x: list[int], y:list[int])-> None:
    m_current = b_current = 0
    iteration = 1000
    n = len(x)
    learning_rate = 0.001
    for i in range(iteration):
        y_predicted = m_current * x + b_current # y = mx + b
        cost = (1/n) * sum([val ** 2 for val in (y - y_predicted)])
        m_derivative = -(2/n) * sum(x * (y - y_predicted))
        b_derivative = -(2/n) * sum(y - y_predicted)
        m_current =  m_current - learning_rate * m_derivative
        b_current =  b_current - learning_rate * b_derivative
        print(f"m {m_current} b {b_current} cost {cost} iteration {i}")

# We are using numpy array because its fast.
x : list[int] = np.array([1,2,3,4,5])
y : list[int] = np.array([5,7,9,11,13])
gradientDescent(x,y)
