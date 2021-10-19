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
import random
import numpy as np

file_20 = sys.argv[1]
file_full = sys.argv[2]
file_test = sys.argv[3]

with open(file_20) as f:
    list_20 = f.read().splitlines()
with open(file_full) as f1:
    list_full = f1.read().splitlines()

id_full, id_20 = [], []
for line in list_20:
    ID, _, _ = line.split(",")
    id_20.append(ID)
id_20 = np.unique(id_20)
final_list = []
for i in range(len(list_full)):
    ID, _, _ = list_full[i].split(",")
    count = 0
    for j in range(len(id_20)):
        if ID != id_20[j]:
            count += 1
    if count == len(id_20):
        final_list.append(list_full[i])
print(len(list_full) - len(id_20), len(final_list))
f1 = open(file_test, "w")
for ID in final_list:
    f1.write(ID)
    f1.write("\n")


exit()
speech_dur = 3600
while speech_dur > 0:
    choice = random.choice(final_list)
    index = final_list.index(choice)
    del final_list[index]
    ID, total_dur, human_dur = choice.spl







