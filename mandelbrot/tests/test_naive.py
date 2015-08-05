#!/usr/bin/env python
"""Tests for module naive"""

import unittest
import os
from mandelbrot.naive import NaiveCalculator
from mandelbrot import tests

DATA_FILE = os.path.join(tests.OUTPUT_DIR, NaiveCalculator.file_name_data)
PLOT_FILE = os.path.join(tests.OUTPUT_DIR, NaiveCalculator.file_name_plot)

class Test(unittest.TestCase):
    # Class Under Test
    cut = NaiveCalculator

    def setUp(self):
        tests.purge_output_dir()

    def tearDown(self):
        tests.delete_output_dir()

    def test_calculate(self):
        c = self.cut(**tests.PARAM_LIST)
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
        c = self.cut(**tests.PARAM_LIST)
        ms1 = c.calculate()
        c.save_data(ms1, DATA_FILE)

        self.assertTrue(os.path.isfile(DATA_FILE))

        ms2 = list()
        with open(DATA_FILE, 'r') as f:
            for line in f:
                row = list()
                for cell in line.split(";"):
                    row.append(float(cell))
                ms2.append(row)

        self.assertEqual(ms1, ms2)

        # test that is overwrites, not appends
        c.save_data(ms1, DATA_FILE)
        ms2 = list()
        with open(DATA_FILE, 'r') as f:
            for line in f:
                row = list()
                for cell in line.split(";"):
                    row.append(float(cell))
                ms2.append(row)

        self.assertEqual(ms1, ms2)

    def test_plot(self):
        c = self.cut(**tests.PARAM_LIST)
        ms = c.calculate()
        c.plot(ms, PLOT_FILE)
        self.assertTrue(os.path.isfile(PLOT_FILE))

    def test_run(self):
        c = self.cut(**tests.PARAM_LIST).run()

    def test_calculate(self):
        """Ensure that the result always is the same."""

        self.assertEqual(
            self.cut(pre_min=0, pre_max=1, Pre=1, pim_min=0, pim_max=1, Pim=1, T=1, I=1).calculate(),
            [[1.0]]
        )

        self.assertEqual(
            self.cut(pre_min=0, pre_max=1, Pre=1, pim_min=0, pim_max=1, Pim=1, T=1e6, I=1e6).calculate(),
            [[1.0]]
        )

        self.assertEqual(
            self.cut(pre_min=-1, pre_max=1, Pre=3, pim_min=-1, pim_max=1, Pim=3, T=1e6, I=1e6).calculate(),
            [[8e-06, 1e-05, 8e-06],
             [1.7e-05, 1.0, 1.0],
             [1.7e-05, 1.0, 1.0]]
        )

        self.assertEqual(
            self.cut(pre_min=-4, pre_max=5, Pre=10, pim_min=-4, pim_max=5, Pim=10, T=10, I=10).calculate(),
            [[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
             [0.3, 0.3, 0.3, 0.3, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3],
             [0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3],
             [0.3, 0.4, 0.4, 0.5, 0.5, 0.5, 0.4, 0.4, 0.3, 0.3],
             [0.3, 0.4, 0.5, 1.0, 1.0, 0.8, 0.4, 0.4, 0.3, 0.3],
             [0.3, 0.4, 0.5, 0.7, 1.0, 0.7, 0.4, 0.4, 0.3, 0.3],
             [0.3, 0.4, 0.4, 0.5, 0.5, 0.5, 0.4, 0.4, 0.3, 0.3],
             [0.3, 0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3],
             [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
             [0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3]]
        )

        self.assertEqual(
            self.cut(pre_min=-4, pre_max=5, Pre=10, pim_min=-4, pim_max=5, Pim=10, T=10000000, I=10000).calculate(), 
            [[0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0006, 0.0006, 0.0007, 0.0007, 0.0007, 0.0006, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0006, 0.0007, 0.0007, 0.0008, 0.0008, 0.0007, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0007, 0.0008, 0.0012, 1.0, 0.0011, 0.0007, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0007, 0.0007, 0.001, 1.0, 0.001, 0.0007, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0006, 0.0007, 0.0007, 0.0008, 0.0007, 0.0007, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0006, 0.0006, 0.0007, 0.0007, 0.0007, 0.0006, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006],
             [0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006, 0.0006]]
        )

if __name__ == "__main__":
    unittest.main()
