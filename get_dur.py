#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd04>
#
# Distributed under terms of the MIT license.

import sys

total_dur=0
for sent in sys.stdin.read().strip().split("\n"):
    sent = sent.split()
    try:
        total_dur += float(sent[2])
    except:
        print(sent)

print(total_dur/3600)
