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
        print("Test for exception with n=0")
        with self.assertRaises(ValueError):
            self.test_calculate(n=0)
        print("Test with 1 process")
        self.test_calculate(n=1)
        print("Test with 4 processes")
        self.test_calculate(n=4)


if __name__ == "__main__":
    unittest.main()
