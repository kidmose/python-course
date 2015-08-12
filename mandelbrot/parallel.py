from __future__ import division
"""Parallel implementation of mandelbrot calculator."""

import mandelbrot
import math
import numpy as np
import sys
from multiprocessing import Pool

logger = mandelbrot.get_logger(__name__)


class ParallelCalculator(mandelbrot.MandelbrotCalculator):
    """
    Parallel implementation of mandelbrot calculator.

    Changed to use numpy arrays to enable the parallelism.
    """
    file_name_data = "parallel_data.csv"
    file_name_plot = "parallel_plot.png"

    def calculate(self):
        """Implements dispatching functionality."""
        # calculate grid size and steps
        im_span = self.pim_max-self.pim_min
        im_step = im_span / self.Pim
        re_span = self.pre_max-self.pre_min
        re_step = re_span / self.Pre
        
        # calculate list of c values (flat list)
        re_s = [i*re_step + self.pre_min for i in range(self.Pre)]
        im_s = [i*im_step + self.pim_min for i in range(self.Pim)]
        c_s = [re+im*1j for im in im_s for re in re_s]

        pool = Pool(processes=self.n)
        results = pool.map(self.single_point_calculation, c_s)
        return [results[self.Pre*i : self.Pre*(i+1)] for i in range(self.Pim)] # unflatten

    def single_point_calculation(self, c):
        """
        Calculates the value for a single location.

        This is the method which is distributed, 
        along with the data, to each process.
        """
        i = 0
        z = 0+0j
        while math.sqrt(abs(z)) <= self.T and i < self.I:
            z = z**2 + c
            i += 1
        return i/self.I


# fix for old python versions (before 3) to enable pickling methods
# http://bytes.com/topic/python/answers/552476-why-cant-you-pickle-instancemethods
if sys.hexversion < 0x03000000: # prior to python 3
    def _pickle_method(method):
        func_name = method.im_func.__name__
        obj = method.im_self
        cls = method.im_class
        return _unpickle_method, (func_name, obj, cls)

    def _unpickle_method(func_name, obj, cls):
        for cls in cls.mro():
            try:
                func = cls.__dict__[func_name]
            except KeyError:
                pass
            else:
                break
        return func.__get__(obj, cls)

    import copy_reg
    import types
    copy_reg.pickle(types.MethodType, _pickle_method, _unpickle_method)
