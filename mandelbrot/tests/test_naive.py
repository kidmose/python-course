#!/usr/bin/env python
"""Tests for naive"""

import unittest
import mandelbrot
from mandelbrot import MandelbrotCalculator as C

logger = mandelbrot.get_logger(__name__)

PARAM_LIST = {
    'pre_min': -1,
    'pre_max': 1, 
    'Pre': 10,
    'pim_min': -1,
    'pim_max': 1,
    'Pim': 10,
    'T': 10
}
class Test(unittest.TestCase):
    def test_MandebrotCalculator(self):
        self.assertIsNotNone(C(**PARAM_LIST))

        for (K, V) in PARAM_LIST.items():
            with self.assertRaises(KeyError):
                kwargs = {k: v for (k, v) in PARAM_LIST.items() if k != K}
                C(**kwargs)

        with self.assertRaises(ValueError):
            kwargs = dict(PARAM_LIST)
            kwargs['pre_min'] = 1
            kwargs['pre_max'] = -1
            C(**kwargs)

        with self.assertRaises(ValueError):
            kwargs = dict(PARAM_LIST)
            kwargs['pim_min'] = 1
            kwargs['pim_max'] = -1
            C(**kwargs)

        with self.assertRaises(ValueError):
            kwargs = dict(PARAM_LIST)
            kwargs['Pre'] = 0
            C(**kwargs)

        with self.assertRaises(ValueError):
            kwargs = dict(PARAM_LIST)
            kwargs['Pre'] = -1
            C(**kwargs)

        with self.assertRaises(ValueError):
            kwargs = dict(PARAM_LIST)
            kwargs['Pim'] = 0
            C(**kwargs)

        with self.assertRaises(ValueError):
            kwargs = dict(PARAM_LIST)
            kwargs['Pim'] = -1
            C(**kwargs)
            
        with self.assertRaises(ValueError):
            kwargs = dict(PARAM_LIST)
            kwargs['T'] = 0
            C(**kwargs)

        with self.assertRaises(ValueError):
            kwargs = dict(PARAM_LIST)
            kwargs['T'] = -1
            C(**kwargs)
            

if __name__ == "__main__":
    unittest.main()
