#!/usr/bin/python
# coding:utf-8
# Copyright 2021 EDF
"""
Class to define a benchmark problem.

@author: efekhari27
"""

import openturns as ot


class CentralTendencyBenchmarkProblem:
    """Class to define a benchmark problem."""

    def __init__(self, name, compositeRandomVector, mean, std):
        """
        Create a central tendency problem.

        The essential information is the exact mean and standard deviation.
        It should be as accurate as possible.
        The best possible accuracy for a Python float is 53 significant
        (binary) bits, which approximately corresponds to 15-17 decimal digits.
        If this accuracy is not available, then a reference value may be used,
        for example from a large Monte-Carlo sample.

        In general, the exact mean should be a constant value,
        e.g. 0.123456789.
        However, we may be forced to compute this mean and standard deviation 
        at the creation of the problem, for example if the input distribution 
        of the problem can be set at the creation of the object.
        In this case, the unit test must check that the default value of the
        parameters correspond to a reference, constant, value.

        Parameters
        ----------
        name : str
            The name of the benchmark problem.
            This is a short string, typically less than a dozen of caracters.

        compositeRandomVector : ot.CompositeRandomVector
            The input random vector composed by the function.

        mean : float
            The exact mean.

        std : float
            The exact standard deviation.

        Example
        -------
        problem  = CentralTendencyBenchmarkProblem(name, compositeRandomVector,
                                                    mean, std)
        """
        self.name = name
        self.compositeRandomVector = compositeRandomVector
        self.mean = mean
        self.std = std

        return None

    def getRandomVector(self):
        """
        Return the RandomVector.

        Parameters
        ----------
        None.

        Returns
        -------
        event: ot.CompositeRandomVector
            The input random vector composed by the function.
        """
        return self.compositeRandomVector

    def getMean(self):
        """
        Return the mean.

        Parameters
        ----------
        None.

        Returns
        -------
        mean: float
            The mean of the composite random vector.
        """
        return self.mean
        
    def getStd(self):
        """
        Return the standard deviation.

        Parameters
        ----------
        None.

        Returns
        -------
        std: float
            The standard deviation of the composite random vector.
        """
        return self.std

    def getName(self):
        """
        Return the name of the problem.

        Parameters
        ----------
        None.

        Returns
        -------
        name: str
            The name of the problem.
        """
        return self.name

    def __str__(self):
        """
        Convert the object into a string.

        This method is typically called with the "print" statement.

        Parameters
        ----------
        None.

        Returns
        -------
        s: str
            The string corresponding to the object.
        """
        s = ("name = %s\n" "composite random vector = %s\n" "mean = %s\n" 
                    "standard deviation = %s\n") % (
            self.name,
            self.compositeRandomVector,
            self.mean,
            self.std,
        )
        return s

    def toFullString(self):
        """
        Convert the object into a string, with full details.

        Parameters
        ----------
        None.

        Returns
        -------
        s: str
            The string of the problem.
        """
        g = self.compositeRandomVector.getFunction()
        distribution = self.compositeRandomVector.getAntecedent().getDistribution()
        s = (
            "name = %s \n"
            "function = %s\n"
            "mean = %s\n"
            "standard deviation = %s\n"
            "distribution = %s"
        ) % (self.name, g, self.mean, self.std, distribution,)
        return s
