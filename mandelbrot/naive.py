from __future__ import division

import mandelbrot
import math

logger = mandelbrot.get_logger(__name__)


class NaiveCalculator(mandelbrot.MandelbrotCalculator):
    file_name_data = "naive_data.csv"
    file_name_plot = "naive_plot.png"

    def calculate(self):
        ms = list()

        im_span = self.pim_max-self.pim_min
        im_step = im_span / self.Pim
        re_span = self.pre_max-self.pre_min
        re_step = re_span / self.Pre

        for i_im in range(self.Pim):
            im = i_im*im_step + self.pim_min
            row = list()
            for i_re in range(self.Pre):
                c = i_re*re_step + self.pre_min + im*1j
                i = 0
                z = 0+0j
                while math.sqrt(abs(z)) <= self.T and i < self.I:
                    z = z**2 + c
                    i += 1
                row.append(i/self.I)
            ms.append(row)

        return ms
