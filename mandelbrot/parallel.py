import mandelbrot
import math
import numpy as np

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
        
        # Create grids for results and c values
        results = np.zeros([self.Pim, self.Pre])
        c_s = np.zeros([self.Pim, self.Pre], dtype=complex)
        for i_im in range(self.Pim):
            im = i_im*im_step + self.pim_min
            for i_re in range(self.Pre):
                c_s[i_im, i_re] = i_re*re_step + self.pre_min + im*1j

        # create list of indexes
        idxs = []
        for i_im in range(self.Pim):
            for i_re in range(self.Pre):
                idxs.append((i_im, i_re))

        for idx in idxs:
            results[idx] = self.single_point_calculation(c_s[idx])

        return results.tolist()

    def single_point_calculation(self, c):
        """Calculates the value for a single location"""
        i = 0
        z = 0+0j
        while math.sqrt(abs(z)) <= self.T and i < self.I:
            z = z**2 + c
            i += 1
        return i/self.I
