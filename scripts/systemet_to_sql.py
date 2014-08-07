# -*- coding: utf-8 -*-

import sys

from xmlconverter import convert, from_attribute, computed_by
from utilities import change_category


def stringify(value):
    # replace ' with '' and wrap in ''
    return '\'' + value.replace('\'', '\'\'') + '\''


def create_sql_insert(values):
    sorted = []

    for column in schema:
        value = values[column]

        if type(value) is str or type(value) is unicode:
            value = stringify(value)

        if not value:
            value = 'NULL'

        sorted.append(unicode(value))

    return 'INSERT INTO articles VALUES(' + ','.join(sorted) + ');\n'


schema = [
    'name',
    'name2',
    'type'
]

mappings = {
    'name': from_attribute('Namn', unicode),
    'name2': from_attribute('Namn', unicode, 'Namn2'),
    'type': from_attribute('Varugrupp', change_category)
}

if __name__ == "__main__":
    input = sys.stdin
    if len(sys.argv) == 2:
        input = open(sys.argv[1])

    convert(input, 'artikel', schema, mappings, output_func=create_sql_insert)