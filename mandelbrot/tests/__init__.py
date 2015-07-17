"""
Test suite for module.

Holds constants and methods shared among in multiple tests.
"""

import os
import shutil

PARAM_LIST = {
    'pre_min': 100,
    'pre_max': 101, 
    'Pre': 10,
    'pim_min': -101,
    'pim_max': -100,
    'Pim': 14,
    'T': 16
}

OUTPUT_DIR = "test-output"

def purge_output_folder(path=OUTPUT_DIR):
    if os.path.isfile(path):
        os.remove(path)
    if os.path.isdir(path):
        shutil.rmtree(path)
    if os.path.exists(path):
        raise Exception("Failed to removed test output folder")
    os.makedirs(path)
