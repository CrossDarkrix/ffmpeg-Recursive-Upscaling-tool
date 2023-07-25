#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CommandName: ffmupimg
ScriptName: ffmpeg_upscaling_image_tool.py
Description: Auto image Resizing tool
Author: DarkRix
Version: 2.2
"""

import concurrent.futures, os, shutil, sys

class ConvertThread(object):
    def __init__(self, workpath):
        self.workpath = workpath

    def find_dirs(self, directory):
        for r, Dirs, File, in os.walk(directory):
            yield r
            for F in File:
                yield os.path.join(r, F)

    def work(self):
        for Files2 in self.find_dirs(self.workpath):
            if os.path.exists(os.path.dirname(Files2)):
                os.chdir(os.path.dirname(Files2))
            else:
                os.chdir(os.path.dirname(os.path.abspath(Files2)))
            if not '(x{})'.format(sys.argv[2]) in Files2.split('/')[-1:][0]:
                concurrent.futures.ThreadPoolExecutor(os.cpu_count() * 9999).submit(self.convert, Files2.split('/')[-1]).result()
            os.chdir(self.workpath)
        for Files3 in self.find_dirs(self.workpath):
            if os.path.exists(os.path.dirname(Files3)):
                os.chdir(os.path.dirname(Files3))
            else:
                os.chdir(os.path.dirname(os.path.abspath(Files3)))
            self.frename(Files3.split('/')[-1])
            os.chdir(self.workpath)
        print('\nConverting Done!')

    def frename(self, fName):
        if ' (x{})'.format(sys.argv[2]) in fName:
            os.rename(fName, fName.replace(' (x{})'.format(sys.argv[2]), ''))

    def convert(self, fname):
        if fname.split('.')[-1].lower() == 'png':
            os.system('ffmpeg -i "{}" -hide_banner -y -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
            try:
                os.remove(fname)
            except:
                print('Error! Old File Not Removed!')
        elif fname.split('.')[-1].lower() == 'jpg':
            os.system('ffmpeg -i "{}" -hide_banner -y -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
            try:
                os.remove(fname)
            except:
                print('Error! Old File Not Removed!')
        elif fname.split('.')[-1].lower() == 'jpeg':
            os.system('ffmpeg -i "{}" -hide_banner -y -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
            try:
                os.remove(fname)
            except:
                print('Error! Old File Not Removed!')
        elif fname.split('.')[-1].lower() == 'tiff':
            os.system('ffmpeg -i "{}" -hide_banner -y -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
            try:
                os.remove(fname)
            except:
                print('Error! Old File Not Removed!')
        elif fname.split('.')[-1].lower() == 'webp':
            os.system('ffmpeg -i "{}" -hide_banner -y -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
            try:
                os.remove(fname)
            except:
                print('Error! Old File Not Removed!')
        elif fname.split('.')[-1].lower() == 'gif':
            os.system('ffmpeg -i "{}" -hide_banner -y -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).gif'.format(fname.split('.')[0], sys.argv[2])))
            try:
                os.remove(fname)
            except:
                print('Error! Old File Not Removed!')

def main():
    try:
        if sys.argv[1] == '-h':
            print('{} [input_directory] [scale_value(example: 3)]'.format(sys.argv[0].split('/')[-1]))
            sys.exit(0)
        elif sys.argv[1] == '--help':
            print('{} [input_directory] [scale_value(example: 3)]'.format(sys.argv[0].split('/')[-1]))
            sys.exit(0)
    except IndexError:
        print('{} [input_directory] [scale_value(example: 3)]'.format(sys.argv[0].split('/')[-1]))
        sys.exit(0)

    output_dir = '{}(scale_{}.000x)'.format(sys.argv[1], sys.argv[2])
    try:
        shutil.copytree(sys.argv[1], output_dir)
    except:
        print('Error! Folder not Created!')
        sys.exit(1)
    os.chdir(output_dir)
    print('converting......')
    concurrent.futures.ThreadPoolExecutor(os.cpu_count() * 999999999999999999).submit(ConvertThread(os.getcwd()).work).result()

if __name__ == '__main__':
    main()