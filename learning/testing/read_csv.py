# -*- coding: utf-8 -*-

__author__ = 'arobres'

import csv

def unicode_csv_reader():

    with open('Lista_paises_simple.csv', 'rU') as csvfile:
        file_reader = csv.reader(csvfile, delimiter=';', quotechar='\n')
        for row in file_reader:
            yield [unicode(cell, 'utf-8') for cell in row]


def obtain_all_countries():
    countries = []
    result = unicode_csv_reader()
    for question, answer in result:
        countries.append({'question': question, 'answer': answer})

    return countries
