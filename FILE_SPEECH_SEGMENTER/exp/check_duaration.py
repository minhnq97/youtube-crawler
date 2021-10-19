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

file_name = sys.argv[1]

with open(file_name, "rt") as f:
    lines = f.read().splitlines()
total_duration = 0
total_human_duration = 0
j = 0
for line in lines:
    _, s, e = line.split(",")
    #if 0.5 > float(human_duration) / float(duration) > 0.15:
    #    j += 1
    #total_duration += float(duration)
    total_human_duration += float(e) - float(s)
#print("TOTAL_DURATION", total_duration/3600)
print("TOTAL_SPEECH_DURATION", total_human_duration/3600)
