#!/usr/bin/python 
#codind: utf-8

__author__ = "TaQini"

import re
import os

pattern = "(((([2][5][0-5])|([2][0-4][0-9]\.)|([1]?[0-9]?[0-9]\.)){3}(([2][5][0-5])|([2][0-4][0-9])|([1]?[0-9]?[0-9]))))"
res = open("./list","r").read()

r = re.findall(pattern,res)
for i in range(len(r)):
    if (i%2==1):
        os.system("curl ip.cn/index.php?ip=" + r[i][0])
    #print r[i][0]

