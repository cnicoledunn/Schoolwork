#!/usr/bin/env python3
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt

#choose center of distribution to be zero
N=200
data = np.random.normal(loc=0, scale=1, size=(N,2))

#Generates an N-vector of ones
y = np.ones(shape=N, dtype=int)
#Returns a True-False N-vector for where the product of the first and second columns of our data matrix are negative numbers
xprod = (data[:,0])*(data[:,1]) < 0
#Assigns each negative value of xprod a value of -1, and each positive value a value of +1
y[xprod] = -1

# perform a polynomial features transform of the dataset
trans = PolynomialFeatures(degree=2)
trans_data = trans.fit_transform(data)

#Perform linear regression
linreg = LinearRegression(copy_X=True, fit_intercept=True, normalize=False)
linreg.fit(trans_data, y)

def classified(linreg, data):
    """Creates a classifier for our polynomial least squares"""
    predictions=linreg.predict(data)
    predictions[predictions < 0] = -1
    predictions[predictions >= 0] = 1
    return predictions

#Polynomial least squares classifier; gives the error rate of our classifier
predictions=classified(linreg, trans_data)
print(np.sum(predictions != y)/len(predictions))

#Creates our grid
x = np.linspace(-4, 4, 200)
y = np.linspace(-4, 4, 200)
xv, yv = np.meshgrid(x, y)
positions = np.vstack([xv.ravel(), yv.ravel()]).T

#Classifies our gridpoints
trans = PolynomialFeatures(degree=2)
transformed_positions = trans.fit_transform(positions)
classified_positions=classified(linreg, transformed_positions)

#Generates our plots
plt.scatter(positions[:,0], positions[:,1], c=classified_positions)
plt.scatter(data[:,0], data[:,1], c=predictions, cmap='ocean_r')
plt.show()


