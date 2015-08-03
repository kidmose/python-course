import mandelbrot
import math

logger = mandelbrot.get_logger(__name__)


class OptimisedCalculator(mandelbrot.MandelbrotCalculator):
    """
    Optimised calculation based on NaiveCalculator.

    Profiled using line_profiler with default parameters
    (I=100, Pim=100, Pre=100, T=10, naive=False, optimised=True,
    output='output', pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
    calculate() running time before optimisation: 3.397 s

    # Optimisation step 01
    ## Observation
    `while math.sqrt(abs(z)) <= self.T and i < self.T:` is hit 245245 times
    and consumes 36.0% of the time.
    ## Change
    Eliminate math.sqrt by taking the square on both sides,
    as this is assumed to be an expensive operation.
    ## Speed-up
    Negligible, within noise.
    `**` operator might be as expensive as `math.sqrt`.

    # Optimisation step 02
    ## Observation
    Step 01 provided no improvement. It is possible that another operation is the expensive one.
    ## Change
    On same line as targeted in step 01 the calculation of the square can be moved
    to a precomputation step, eliminating the need to redo it 245245 times.
    ## Speed-up
    Still negligible.
    Apparently the comparissons and/or the variable dereference is what takes the time.
    """

    file_name_data = "optimised_data.csv"
    file_name_plot = "optimised_plot.pdf"

    def calculate(self):
        ms = list()

        im_span = self.pim_max-self.pim_min
        im_step = im_span / self.Pim
        re_span = self.pre_max-self.pre_min
        re_step = re_span / self.Pre

        Tprecomp = self.T**2

        for i_im in range(self.Pim):
            im = i_im*im_step + self.pim_min
            row = list()
            for i_re in range(self.Pre):
                c = i_re*re_step + self.pre_min + im*1j
                i = 0
                z = 0+0j
                while abs(z) <= Tprecomp and i < self.I:
                    z = z**2 + c
                    i += 1
                row.append(i/self.I)
            ms.append(row)

        return ms
