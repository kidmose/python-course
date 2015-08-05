import mandelbrot
import math
import numpy as np
from multiprocessing import Pool

logger = mandelbrot.get_logger(__name__)


class ParallelCalculator(mandelbrot.MandelbrotCalculator):
    file_name_data = "parallel_data.csv"
    file_name_plot = "parallel_plot.pdf"

    def calculate(self):

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
        """Calculates the value for a single location"""
        i = 0
        z = 0+0j
        while math.sqrt(abs(z)) <= self.T and i < self.I:
            z = z**2 + c
            i += 1
        return i/self.I
