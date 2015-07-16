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

## Installation instructions

	$ virtualenv -p python3 env  # Create virtual env for isolation
	$ source env/bin/activate  # Enter virtual environment
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
