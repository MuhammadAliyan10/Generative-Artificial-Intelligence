import numpy as np
import pandas as pd
from sklearn import linear_model

df = pd.read_csv('../Data/test_scores.csv')

def getCofInt():
    math = df[['math']]
    cs = df['cs']
    reg = linear_model.LinearRegression()
    reg.fit(math, cs)
    return reg.coef_, reg.intercept_

def gradientDescent(x, y):
    m_current = b_current = 0
    iteration = 1000
    n = len(x)
    learning_rate = 0.0001
    for i in range(iteration):
        y_predicted = m_current * x + b_current
        m_derivative = -(2/n) * sum(x * (y - y_predicted))
        b_derivative = -(2/n) * sum(y - y_predicted)
        m_current =  m_current - learning_rate * m_derivative
        b_current =  b_current - learning_rate * b_derivative
    return m_current, b_current

if __name__== "__main__":
    x = np.array(df.math)
    y = np.array(df.cs)

    print("Gradient Descent")
    m, p = gradientDescent(x, y)
    print(f'Coefficient: {m}, Intercept: {p}')

    print("Linear Regression")
    e, g = getCofInt()
    print(f'Coefficient: {e}, Intercept: {g}')
