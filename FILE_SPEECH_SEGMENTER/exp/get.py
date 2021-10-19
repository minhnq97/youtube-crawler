#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd04>
#
# Distributed under terms of the MIT license.

"""

"""
import sys
import random
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
f1 = open(sys.argv[2], "w")
speech_dur = 3600
while speech_dur > 0:
    choice = random.choice(lines)
    index = lines.index(choice)
    del lines[index]
    ID, stime, etime = choice.split(",")
    f1.write(choice)
    f1.write("\n")
    speech_dur -= float(etime) - float(stime)


