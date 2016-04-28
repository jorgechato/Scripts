#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, listdir, system
import sys

def main(argv):
    if len(sys.argv) == 1:
        order()
        sys.exit()

    if argv[0] == "-r":
        replace()
        sys.exit()

    if argv[0] == "-rf":
        replaceFolder()
        sys.exit()

    if argv[0] == "-h":
        print '\t----------------------\n'
        print 'Name:\t\tnumber.py\nCreated by:\tJorge Chato\nWeb:\t\tjorgechato.com\n'
        print '\t----------------------\n'
        print '[]\t\tAdd 0 into filenames, only files named with number\n'
        print '-r\t\tReplace the current filename to a number\n'
        print '-rf\t\tReplace the current folder name to a number\n'
        sys.exit()

def order():
    maxLength = 0
    sufixes = []

    for index, value in enumerate(listdir(".")):
        filename = path.splitext(value)[0]
        sufixes.append(path.splitext(listdir(".")[index])[1])
        if maxLength < len(filename):
            maxLength = len(filename)

    sufixes = list(set(sufixes))
    prefix = "0" * (maxLength - 1)

    for i in sufixes:
        sufix = i.replace(".","")
        system("rename 'unless (/0+[0-9]{4}."+sufix+"/) {s/^([0-9]{1,3}\."+sufix+")$/"+prefix+"$1/g;s/0*([0-9]{"+`maxLength`+"}\..*)/$1/}' *")

def replace():
    filenames = []

    for i in listdir("."):
        name = path.splitext(i)[0].replace(" ","\ ") + path.splitext(i)[1]
        filenames.append(name)

    filenames.sort()

    for num in range(len(filenames)):
        split = filenames[num].rsplit('.', 1)
        sufix = "." + split[1]
        filename = split[0]
        prefix = "0" * (len(str(len(filenames))) - len(str(num+1)))
        system("mv -vn "+filename+sufix+" "+prefix+`(num+1)`+sufix)

def replaceFolder():
    folderNames = []

    for i in listdir("."):
        folderNames.append(path.split(i)[1].replace(" ","\ "))

    folderNames.sort()

    for num in range(len(folderNames)):
        prefix = "0" * (len(str(len(folderNames))) - len(str(num)))
        system("mv -vn "+folderNames[num]+" "+prefix+`num`)

if __name__ == "__main__":
    main(sys.argv[1:])
