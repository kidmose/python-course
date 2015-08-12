# Mini project for course in python calculating Mandelbrot fractals #

[![Build Status](https://travis-ci.org/kidmose/python-course.svg?branch=master)](https://travis-ci.org/kidmose/python-course)

# Credit
 * `mandelbrot` package is the work of Egon Kidmose.
 * Originally forked from [Ian Oszwald's python_template_with_config](https://github.com/ianozsvald/python_template_with_config) for use of `setuputils`, module structure etc.

# Hand-in reading instructions
For the written part of the hand-in please refer to this document and comments in code, which are formatted for pydoc (After installing as described below: `python -c "import mandelbrot; help(mandelbrot)`).

# Setup

## Requirements
This serves to document my set-up as a known good enviroment. 
Not compatible with python 2.7.
Expected to be OS independent, but I develop and test on Linux Mint as specified below. 

 * Python 3.4+
 * Linux Mint 17.1 x86_64 on Oracle VirtualBox (At lest not tested elsewhere)

If matplotlib available the setup script will install it, but has some dependecies.
On Linux Mint 17.1 and presumeable recent ubuntus they can be installed with:

	sudo apt-get install -qq build-essential python-dev python3-dev libpng12-dev libjpeg8-dev libfreetype6-dev

## Installation instructions

	$ virtualenv -p python3 env  # Create virtual env for isolation
	$ source env/bin/activate  # Enter virtual environment
	$ pip install cython # setup relies on python
    $ python setup.py develop  # "develop" for symlinks to reflect code changes
	
	# Alternatively, for an installation that will not be edited:
    $ python setup.py install

## Test

How to run
TravisCI

# Project structure

# Tools and techniques used

## Git version control

Hosted on github for availability, easy publishing and nice tools.

Cloned cloned from Ian Ozswald's template and remote updated locally to point to new git repository - We strongly expect it to diverge completely from the template so no point in forking on github.
(Keeping refference just in case we want to pull Ians updates in.)

	$ git remote -v
	origin  git@github.com:kidmose/python-course.git (fetch)
	origin  git@github.com:kidmose/python-course.git (push)
	template        git@github.com:ianozsvald/python_template_with_config.git (fetch)
	template        git@github.com:ianozsvald/python_template_with_config.git (push)

Using `master` branch for stable code and `development` branch for unstable developement.
Implement the full gitflow workflow is deemed overkill for a small, single contributor projet.

## Test driven development

## Markdown

# Unimplemented ideas

 * how to run tests
 * Test coverage
 * Smart logging
 * PEP8/pyflake evaluation

## Results

	(env)egk@js4:[python-course]$ ./mandelbrot/cli.py --naive
	Arguments: Namespace(I=100, Pim=5000, Pre=5000, T=10, n=4, naive=True, optimised=False, output='output', parallel=False, pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
	Running naive
	Running calculate...
	calculate completed in 570.83s
	Running plot...
	plot completed in 1,728.02s
	Running save_data...
	save_data completed in 41.20s
	Done

	(env)egk@js4:[python-course]$ ./mandelbrot/cli.py --optimised
	Arguments: Namespace(I=100, Pim=5000, Pre=5000, T=10, n=4, naive=False, optimised=True, output='output', parallel=False, pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
	Running optimised
	Running calculate...
	calculate completed in 44.73s
	Running plot...
	plot completed in 1,752.35s
	Running save_data...
	save_data completed in 41.23s
	Done

	(env)egk@js4:[python-course]$ ./mandelbrot/cli.py --parallel -n=1
	Arguments: Namespace(I=100, Pim=5000, Pre=5000, T=10, n=1, naive=False, optimised=False, output='output', parallel=True, pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
	Running parallel
	Running calculate...
	calculate completed in 634.00s
	Running plot...
	plot completed in 1,819.19s
	Running save_data...
	save_data completed in 41.31s
	Done

	(env)egk@js4:[python-course]$ ./mandelbrot/cli.py --parallel -n=2
	Arguments: Namespace(I=100, Pim=5000, Pre=5000, T=10, n=2, naive=False, optimised=False, output='output', parallel=True, pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
	Running parallel
	Running calculate...
	calculate completed in 338.52s
	Running plot...
	plot completed in 1,790.49s
	Running save_data...
	save_data completed in 40.96s
	Done

	(env)egk@js4:[python-course]$ ./mandelbrot/cli.py --parallel -n=4
	Arguments: Namespace(I=100, Pim=5000, Pre=5000, T=10, n=4, naive=False, optimised=False, output='output', parallel=True, pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
	Running parallel
	Running calculate...
	calculate completed in 205.88s
	Running plot...
	plot completed in 1,797.77s
	Running save_data...
	save_data completed in 44.26s
	Done

	(env)egk@js4:[python-course]$ ./mandelbrot/cli.py --parallel -n=8
	Arguments: Namespace(I=100, Pim=5000, Pre=5000, T=10, n=8, naive=False, optimised=False, output='output', parallel=True, pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
	Running parallel
	Running calculate...
	calculate completed in 141.65s
	Running plot...
	plot completed in 1,834.95s
	Running save_data...
	save_data completed in 41.74s
	Done

	(env)egk@js4:[python-course]$ ./mandelbrot/cli.py --parallel -n=16
	Arguments: Namespace(I=100, Pim=5000, Pre=5000, T=10, n=16, naive=False, optimised=False, output='output', parallel=True, pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
	Running parallel
	Running calculate...
	calculate completed in 118.08s
	Running plot...
	plot completed in 1,836.94s
	Running save_data...
	save_data completed in 62.01s
	Done

	(env)egk@js4:[python-course]$ ./mandelbrot/cli.py --parallel -n=32
	Arguments: Namespace(I=100, Pim=5000, Pre=5000, T=10, n=32, naive=False, optimised=False, output='output', parallel=True, pim_max=1.5, pim_min=-1.5, pre_max=1.0, pre_min=-2.0)
	Running parallel
	Running calculate...
	calculate completed in 113.07s
	Running plot...
	plot completed in 1,813.41s
	Running save_data...
	save_data completed in 41.46s
	Done
	(env)egk@js4:[python-course]$
