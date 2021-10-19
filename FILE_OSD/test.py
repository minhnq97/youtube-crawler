#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd04>
#
# Distributed under terms of the MIT license.

"""

"""
with open("mienbac.csv") as f:
    lines = f.read().splitlines()

with open("mienbac_extra.csv") as f1:
    lines1 = f1.read().splitlines()

f2 = open("mienbac_full.csv", "a")
for line in lines:
    f2.write(line)
    f2.write("\n")

for line in lines1:
    f2.write(line)
    f2.write("\n")
