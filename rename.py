#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

pathiter = (os.path.join(root, filename)
        for root, _, filenames in os.walk(folder)
        for filename in filenames
        )
for path in pathiter:
    newname =  path.replace('*.txt', '_ES_manual.txt')
    if newname != path:
        os.rename(path,newname)
