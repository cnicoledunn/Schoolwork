#!/usr/bin/env python3
import numpy as np

#################### Function Definitions ######################

def least_squares_approximate(matrix, vector):
    """Returns the least squares approximate solution to a least squares problem in the format Ax=b"""
    #First compute pseudoinv (pseudo-inverse of "matrix"):
    pseudoinv = np.linalg.pinv(matrix, rcond=1e-15)
    #Then take the matrix product pseudoinv*vector to get our approximate solution ("approxsol"):
    approxsol = np.dot(pseudoinv, b)
    return approxsol

def residual_norm_squared(matrix, solution, vector):
    """Returns the residual norm squared for a given solution and least squares problem"""
    #First calculate the residual & store as "residual":
    residual = np.dot(matrix, solution) - vector
    #Then calculate the square of the 2-norm of our residual & store as "normsquared":
    normsquared = np.linalg.norm(residual)**2
    return normsquared


def smallest_residual(matrix, solution, vector, resnorm):
    """Verifies whether a given solution is indeed the smallest residual by verifying the inequality with three random 10-vectors"""
    #Generate three random 10-vectors; store as r, s, t:
    r = np.random.rand(10, 1)
    s = np.random.rand(10, 1)
    t = np.random.rand(10, 1)
    if residual_norm_squared(matrix, solution+r, vector)>resnorm:
        if residual_norm_squared(matrix, solution+s, vector)>resnorm:
            if residual_norm_squared(matrix, solution+t, vector)>resnorm:
                return True


#Generate a random 30x10 matrix A
A = np.random.rand(30, 10)
#and a random 30-vector B (expressed as a column vector)
b = np.random.rand(30, 1)

#Store the least squares approximate solution for A, b as "x"
x=least_squares_approximate(A, b)
#and store the associated residual norm squared as "resnorm"
resnorm=residual_norm_squared(A, x, b)

print(f"Our least squares approximate solution is the 10-vector x = {x}")
print(f"The associated norm squared is {resnorm}")

if smallest_residual(A, x, b, resnorm):
    print("We conclude our approximation has the smallest associated residual norm because the inequality holds for three random 10-vectors r, s, t")






