# Mini project for course in python calculating Mandelbrot fractals #

# Credit
 * `mandelbrot` package is the work of Egon Kidmose.
 * Originally forked from [Ian Oszwald's python_template_with_config](https://github.com/ianozsvald/python_template_with_config) for use of `setuputils`, module structure etc.

# Hand-in reading instructions
For the written part of the hand-in please refer to this document and comments in code, which are formatted for pydoc (After installing as described below: `python -c "import mandelbrot; help(mandelbrot)`).

# Setup

## Development environment
This serves to document my set-up as a known good enviroment. 
To my knowledge the code is not dependent on specifically using Anaconda for python nor on the OS.
Be cautious of running in python 2.7 and make sure to run unittest.

 * Python 3.4+
 * Anaconda set up as per course materials
 * Linux Mint 17.1 x86_64 on Oracle VirtualBox

## Installation instructions

	$ export PATH="/home/dkegokid/opt/anaconda3/bin:$PATH"  # Anaconda
	$ virtualenv env  # Avoid interfering with rest of system ...
	$ source env/bin/activate  # ... by using virtual enviroment
    $ python setup.py develop  # "develop" for symlinks to reflect code changes
	
	# Alternatively, for installation that will not be edited:
    $ python setup.py install

## Test

To execute unittest go to the `utils` folder and run `./unittests.sh` (Requires `sh`, alternatively check file for command).

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

## Unit testing

## Test driven development

## Markdown

# Unimplemented ideas

 * Test coverage
 * Smart logging
 * PEP8/pyflake evaluation

