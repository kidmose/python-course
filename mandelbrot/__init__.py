"""
Mini project for course in python calculating Mandelbrot fractals. 
"""
from abc import ABC
import logging
import sys

class MandelbrotCalculator(ABC):
    """
    Structure for calculation of mandelbrot sets.

    Provides a structure for the processing involved with 
    each implementation/approach to calculate a mandelbrot set. 
    The calculation itself is left to derived classes, 
    shared support functionality is implemented here (DRY principle). 
    """

    def __init__(self):
        pass

    def calculate(self):
        """Calculate and return the Mandelbrot set."""
        pass

    def plot(self, mandelbrot_set):
        """Plot the Mandelbrot set and return reference to figure."""
        pass

    def save_png(self, figure, file_name):
        """Save the figure to file_name."""
        pass

    def run(self):
        """Runs the sequence of the above steps."""
        ms = self.calculate()
        fig = self.plot(ms)
        self.save_png(fig, self.file_name)

    file_name = "DEFAULT_FILE_NAME.PDF"

def get_logger(name):
    logger = logging.getLogger(name)
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

    return logger
