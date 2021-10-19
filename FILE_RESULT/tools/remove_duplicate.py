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
import numpy as np

input_file = sys.argv[1]

with open(input_file, "rt") as f:
    lines = f.read().splitlines()
lines = np.unique(lines)
print(len(lines))
f1 = open("QNQN.txt", "w")

for line in lines:
    f1.write(line)
    f1.write("\n")
