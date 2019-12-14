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
        k,v = row
        d[k] = v

csv_reader('/home/seed/capitals/data/capitals.csv')
