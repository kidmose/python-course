#!/usr/bin/env python
"""Command Line Interface for the package."""
import argparse

import mandelbrot
from mandelbrot import naive
from mandelbrot import optimised
from mandelbrot import parallel

if __name__ == "__main__":
    # Create an argument parser which also shows the defaults when --help is
    # called
    parser = argparse.ArgumentParser(description='Various mandelbrot set implementations',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--pre_min', type=float, default=-2., help='Minimal value for Re(p) axis')
    parser.add_argument('--pre_max', type=float, default=1., help='Maximal value for Re(p) axis')
    parser.add_argument('--Pre', type=int, default=5000, help='Steps on the Re(p) axis')

    parser.add_argument('--pim_min', type=float, default=-1.5, help='Minimal value for Im(p) axis')
    parser.add_argument('--pim_max', type=float, default=1.5, help='Maximal value for Im(p) axis')
    parser.add_argument('--Pim', type=int, default=5000, help='Steps on the Im(p) axis')

    parser.add_argument('-T', type=int, default=10, help='Threshold T for calculation')
    parser.add_argument('-I', type=int, default=100, help='Max iterations pr. point')
    parser.add_argument('-n', type=int, default=4, help='Number of parallel process (Applies to parallel only)')

    parser.add_argument('--naive', action='store_true', help='Whether to run the naive calculation')
    parser.add_argument('--optimised', action='store_true', help='Whether to run the optimised calculation')
    parser.add_argument('--parallel', action='store_true', help='Whether to run the parallel calculation')
    
    parser.add_argument('--output', type=str, default="output", help='Output folder')

    args = parser.parse_args()        

    # logger = mandelbrot.get_logger(__name__)
    print('Arguments: {}'.format(args))

    if args.naive:
        print('Running naive')
        naive.NaiveCalculator(**dict(args._get_kwargs())).run()
        print('Done')
    if args.optimised:
        print('Running optimised')
        optimised.OptimisedCalculator(**dict(args._get_kwargs())).run()
        print('Done')
    if args.parallel:
        print('Running parallel')
        parallel.ParallelCalculator(**dict(args._get_kwargs())).run()
        print('Done')
