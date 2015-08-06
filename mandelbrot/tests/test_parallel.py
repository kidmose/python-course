#!/usr/bin/env python
"""Tests for module parallel"""

import unittest
import os
from mandelbrot.parallel import ParallelCalculator
from mandelbrot import tests

DATA_FILE = os.path.join(tests.OUTPUT_DIR, ParallelCalculator.file_name_data)
PLOT_FILE = os.path.join(tests.OUTPUT_DIR, ParallelCalculator.file_name_plot)

class Test(tests.test_naive.Test):
    # Class under test
    cut = ParallelCalculator

    def test_multiple_processes(self):
        with self.assertRaises(ValueError):
            self.test_calculate(n=0)
        self.test_calculate(n=1)
        self.test_calculate(n=4)


if __name__ == "__main__":
    unittest.main()
