"""
Mini project for course in python calculating Mandelbrot fractals. 
"""
import logging
import sys
import os
import matplotlib
from time import time
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np


class MandelbrotCalculator(object):
    """
    Base class with structure for calculation of mandelbrot sets.

    Provides a structure for the processing involved with 
    each implementation/approach to calculate a mandelbrot set. 
    The calculation itself is left to derived classes, 
    shared support functionality is implemented here. (DRY principle). 

    See cli.py for explanation of arguments.
    """

    def __init__(self, *args, **kwargs):
        # Mandatory parameters - required for calculation
        try:
            self.pre_min = kwargs['pre_min']
            self.pre_max = kwargs['pre_max']
            self.Pre = kwargs['Pre']
            self.pim_min = kwargs['pim_min']
            self.pim_max = kwargs['pim_max']
            self.Pim = kwargs['Pim']
            self.T = kwargs['T']
            self.I = kwargs['I']
        except KeyError as e:
            logger.error("Parameter is mandatory.")
            raise e

        # Optional parameters
        self.output_dir = kwargs.get('output_dir', 'output')
        self.n = kwargs.get('n', 4)

        if self.pre_min >= self.pre_max:
            raise ValueError("min must be below max")

        if self.pim_min >= self.pim_max:
            raise ValueError("min must be below max")

        if not self.Pre > 0:
            raise ValueError("Must be positive")

        if not self.Pim > 0:
            raise ValueError("Must be positive")

        if not self.T > 0:
            raise ValueError("Must be positive")

    def calculate(self):
        """Calculate and return the Mandelbrot set."""
        logger.warn("Not implemented in the base class")

    def save_data(self, mandelbrot_set, file_name):
        """Save the calculated data to a CSV file."""
        if not os.path.exists(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name))
        with open(file_name, 'w') as f:
            for row in mandelbrot_set:
                f.write(";".join([str(el) for el in row])+"\n")

    def plot(self, mandelbrot_set, file_name):
        """Plot the Mandelbrot set and save it to a file."""
        data = np.array(mandelbrot_set)
        fig, ax = plt.subplots()
        heatmap = ax.pcolor(data, cmap=plt.cm.hot)

        if not os.path.exists(os.path.dirname(file_name)):
            os.makedirs(os.path.dirname(file_name))
        plt.savefig(file_name)

    def run(self):
        """Runs the sequence of the above steps."""

        print("Running calculate...")
        start = time()
        ms = self.calculate()
        print("calculate completed in {:,.2f}s".format(time()-start))

        print("Running plot...")
        start = time()
        self.plot(ms, os.path.join(self.output_dir, self.file_name_plot))
        print("plot completed in {:,.2f}s".format(time()-start))

        print("Running save_data...")
        start = time()
        self.save_data(ms, os.path.join(self.output_dir, self.file_name_data))
        print("save_data completed in {:,.2f}s".format(time()-start))

    @property
    def file_name_data(self):
        """Name of file to store data in."""
        raise NotImplementedError("Must be overridden in derived class")

    @property
    def file_name_plot(self):
        """Name of file to store plot in."""
        raise NotImplementedError("Must be overridden in derived class")


def get_logger(name):
    logger = logging.getLogger(name)
    # remove any existing handlers
    for h in logger.handlers:
        logger.removeHandler(h)
    # only add a new handler if we've not set one yet
    if len(logger.handlers) == 0:
        fmt = '%(asctime)s.%(msecs)d %(levelname)s p%(process)s {%(pathname)s:%(lineno)d} - %(message)s'
        fmt = '%(name)s - %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        
        formatter = logging.Formatter(fmt, datefmt=datefmt)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger

logger = get_logger(__name__)
