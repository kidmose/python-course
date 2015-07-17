import  mandelbrot
import math

logger = mandelbrot.get_logger(__name__)


class NaiveCalculator(mandelbrot.MandelbrotCalculator):
    file_name_data = "naive_data.csv"
    file_name_plot = "naive_plot.pdf"

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
                re = i_re*re_step + self.pre_min
                row.append(self.iterate(re+im*1j))
            ms.append(row)

        return ms

    def iterate(self, c):
        i = 0
        z = 0+0j
        while math.sqrt(abs(z)) <= self.T and i < self.I:
            z = z**2 + c
            i += 1
        return i/self.I
