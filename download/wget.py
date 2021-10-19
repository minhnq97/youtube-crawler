#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd04>
#
# Distributed under terms of the MIT license.

import subprocess
import sys
import os

for roots, dirs, files in os.walk(".", topdown=False):
    print(files)





exit()
with open("mbac.txt", "rt") as f:
    url_lists = f.read().splitlines()

f1 = open("../FILE_RESULT/mien_bac_result.txt", "a")
for url in url_lists:
    # execute command
    try:
        subprocess.run(["wget", url])
        f1.write(url.split(".mp3")[0].split("-")[-1] + ',' + url)
        f1.write('\n')
    except:
        print("------------ERROR------------")


