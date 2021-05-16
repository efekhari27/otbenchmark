"""
Class to define the ReliabilityProblem22 benchmark problem.

@author: efekhari27
"""

from otbenchmark.CentralTendencyBenchmarkProblem import CentralTendencyBenchmarkProblem
import openturns as ot
import numpy as np


class CentralTendencyProblem22(CentralTendencyBenchmarkProblem):
    def __init__(self, mu=[0.5] * 2, sigma=[0.15] * 2):
        """
        Creates a central problem from the ReliabilityProblem22.

        The function is the following:

        g(x1, x2) = 2.5 - 1 / sqrt(2) * (x1 + x2) + 0.1 * (x1 - x2) ^ 2.

        We have x1 ~ Normal(mu[0], sigma[0]) and x2 ~ Normal(mu[1], sigma[1]).

        Parameters
        ----------
        mu : sequence of floats
            The list of two items representing the means of the gaussian distributions.

        sigma : float
            The list of two items representing the standard deviations of
            the gaussian distributions.
        
        Example
        -------
        problem  = CentralTendencyProblem22()
        """
        formula = "2.5 - 1 / sqrt(2) * (x1 + x2) + 0.1 * (x1 - x2) ^2"
        g = ot.SymbolicFunction(["x1", "x2"], [formula])
        inputDimension = len(mu)
        if inputDimension != 2:
            raise Exception(
                "The dimension of mu is %d, but the expected dimension is 2."
                % (inputDimension)
            )

        inputDimension = len(sigma)
        if inputDimension != 2:
            raise Exception(
                "The dimension of sigma is %d, but the expected dimension is 2."
                % (inputDimension)
            )
        X1 = ot.Normal(mu[0], sigma[0])
        X1.setDescription(["X1"])
        X2 = ot.Normal(mu[1], sigma[1])
        X2.setDescription(["X2"])

        myDistribution = ot.ComposedDistribution([X1, X2])
        inputRandomVector = ot.RandomVector(myDistribution)
        compositeRandomVector = ot.CompositeRandomVector(
            g, inputRandomVector
        )

        name = "CTP22"
        Yexact = 2.5 - 1 / np.sqrt(2) * (X1 + X2) + 0.1 * (X1 - X2) * (X1 - X2)
        mean = Yexact.getMean()[0]
        std = Yexact.getStandardDeviation()[0]

        super(CentralTendencyProblem22, self).__init__(name, compositeRandomVector, 
                                                        mean, std)
        return None
