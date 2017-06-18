#!/bin/bash
echo "Content-type: text/html\n\n"
echo ""
. /usr/local/bin/virtualenvwrapper.sh
. ~/.profile
workon cv
/home/pi/PetFeeder/turtle.py
