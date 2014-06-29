# -*- coding: utf-8 -*-

import sys

from xmlconverter import convert, fromAttribute, computedBy
from utilities import change_category

def stringify(value):
        # replace ' with '' and wrap in ''
        return '\''+value.replace('\'', '\'\'')+'\''

def create_sql_insert(values):
        sorted = []

        for column in schema:
                value = values[column]

                if type(value) is str or type(value) is unicode:
                        value = stringify(value)

                if not value:
                        value = 'NULL'

                sorted.append(unicode(value))

        return 'INSERT INTO articles VALUES('+','.join(sorted)+');\n'

schema = [
        'name',
        'name2',
        'category'
]

mappings = {
        'name': fromAttribute('Namn', unicode),
        'name2' : fromAttribute('Namn', unicode, 'Namn2'),
        'category': fromAttribute('Varugrupp', change_category)
}


if __name__ == "__main__":
        input = sys.stdin
        if len(sys.argv) == 2:
                input = open(sys.argv[1])

        convert(input, 'artikel', schema, mappings, output_func=create_sql_insert)