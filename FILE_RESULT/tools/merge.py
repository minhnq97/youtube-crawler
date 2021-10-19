#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd04>
#
# Distributed under terms of the MIT license.

"""

"""

with open("QNQN1.txt", "rt") as f:
    lines = f.read().splitlines()

with open("QNQN2.txt", "rt") as f1:
    lines1 = f1.read().splitlines()
import numpy as np
lines.extend(lines1)

lines = np.unique(lines)
f2 = open("QNQN.txt", "w")
for line in lines:
    f2.write(line + "\n")
