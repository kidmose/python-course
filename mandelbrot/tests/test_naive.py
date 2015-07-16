#!/usr/bin/env python
"""Tests for naive"""

import unittest
import mandelbrot
from mandelbrot import naive

logger = mandelbrot.get_logger(__name__)

class Test(unittest.TestCase):
    def test1(self):
        logger.error("Not testing anything!")
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
