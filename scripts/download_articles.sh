#!/bin/bash
XML_FILE="https://www.systembolaget.se/api/assortment/products/xml"

# remove old file
rm articles.txt

curl $XML_FILE > articles.txt