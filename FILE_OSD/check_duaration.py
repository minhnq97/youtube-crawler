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
for line in lines:
    _, _, duration, human_duration = line.split(",")
    total_duration += float(duration)
    total_human_duration += float(human_duration)
print("TOTAL_DURATION", total_duration/3600)
print("TOTAL_SPEECH_DURATION", total_human_duration/3600)

