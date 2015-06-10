#!/usr/bin/env python
"""Mandelbrot calculations with different implementations."""
import argparse
import logging
from abc import ABC
import sys

import naive
#from mandelbrot import optimised
#from mandelbrot import parallel 

class MandelbrotCalculator(ABC):
    """
    Structure for calculation of mandelbrot sets.

    Provides a structure for the processing involved with 
    each implementation/approach to calculate a mandelbrot set. 
    The calculation itself is left to derived classes, 
    shared support functionality is implemented here (DRY principle). 
    """

    def __init__(self, 
    ):
        pass

    def calculate(self,
    ):
        pass

    def save(self,
    ):
        pass

    def plot(self,
    ):
        pass

    def save_pdf(self, 
    ):
        pass

    def run(self,
    ):
        ms = calculate()
        save(ms)
        fig = plot(ms)
        save_pdf(fig)

if __name__ == "__main__":
    # Create an argument parser which also shows the defaults when --help is
    # called
    parser = argparse.ArgumentParser(description='Various mandelbrot set implementations',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--pre_min', type=float, default=-2., help='Minimal value for Re(p) axis')
    parser.add_argument('--pre_max', type=float, default=1., help='Maximal value for Re(p) axis')
    parser.add_argument('--Prim', type=int, default=5000, help='Steps on the Im(p) axis')

    parser.add_argument('--pim_min', type=float, default=-1.5, help='Minimal value for Im(p) axis')
    parser.add_argument('--pim_max', type=float, default=1.5, help='Maximal value for Im(p) axis')
    parser.add_argument('--Pre', type=int, default=5000, help='Steps on the Re(p) axis')

    parser.add_argument('--T', type=int, default=10, help='Threshold T for calculation')

    parser.add_argument('--naive', type=bool, default=True, help='Whether to run the naive calculation')
    

    args = parser.parse_args()

    logger = logging.getLogger("mandelbrot")
    # remove any existing handlers
    for h in logger.handlers:
        logger.removeHandler(h)
    # only add a new handler if we've not set one yet
    if len(logger.handlers) == 0:
        fmt = '%(asctime)s.%(msecs)d p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        
        ch = logging.StreamHandler(sys.stdout)
        #ch.setLevel(log_level)
        
        formatter = logging.Formatter(fmt, datefmt=datefmt)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        

    logger.info('Arguments: {}'.format(args))

    if args.naive:
        logger.info('Running')
        naive.Calculator().run()
        logger.info('Done')
