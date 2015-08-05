#!/usr/bin/env python
"""Tests for module optimised"""

import unittest
import os
from mandelbrot.optimised import OptimisedCalculator
from mandelbrot import tests

DATA_FILE = os.path.join(tests.OUTPUT_DIR, OptimisedCalculator.file_name_data)
PLOT_FILE = os.path.join(tests.OUTPUT_DIR, OptimisedCalculator.file_name_plot)

class Test(tests.test_naive.Test):
    # Class under test
    cut = OptimisedCalculator


if __name__ == "__main__":
    unittest.main()
