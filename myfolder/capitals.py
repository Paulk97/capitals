import csv

'''Reading csv file as dictionary

'''
csv_path= 'data/capitals.csv'

reader = csv.reader(open(csv_path, 'r'))
d = {}
for row in reader:
    k, v = row
    d[k] = v

'''From the dictionary return the value (capital) of the input key(state)

'''


def check_capital(state):
    if state in d.keys():
        return (d[state])
    else:
        return("Sorry, {} does not seem to be an European state".
               format(state))
