import  mandelbrot

logger = mandelbrot.get_logger(__name__)

class NaiveCalculator(mandelbrot.MandelbrotCalculator):
    def calculate(self):
        logger.critical("No calculation implemented - simply producing zeroes")
        ms = list()

        for im in range(self.Pim):
            row = list()
            for re in range(self.Pre):
                row.append(0.)
            ms.append(row)

        return ms
