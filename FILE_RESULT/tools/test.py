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
f = open("../mien_nam.txt", "w")
for roots, dirs, files in os.walk("/project/AI-team/exp/temp_corpora/speech/6000_ASR/MIEN_NAM", topdown=False):
    for file in files:
        f.write(os.path.join("/project/AI-team/exp/temp_corpora/speech/6000_ASR/MIEN_NAM",file))
        f.write("\n")



