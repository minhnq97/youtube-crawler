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

with open(sys.argv[1], "rt") as f:
    id = [line.split(',')[0] for line in f.read().splitlines()]

print(len(id))
print(len(list(set(id))))
