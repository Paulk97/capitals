#! /usr/bin/env python3
''' importing related modules

'''


import argparse
import csv
import time
import sys
from capitals import check_capital


'''Implementing argparse position and optional argument

'''


parser = argparse.ArgumentParser()
parser.add_argument('state', type=str, help="Dispaly capital's state name")
parser.add_argument('-v', '--verbosity',
                    help='increase verbosity', action='count', default=0)
args = parser.parse_args()
variable = check_capital(args.state)
# print (args.state)


'''Defining levels of verbosity

'''


if args.verbosity >= 2:
    time.sleep(1)
    print('Running {}...'.format(__file__))
    for i in range(101):
        time.sleep(0.02)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print(' ')
    time.sleep(1)
    print('Extracting your input from csv file...')
    for i in range(101):
        time.sleep(0.02)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print('')
    time.sleep(1)
    print('Fiding matching value...')
    for i in range(101):
        time.sleep(0.02)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print('')
    time.sleep(1)
    print('Obtainng the name of the capital...')
    for i in range(101):
        time.sleep(0.02)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print('')
    time.sleep(1)
    print('Returning matched value...')
    for i in range(101):
        time.sleep(0.02)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print('')
    time.sleep(2)
    print("The Eu state's capital of {} is {}".format(args.state, variable))
elif args.verbosity >= 1:
    print("The Eu state's capital of {} is {}".format(args.state, variable))
else:
    print(variable)
