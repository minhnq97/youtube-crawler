#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd04>
#
# Distributed under terms of the MIT license.

"""

"""
import os
import sys

file_input = sys.argv[1]
file_output = sys.argv[2]
region = sys.argv[3]
with open(file_input, "rt") as f:
    lines = f.read().splitlines()
f1 = open(file_output, "w")
for line in lines:
    if len(line.split(",")) == 4:
        ID, _, total_dur, human_dur = line.split(",")
        f1.write(os.path.join("/project/Corpora/speech/6000_ASR", region, ID + ".wav") + "," + total_dur + "," + human_dur)
        f1.write("\n")
    else:
        ID, total_dur, human_dur = line.split(",")
        f1.write(ID + "," + total_dur + "," + human_dur)
        f1.write("\n")
