import csv
import os.path

'''Reading csv file as dictionary
'''

def type_file(path):
    extension = os.path.splitext(path)[1]
    return extension

def csv_reader(path):
    reader = csv.reader(open(path, 'r'))
    d = {}
    for row in reader:
        k, v = row
        d[k] = v

'''From the dictionary return the value (capital) of the input key(state)
'''

csv_reader('/data/capitals.csv')

def check_capital(state):
    if state in d.keys():
        return (d[state])
    else:
        return("Sorry, {} does not seem to be an European state".
               format(state))
