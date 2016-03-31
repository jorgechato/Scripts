#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path, listdir, system
from glob import glob
import sys, getopt

def main(argv):
    before = ""
    after = ""
    remove = ""

    try:
        opts, args = getopt.getopt(argv,"b:a:r:",["before=","after=","remove="])
    except getopt.GetoptError:
        usage()

    for opt, arg in opts:
        if opt in ("-b", "--before"):
            before = arg
        elif opt in ("-a", "--after"):
            after = arg
        elif opt in ("-r", "--remove"):
            remove = arg
            changeFilename(remove)
        else:
            usage()

    if before != "" and after != "":
        changeFilename(before, after)
    else:
        usage()

def changeFilename(before, after=""):
    for value in glob("*"+before+"*"):
        filename = "".join(path.splitext(value)).replace(before, after)
        system("mv -vn -- "+value+" "+filename)
    sys.exit()

def usage():
    print '\t----------------------\n'
    print 'Name:\t\tname.py\nCreated by:\tJorge Chato\nWeb:\t\tjorgechato.com\n'
    print '\t----------------------\n'
    print '-b <old name> -a <new name>\tChange part of the filename to another\n'
    print '-r <old name>\t\t\tDelete part of the filename\n'
    sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
