import csv

'''Dictionary of states(keys) and capitals(values)
'''


dict_data = {
    'Armenia': 'Yerevan',
    'Austria': 'Vienna',
    'Azerbaijan': 'Baku',
    'Belarus': 'Minsk',
    'Belgium': 'Brussels',
    'Bosnia and Herzegovina': 'Sarajevo',
    'Bulgaria': 'Sofia',
    'Croatia': 'Zagreb',
    'Cyprus': 'Nicosia',
    'Czech Republic': 'Prague',
    'Denmark': 'Copenhagen',
    'Estonia': 'Tallinn',
    'Faroe Islands': 'Torshavn',
    'Finland': 'Helsinki',
    'France': 'Paris',
    'Georgia': 'Tbilisi',
    'Germany': 'Berlin',
    'Gibraltar': 'Gibraltar',
    'Greece': 'Athens',
    'Guernsey': 'Saint Peter Port',
    'Hungary': 'Budapest',
    'Iceland': 'Reykjavik',
    'Ireland': 'Dublin',
    'Isle of Man': 'Douglas',
    'Italy': 'Rome',
    'Jersey': 'Saint Helier',
    'Kosovo': 'Pristina',
    'Latvia': 'Riga',
    'Liechtenstein': 'Vaduz',
    'Lithuania': 'Vilnius',
    'Luxembourg': 'Luxembourg',
    'Macedonia': 'Skopje',
    'Malta': 'Valletta',
    'Moldova': 'Chisinau',
    'Monaco': 'Monaco',
    'Montenegro': 'Podgorica',
    'Netherlands': 'Amsterdam',
    'Northern Cyprus': 'North Nicosia',
    'Norway': 'Oslo',
    'Poland': 'Warsaw',
    'Portugal': 'Lisbon',
    'Romania': 'Bucharest',
    'Russia': 'Moscow',
    'San Marino': 'San Marino',
    'Serbia': 'Belgrade',
    'Slovakia': 'Bratislava',
    'Slovenia': 'Ljubljana',
    'Spain': 'Madrid',
    'Svalbard': 'Longyearbyen',
    'Sweden': 'Stockholm',
    'Switzerland': 'Bern',
    'Turkey': 'Ankara',
    'Ukraine': 'Kyiv',
    'United Kingdom': 'London',
    'Vatican City': 'Vatican City'
}

'''Creating csv file
'''


with open('capitals.csv', 'w') as file:
    for key in dict_data:
        csv_columns = []
        k = key
        csv_columns.append(k)
        v = dict_data[key]
        csv_columns.append(v)
        w = csv.DictWriter(file, fieldnames=csv_columns)
        w.writeheader()
