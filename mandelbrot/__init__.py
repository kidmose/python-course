"""
Mini project for course in python calculating Mandelbrot fractals. 
"""
import logging
import sys

class MandelbrotCalculator(object):
    """
    Base class with structure for calculation of mandelbrot sets.

    Provides a structure for the processing involved with 
    each implementation/approach to calculate a mandelbrot set. 
    The calculation itself is left to derived classes, 
    shared support functionality is implemented here. (DRY principle). 
    """

    def __init__(self, *args, **kwargs):
        try:
            self.pre_min = kwargs['pre_min']
            self.pre_max = kwargs['pre_max']
            self.Pre = kwargs['Pre']
            self.pim_min = kwargs['pim_min']
            self.pim_max = kwargs['pim_max']
            self.Pim = kwargs['Pim']
            self.T = kwargs['T']
        except KeyError as e:
            logger.error("All parameters are mandatory.")
            raise e

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
        with open(file_name, 'w') as f:
            for row in mandelbrot_set:
                f.write(";".join([str(el) for el in row])+"\n")

    def plot(self, mandelbrot_set):
        """Plot the Mandelbrot set and return reference to figure."""
        logger.warn("Not implemented in the base class")

    def save_plot(self, figure, file_name):
        """Save the figure to file_name."""
        logger.warn("Not implemented in the base class")

    def run(self):
        """Runs the sequence of the above steps."""
        ms = self.calculate()
        fig = self.plot(ms)
        self.save_plot(fig, self.file_name_plot)
        self.save_data(ms, self.file_name_data)

    file_name_data = "DEFAULT_DATA_FILENAME.csv"
    file_name_plot = "DEFAULT_FILE_NAME.pdf"

def get_logger(name):
    logger = logging.getLogger(name)
    # remove any existing handlers
    for h in logger.handlers:
        logger.removeHandler(h)
    # only add a new handler if we've not set one yet
    if len(logger.handlers) == 0:
        fmt = '%(asctime)s.%(msecs)d %(levelname)s p%(process)s {%(pathname)s:%(lineno)d} - %(message)s'
        datefmt = '%Y-%m-%d %H:%M:%S'
        
        ch = logging.StreamHandler(sys.stdout)
        #ch.setLevel(log_level)
        
        formatter = logging.Formatter(fmt, datefmt=datefmt)
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger

logger = get_logger(__name__)
