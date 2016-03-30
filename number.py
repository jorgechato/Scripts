#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys

def main(argv):
    if len(sys.argv) == 1:
        order()
        sys.exit(2)

    if argv[0] == "-r":
        replace()
        sys.exit(2)

    if argv[0] == "-rf":
        replaceFolder()
        sys.exit(2)

    if argv[0] == "-h":
        print '\t----------------------\n'
        print 'Name:\t\tnumber.py\nCreated by:\tJorge Chato\nWeb:\t\tjorgechato.com\n'
        print '\t----------------------\n'
        print '[]\t\tAdd 0 into filenames, only files named with number\n'
        print '-r\t\tReplace the current filename to a number\n'
        print '-rf\t\tReplace the current folder name to a number\n'
        sys.exit(2)

def order():
    maxLength = 0
    sufix = os.path.splitext(os.listdir(".")[0])[1].replace(".","")

    for i in os.listdir("."):
        filename = os.path.splitext(i)[0]
        if maxLength < len(filename):
            maxLength = len(filename)

    prefix = "0" * (maxLength-1)
    os.system("rename 'unless (/0+[0-9]{4}."+sufix+"/) {s/^([0-9]{1,3}\."+sufix+")$/"+prefix+"$1/g;s/0*([0-9]{4}\..*)/$1/}' *")

def replace():
    sufix = os.path.splitext(os.listdir(".")[0])[1]
    filenames = []

    for i in os.listdir("."):
        filenames.append(os.path.splitext(i)[0].replace(" ","\ "))

    filenames.sort()

    for num in range(len(filenames)):
        prefix = "0" * (len(str(len(filenames))) - len(str(num)))
        os.system("mv -vn "+filenames[num]+sufix+" "+prefix+`num`+sufix)

def replaceFolder():
    folderNames = []

    for i in os.listdir("."):
        folderNames.append(os.path.split(i)[1].replace(" ","\ "))

    folderNames.sort()

    for num in range(len(folderNames)):
        prefix = "0" * (len(str(len(folderNames))) - len(str(num)))
        os.system("mv -vn "+folderNames[num]+" "+prefix+`num`)

if __name__ == "__main__":
    main(sys.argv[1:])
