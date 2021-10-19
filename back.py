#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 minhnq <minhnq@rd04>
#
# Distributed under terms of the MIT license.

import os
import sys
from downloader import Downloader
import youtube_dl
import traceback
from youtube_dl.utils import DownloadError, ExtractorError

path = '/project/AI-team/exp/temp_corpora/speech/6000_ASR/QUANGNAM_QUANGNGAI_1'

def _download(url):
    dl = Downloader(url, path)
    #f = open('FILE_ERROR/miennam_file_error_counter.txt','w')
    flag = True
    counter=0
    print(flag)
    while flag:
        try:
            counter+=1
            if counter > 5:
                #f.write(url)
                #f.write('\n')
                break
            print("Downloading", url)
            dl.download()
            info = dl.extract_info()
            return info
            flag = False
        except Exception as e:
            flag = True
            print("Error: ",e)


if __name__ == "__main__":
    input_file_path = sys.argv[1]
    url_list = []
    #f_error = open('FILE_ERROR/miennam_file_error_url.txt', 'a')
    #f_result = open('FILE_RESULT/miennam_result_1.txt', 'a')
    with open(input_file_path, "rt") as f:
        url_list =  f.read().splitlines()
    ydl_opts = {
             'ignoreerrors': True,
         }
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    for url in url_list:
        try:
            meta = ydl.extract_info(url, download=False)
            if meta.get('_type', '') == 'playlist':
                url_playlist = [data['webpage_url'] for data in meta['entries'] if data != None]
                for u in url_playlist:
                    info = _download(u)
                    print("METAINFO:",info['id'], info['webpage_url'])
                    #f_result.write(info['id'] + ',' + info['webpage_url'])
                    #f_result.write('\n')
            else:
                info = _download(url)
                #print("METAINFO:",info['id'], info['webpage_url'])


                #f_result.write(info['id'] + ',' + info['webpage_url'])
                #f_result.write('\n')
        except DownloadError as e:
            print(traceback.print_exc())
            #f_error.write(url)
            #f_error.write('\n')
            print("Error at download")
        except ExtractorError as e:
            print(traceback.print_exc())
            print("Error at info  extractction")




