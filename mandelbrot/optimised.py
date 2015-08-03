import mandelbrot
import math

logger = mandelbrot.get_logger(__name__)


class OptimisedCalculator(mandelbrot.MandelbrotCalculator):
    """
    Optimised calculation based on NaiveCalculator.

    Profiled using line_profiler with default parameters
    (I=100, Pim=100, Pre=100, T=10, naive=False, optimised=True,
    output='output', pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
    Total running time before optimisation: 3.397 s

    # Optimisation step 1
    ## Observation
    `while math.sqrt(abs(z)) <= self.T and i < self.T:` is hit 245245 times
    and consumes 36.0% of the time.
    ## Change
    Eliminate math.sqrt by taking the square on both sides,
    as this is assumed to be an expensive operation.
    ## Speedup
    Negligeable, within noise.
    `**` operator might be as expensive as `math.sqrt`.
    """

    file_name_data = "optimised_data.csv"
    file_name_plot = "optimised_plot.pdf"

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
                while abs(z) <= self.T**2 and i < self.I:
                    z = z**2 + c
                    i += 1
                row.append(i/self.I)
            ms.append(row)

        return ms
