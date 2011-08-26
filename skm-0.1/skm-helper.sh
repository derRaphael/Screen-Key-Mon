#!/bin/bash

#
# Script to perform some tasks
#

if [ "$(id -u)" != "0" ]; then
echo "This script must be run as root via sudo" 1>&2
exit 1
fi

while :
do

echo ""
echo "  *****************************"
echo "  *    ScreenKeyMon Helper    *"
echo "  *****************************"
echo "  *                           *"
echo "  * [r]emove screen-key-mon   *"
echo "  * [c]ompile project         *"
echo "  * [p]urge develepment data  *"
echo "  *                           *"
echo "  * [0] Exit/Stop Helper      *"
echo "  *                           *"
echo "  *****************************"
echo ""
echo -n "  Enter your menu choice [a-0]: "

read yourch

case $yourch in

r) 
	rm -rf /usr/share/pyshared/screenkeymon
	rm -rf /usr/local/lib/python2.6/dist-packages/screenkeymon
	rm -rf build
	rm -f /usr/local/bin/screen-key-mon 
	;;
c) 
	rm -rf /usr/share/pyshared/screenkeymon
	rm -rf /usr/local/lib/python2.6/dist-packages/screenkeymon
	rm -rf build
	rm -f /usr/local/bin/screen-key-mon 
	python setup.py install
	;;
p) 
	rm -rf build
	;;
0) 
	exit 0
	;;
*) 
	echo "Oopps!!! Please select choice r, c, p, or 0"
	echo "Press Enter to continue. . ."
	read 
	;;
esac

done


