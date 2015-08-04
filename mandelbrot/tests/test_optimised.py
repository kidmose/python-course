#!/usr/bin/env python
"""Tests for module naive"""

import unittest
import os
import pyximport; pyximport.install()
from mandelbrot.optimised import OptimisedCalculator
from mandelbrot import tests

NAIVE_DATA_FILE = os.path.join(tests.OUTPUT_DIR, OptimisedCalculator.file_name_data)
NAIVE_PLOT_FILE = os.path.join(tests.OUTPUT_DIR, OptimisedCalculator.file_name_plot)

class Test(tests.test_naive.Test):
    # Class under test
    cut = OptimisedCalculator
    

if __name__ == "__main__":
    unittest.main()
