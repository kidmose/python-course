"""
Efficient algorithm based on naive, implementing cython.
"""

import mandelbrot
import math

logger = mandelbrot.get_logger(__name__)


class OptimisedCalculator(mandelbrot.MandelbrotCalculator):
    """
    Optimised calculation based on NaiveCalculator.

    Adding cython provides the primary optimisation, 
    secondarily some code rewrite in inner loop provides a minor contribution.

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

    # Optimisation step 03

    ## Observation

    To cut down the most expensive part - the while-loop with comparisson and multipe references -
    at least two potential approaches exist:
    Vectorise to eliminate looping or compile to make operations cheaper.

    ## Change

    We use cython to translate the code into C which is then compiled.

    ## Speed-up

    `line_profiler` can no longer be used.
    We use `timeit` within ipython to compare against the naive implementation and
    see aproximately 2 times speed-up:

    >>> from mandelbrot.naive import NaiveCalculator as NC
    >>> %timeit NC(I=100, Pim=100, Pre=100, T=10, output='output', pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0).calculate()
    1 loops, best of 3: 164 ms per loop

    >>> from mandelbrot.optimised import OptimisedCalculator as OC
    >>> %timeit OC(I=100, Pim=100, Pre=100, T=10, output='output', pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0).calculate()
    10 loops, best of 3: 81.5 ms per loop

    After compilation we rely on cythons annotation for a "profile" (`cython -a mandelbrot/optimised.pyx`),
    as the compilation obfuscates the output of cProfile making it hard to use,
    while line_profiler cannot be used at all.
    What this really profiles is how much each line still needs to interact with the python interpreter, rather than running in pure c. 

    # Optimisation step 04

    ## Observation

    Cython still makes many calls to python, as evident from the `profiling/03-step.html`.

    ## Change

    All variables used in the calculation loops are declared for cython to eliminate calls into python.

    ## speed-up

    >>> %timeit OC(I=100, Pim=100, Pre=100, T=10, output='output', pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0).calculate()
    10 loops, best of 3: 36 ms per loop

    # Optimisation step 05

    ## Observation

    The `abs(...)` in the innermost loop is called many times and also general so assumed ineffective.

    ## Change

    Specialise calculation, move some out to precalculation.

    ## Speed-up

    >>> %timeit OC(I=100, Pim=100, Pre=100, T=10, output='output', pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0).calculate()
    10 loops, best of 3: 20.7 ms per loop

    And with 1000x1000 points rather than 100x100 we see it's roughly linear:

    >>> %timeit OC(I=100, Pim=1000, Pre=1000, T=10, output='output', pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0).calculate()
    1 loops, best of 3: 2.58 s per loop
    """

    file_name_data = "optimised_data.csv"
    file_name_plot = "optimised_plot.png"

    def calculate(self):
        """See module and parrent."""
        # Decalaring variables for cython
        cdef double im_span, im_step, re_span, re_step
        # cdef unsigned long long int T # let python handle the overflowing 
        cdef unsigned int i_im, i_re, Pim, Pre, i, I
        cdef double im, re, pim_min, pre_min
        cdef double complex z, c

        # Avoiding object reference for constants
        T = self.T**4
        Pim = self.Pim
        Pre = self.Pre
        pim_min = self.pim_min
        pre_min = self.pre_min
        I = self.I

        ms = list()

        im_span = self.pim_max-self.pim_min
        im_step = im_span / Pim
        re_span = self.pre_max-self.pre_min
        re_step = re_span / Pre

        for i_im in range(Pim):
            im = i_im*im_step + pim_min
            row = list()
            for i_re in range(Pre):
                c = i_re*re_step + pre_min + im*1j
                i = 0
                z = 0+0j
                while (z.real*z.real + z.imag*z.imag) <= T and i < I: # sqrt(abs(z))<=t**4 and i
                    z = z**2 + c
                    i += 1
                row.append(float(i)/float(I))
            ms.append(row)

        return ms
