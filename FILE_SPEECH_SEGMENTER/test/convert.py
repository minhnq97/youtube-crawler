#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd05>
#
# Distributed under terms of the MIT license.

"""
"""
import os
import sys

f1 = open(sys.argv[1].split(".")[0] + "_test.txt", "w")
with open(sys.argv[1]) as f:
    for line in f.read().splitlines():
        ID, stime, etime = line.split(",")
        ID = ID.replace("/project/Corpora/speech/6000_ASR", "/project/AI-team/exp/temp_corpora/speech/6000_ASR")
        f1.write(ID + "," + stime + "," + etime)
        f1.write("\n")
