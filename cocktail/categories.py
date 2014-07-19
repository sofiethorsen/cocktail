#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO would be nice to not have this list present in two places
all_categories = {
    1 : unicode(u'Alkoholfritt'),
    2 : unicode(u'Aniskryddad sprit'),
    3 : unicode(u'Aperitif'),
    4 : unicode(u'Armagnac'),
    5 : unicode(u'Bitter'),
    6 : unicode(u'Blanddrycker'),
    7 : unicode(u'Brandy'),
    8 : unicode(u'Vinsprit'),
    9 : unicode(u'Calvados'),
    10 : unicode(u'Cider'),
    11 : unicode(u'Cognac, Konjak'),
    12 : unicode(u'Drinkar och Cocktails'),
    13 : unicode(u'Fruktvin'),
    14 : unicode(u'Genever'),
    15 : unicode(u'Gin'),
    16 : unicode(u'Glögg och Glühwein'),
    17 : unicode(u'Grappa'),
    18 : unicode(u'Kryddad sprit'),
    19 : unicode(u'Kaffelikör, Chokladlikör'),
    20 : unicode(u'Fruktlikör, Bärlikör'),
    21 : unicode(u'Gräddlikör, Ägglikör'),
    22 : unicode(u'Kryddlikör, Örtlikör'),
    23 : unicode(u'Likör'),
    24 : unicode(u'Madeira'),
    25 : unicode(u'Mjöd'),
    26 : unicode(u'Montilla'),
    27 : unicode(u'Mousserande vin, Champagne'),
    28 : unicode(u'Vodka'),
    29 : unicode(u'Portvin'),
    30 : unicode(u'Punsch'),
    31 : unicode(u'Rom, Ljus rom'),
    32 : unicode(u'Rom, Mörk rom'),
    33 : unicode(u'Rom'),
    34 : unicode(u'Rosé, Rosévin'),
    35 : unicode(u'Vin, Rött vin'),
    36 : unicode(u'Sake'),
    37 : unicode(u'Sherry'),
    38 : unicode(u'Smaksatt sprit'),
    39 : unicode(u'Smaksatt vin'),
    40 : unicode(u'Sprit av frukt'),
    41 : unicode(u'Tequila, Mezcal'),
    42 : unicode(u'Vermouth'),
    43 : unicode(u'Vin av flera typer'),
    44 : unicode(u'Vin, Vitt vin'),
    45 : unicode(u'Whisky, Whiskey'),
    46 : unicode(u'Öl'),
    47 : unicode(u'Öl, Ljus öl'),
    48 : unicode(u'Öl, Mörk öl'),
    49 : unicode(u'Övrig sprit'),
    50 : unicode(u'Övrigt starkvin'),
}

case_insensitive_categories = {}

for key, value in all_categories.items():
  words = value.split(', ')
  words = [word.lower() for word in words]
  case_insensitive_categories[key] = words

all_types = [case_insensitive_categories[key] for key in case_insensitive_categories]