#!/usr/bin/env python
"""Tests for module naive"""

import unittest
import os
from mandelbrot.naive import NaiveCalculator as C
from mandelbrot import tests

NAIVE_DATA_FILE = os.path.join(tests.OUTPUT_DIR, C.file_name_data)
NAIVE_PLOT_FILE = os.path.join(tests.OUTPUT_DIR, C.file_name_plot)

class Test(unittest.TestCase):
    def setUp(self):
        tests.purge_output_dir()

    def tearDown(self):
        tests.delete_output_dir()

    def test_calculate(self):
        c = C(**tests.PARAM_LIST)
        ms = c.calculate()

        # Check dimensions
        self.assertEqual(len(ms), tests.PARAM_LIST['Pim'])
        for row in ms:
            self.assertEqual(len(row), tests.PARAM_LIST['Pre'])

        # check type
        for row in ms:
            for el in row:
                self.assertIsInstance(el, float)

    def test_save_data(self):
        # test save and load
        c = C(**tests.PARAM_LIST)
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
        c = C(**tests.PARAM_LIST)
        ms = c.calculate()
        c.plot(ms, NAIVE_PLOT_FILE)
        self.assertTrue(os.path.isfile(NAIVE_PLOT_FILE))

    def test_run(self):
        c = C(**tests.PARAM_LIST).run()

if __name__ == "__main__":
    unittest.main()
