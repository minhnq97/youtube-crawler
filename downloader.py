#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd04>
#
# Distributed under terms of the MIT license.

from __future__ import unicode_literals
import youtube_dl
import sys
import os

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] in ['finished', 'downloading']:

        try:
            speed = float(d['speed'])/1000
            #if speed < 50:
            #    raise Exception("too slow:", speed)
            print("Speed:", float(d['speed'])/1000)
        except KeyError:
            print("no speech info")


class Downloader():
    def __init__(self, link, folder):
        self.link = link
        self.folder = folder
        self.ydl_opts = {
             'ignoreerrors': True,
             'outtmpl': os.path.join(self.folder, '%(id)s.%(ext)s'),
             'dump_single_json': 'test.json',
             #'outtmpl': os.path.join(self.folder, str(self.file_name) + '.%(ext)s'),
             'format': 'bestaudio/best',
             'postprocessors': [{
                 'key': 'FFmpegExtractAudio',
                 'preferredcodec': 'wav',
                 'preferredquality': '192',
             }],
             'prefer_ffmpeg': True,
             'postprocessor_args': [
                 '-ar', '16000', '-sample_fmt', 's16', '-ac', '1'
                 ],
             'logger': MyLogger(),
             'progress_hooks': [my_hook],
         }
        self.ydl = youtube_dl.YoutubeDL(self.ydl_opts)

    def extract_info(self):
        meta = self.ydl.extract_info(self.link, download=False)
        return meta

    def download(self):
        self.ydl.download([self.link])
        #meta = ydl.extract_info(self.link, download=False)
        #print(meta['webpage_url'])



