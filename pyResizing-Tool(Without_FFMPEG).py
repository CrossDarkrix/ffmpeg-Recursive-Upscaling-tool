#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import concurrent.futures
import os
import shutil
import sys
from PIL import Image
from PIL import ImageFilter

class ConvertImage(object):
    def __init__(self, path):
        self.path = path
        self.imagelist = []
        self.filelist = []
        self.acceptfile = ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.rgb', '.tiff', '.xbm', '.pbm', '.pgm', '.ppm')

    def listfiles(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if file.lower().endswith(self.acceptfile):
                    yield os.path.join(root, file)

    def listupfiles(self):
        self.imagelist = sorted([files for files in self.listfiles()])
        return [Image.open(file).convert('RGBA') for file in self.imagelist]

    def convert(self):
        thread = concurrent.futures.ThreadPoolExecutor(os.cpu_count()*999999)
        images = thread.submit(self.listupfiles)
        thread.shutdown()
        self.filelist = images.result()
        for index, img in enumerate(self.filelist):
            try:
                img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2])))).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(self.imagelist[index].split('.')[0], sys.argv[2]))
            except:
                img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2])))).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(self.imagelist[index].split('.')[0], sys.argv[2]))
            try:
                os.remove(self.imagelist[index])
            except:
                print('Error! Old File Not Removed!')

class RenameImage(object):
    def __init__(self, path):
        self.path = path

    def rename(self):
        for root, dirs, files in os.walk(self.path):
            for file in files:
                if ' (x{})'.format(sys.argv[2]):
                    newName = file.replace(' (x{})'.format(sys.argv[2]), '')
                    os.rename(os.path.join(root, file), os.path.join(root, newName))

    def run(self):
        work = concurrent.futures.ThreadPoolExecutor(os.cpu_count()*9999999)
        work.submit(self.rename)
        work.shutdown()
        print('\nConverting Done!')

def main():
    try:
        if sys.argv[1] == '-h':
            print('{} [input_directory] [scale_value(example: 3)]'.format(sys.argv[0].split('/')[-1]))
            sys.exit(0)
        if sys.argv[1] == '--help':
            print('{} [input_directory] [scale_value(example: 3)]'.format(sys.argv[0].split('/')[-1]))
            sys.exit(0)
    except IndexError:
        print('{} [input_directory] [scale_value(example: 3)]'.format(sys.argv[0].split('/')[-1]))
        sys.exit(0)
    output_dir = '{}(scale_{}x)'.format(sys.argv[1], sys.argv[2])
    try:
        shutil.copytree(sys.argv[1], output_dir)
    except:
        print('Error! Folder not Created!')
        sys.exit(1)
    os.chdir(output_dir)
    ConvertImage(os.getcwd()).convert()
    RenameImage(os.getcwd()).run()

if __name__ == '__main__':
    main()
