from setuptools import setup, find_packages
from Cython.Build import cythonize

setup(
    name='mandelbrot',
    version='0.0.1',
    description='Mini project for course in python calculating Mandelbrot fractals',
    long_description="Course miniproject for Scientific Computing Using Python - 2. High Performance Computing in Python (2015), Aalborg University",
    author='Egon Kidmose',
    author_email='egk@es.aau.dk',
    url='https://github.com/kidmose/python-course',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    ext_modules=cythonize("mandelbrot/optimised.pyx"),
    install_requires=[
        'matplotlib',
        'pytest',
        'cython',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Course responsibles',
        'Operating System :: OS Independent',
        'Programming Language :: Python']
)
