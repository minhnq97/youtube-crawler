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

with open(sys.argv[1], "rt") as f:
    lines = f.read().splitlines()
f1 = open("QNQN2.txt", "w")
for line in lines:
    id, _ = line.split(",")
    if os.path.exists(os.path.join("/project/Corpora/speech/6000_ASR/QUANGNAM_QUANGNGAI", id + ".wav")):
        f1.write(line + "\n")
