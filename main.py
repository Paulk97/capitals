''' importing related modules

'''
import sqlite3
import hashlib
import random
import argparse
import csv
import time
import sys
from myfolder.capitals import check_capital


conn = None
cursor = None
dbpath = 'scripts/data.db'


'''connecting to database in scripts folder.

'''


def open_and_create():

    global conn
    global cursor

    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM users")
    except sqlite3.OperationalError:
        dbmanager.save_new_user(conn, cursor)


'''check for user and password,

from the database connection scripts folder.
'''


def check_for_user(username, password):

    global conn
    global cursor

    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    salt = cursor.execute("SELECT salt FROM user WHERE username=?", (username,))
    salt = salt.fetchall()
    if salt == []:
        print('Invalid Username')
        print('Please, Check Your Username...')
        quit()
    salt = salt[0][0]
    results = cursor.execute("SELECT digest FROM user WHERE username=?", (username,))
    results = results.fetchall()[0][0]
    digest = salt + password
    for i in range(1000000):
        digest = hashlib.sha256(digest.encode('utf-8')).hexdigest()
    conn.commit()
    if digest == results:
        print('Username Correct')
        print('Password Correct')
        print('You are allowed to access the program!')
    else:
        print("Invalid Password")
        print('Please, Check Your Password...')
        quit()
    conn.commit()


'''Implementing argparse position and optional argument

'''

parser = argparse.ArgumentParser()
parser.add_argument('-c', help="check for a usernamename", required=True)
parser.add_argument('-p', help="the username password", required=True)
parser.add_argument('state', type=str, help="Dispaly capital's state name")
parser.add_argument('-v', '--verbosity',
                    help='increase verbosity', action='count', default=0)

args = parser.parse_args()

variable = check_capital(args.state)


'''Defining levels of verbosity

'''

if args.c and args.p:
    check_for_user(args.c, args.p)


if args.verbosity >= 2:
    time.sleep(1)
    print('Running {}...'.format(__file__))
    for i in range(101):
        time.sleep(0.01)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print(' ')
    time.sleep(1)
    print('Extracting your input from csv file...')
    for i in range(101):
        time.sleep(0.01)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print('')
    time.sleep(1)
    print('Fiding matching value...')
    for i in range(101):
        time.sleep(0.01)
        sys.stdout.write("\r%d%%" % i)
        sys.stdout.flush()
    print('')
    time.sleep(1)
    print('Obtainng the name of the capital...')
    for i in range(101):
        time.sleep(0.01)
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

conn.close()
