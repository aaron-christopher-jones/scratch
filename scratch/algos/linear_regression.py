import numpy as np


class LinearRegression:
    """
    Solver: gradient descent.
    """

    def __init__(self, y, X, learning_rate, tol_err):
        """
        """
        self.y = y.reshape(len(y), 1)
        self.X = X
        self.n, self.m = X.shape
        self.learning_rate = learning_rate
        self.tol_err = tol_err

    def _func_loss(self, betas):
        """
        Calculate the loss function.

        Parameters
        ----------
        self : class object
            The class object containing all the key components
        
        betas : array
        """
        Z = self.y - np.dot(self.X, betas)
        return (1 / self.n) * np.dot(Z.T, Z)

    def _func_gradient(self, betas):
        """
        Evaluate the gradient. The 'i' input determines the coefficient against
        which the gradient is to be evaluated.

        Parameters
        ----------
        self : class object
            The class object containing all the key components

        betas : array
        """
        Z = self.y - np.dot(self.X, betas)
        return -(2 / self.n) * np.dot(self.X.T, Z)

    def fit(self):
        """
        Fit the model.

        Parameters
        ----------
        self : class object
            The class object containing all the key components
        """
        betas = np.array([0] * self.m).reshape(self.m, 1)
        lrs = np.array([self.learning_rate] * self.m).reshape(self.m, 1)
        mse = self._func_loss(betas=betas)

        while True:
            betas = betas - lrs * self._func_gradient(betas=betas)
            
            mse_old = mse
            mse = self._func_loss(betas=betas)

            err = abs(mse_old - mse)
            if err <= self.tol_err:
                break
        
        self.coefs = betas
        
    def predict(self, Xvalid):
        """
        Create predicted array given the inputted exogenous dataset.

        Parameters
        ----------
        self : class object
            The class object containing all the key components

        Xvalid : nd-array
            The exogenous data to produce the prediction
        """
        self.yhat = np.dot(Xvalid, self.coefs)
        return self.yhat