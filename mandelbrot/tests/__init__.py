"""
Test suite for module.

Holds constants and methods shared among multiple tests.
See submodules for individual tests.
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
    'T': 16,
    'I': 20,
}

OUTPUT_DIR = "test-output"

def purge_output_dir(path=OUTPUT_DIR):
    delete_output_dir(path=path)
    if os.path.exists(path):
        raise Exception("Failed to removed test output folder")
    os.makedirs(path)

def delete_output_dir(path=OUTPUT_DIR):
    if os.path.isfile(path):
        os.remove(path)
    if os.path.isdir(path):
        shutil.rmtree(path)
