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
import os
import random

speech_dur = sys.argv[1]
file_name = sys.argv[2]
output_file = sys.argv[3]
#file_path = "/project/Corpora/speech/6000_ASR/QUANGNAM_QUANGNGAI"

with open(os.path.join("/mnt/VAIS/Home/minhnq/test/FILE_SPEECH_SEGMENTER", file_name)) as f:
    lines = f.read().splitlines()
lines = lines[1:]
f1 = open(output_file, "w")
speech_dur = int(speech_dur) * 3600
while speech_dur > 0:
    choice = random.choice(lines)
    index = lines.index(choice)
    del lines[index]
    ID, total_dur, human_dur = choice.split(",")
    #f1.write(os.path.join(file_path, ID + ".wav") + "," + total_dur + "," + human_dur)
    f1.write(ID + ',' + total_dur + ',' + human_dur)
    #ID, total_dur, human_dur = choice.split(",")
    #f1.write(ID + "," + total_dur + "," + human_dur)
    f1.write("\n")
    speech_dur -= float(human_dur)




