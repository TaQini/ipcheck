#!/bin/sh
if [ $1 ]:
then    
    traceroute $1 > list
    python ip.py
else
    echo "usage: ./checkip.sh <ip>"
fi
