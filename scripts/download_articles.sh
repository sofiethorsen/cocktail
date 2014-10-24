#!/bin/bash
XML_FILE="http://www.systembolaget.se/Assortment.aspx?Format=Xml"

# remove old file
rm articles.txt

curl $XML_FILE > articles.txt