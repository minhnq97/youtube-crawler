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

f = open(sys.argv[1], "w")
for root, dirs, files in os.walk("/project/Corpora/speech/6000_ASR/MIEN_NAM", topdown=False):
    for id in files:
        f.write(os.path.join("/project/Corpora/speech/6000_ASR/MIEN_NAM", id))
        f.write("\n")
