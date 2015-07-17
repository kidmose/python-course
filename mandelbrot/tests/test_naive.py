#!/usr/bin/env python
"""Tests for module naive"""

import unittest
import os
from mandelbrot.naive import NaiveCalculator as C
from mandelbrot.tests import PARAM_LIST
from mandelbrot.tests import purge_output_folder
from mandelbrot.tests import OUTPUT_DIR

NAIVE_DATA_FILE = os.path.join(OUTPUT_DIR, "test-output-naive-data")
NAIVE_PLOT_FILE = os.path.join(OUTPUT_DIR, "test-output-naive-plot")

class Test(unittest.TestCase):
    def setUp(self):
        purge_output_folder()

    def test_calculate(self):
        c = C(**PARAM_LIST)
        ms = c.calculate()

        # Check dimensions
        self.assertEqual(len(ms), PARAM_LIST['Pim'])
        for row in ms:
            self.assertEqual(len(row), PARAM_LIST['Pre'])

        # check type
        for row in ms:
            for el in row:
                self.assertIsInstance(el, float)

    def test_save_data(self):
        # test save and load
        c = C(**PARAM_LIST)
        ms1 = c.calculate()
        c.save_data(ms1, NAIVE_DATA_FILE)

        self.assertTrue(os.path.isfile(NAIVE_DATA_FILE))

        ms2 = list()
        with open(NAIVE_DATA_FILE, 'r') as f:
            for line in f:
                row = list()
                for cell in line.split(";"):
                    row.append(float(cell))
                ms2.append(row)

        self.assertEqual(ms1, ms2)

        # test that is overwrites, not appends
        c.save_data(ms1, NAIVE_DATA_FILE)
        ms2 = list()
        with open(NAIVE_DATA_FILE, 'r') as f:
            for line in f:
                row = list()
                for cell in line.split(";"):
                    row.append(float(cell))
                ms2.append(row)

        self.assertEqual(ms1, ms2)

    def test_plot(self):
        c = C(**PARAM_LIST)
        ms = c.calculate()
        fig = c.plot(ms)
        self.assertIsNotNone(fig)

    def test_save_plot(self):
        c = C(**PARAM_LIST)
        ms = c.calculate()
        fig = c.plot(ms)
        c.save_plot(fig, NAIVE_PLOT_FILE)

        self.assertTrue(os.path.isfile(NAIVE_PLOT_FILE))

    def test_run(self):
        c = C(**PARAM_LIST)
        c.run()

if __name__ == "__main__":
    unittest.main()
