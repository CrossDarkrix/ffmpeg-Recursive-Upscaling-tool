#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Version 1.0
"""

import concurrent.futures, os, sys

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
            concurrent.futures.ThreadPoolExecutor(os.cpu_count() * 9999).submit(self.convert, Files2.split('/')[-1]).result()
            os.chdir(self.workpath)
        print('\nConverting Done!')

    def convert(self, fname):
        if fname.split('.')[-1].lower() == 'webp':
            os.system('ffmpeg -i "{}" -hide_banner -y -vf scale=iw:ih -vcodec png "{}"'.format(fname, '{}.png'.format(fname.split('.webp')[0])))
            try:
                os.remove(fname)
            except:
                print('Error! Old File Not Removed!')

def main():
    try:
        if sys.argv[1] == '-h':
            print('{} [input_directory]'.format(sys.argv[0].split('/')[-1]))
            sys.exit(0)
        elif sys.argv[1] == '--help':
            print('{} [input_directory]'.format(sys.argv[0].split('/')[-1]))
            sys.exit(0)
    except IndexError:
        print('{} [input_directory]'.format(sys.argv[0].split('/')[-1]))
        sys.exit(0)
    os.chdir('{}'.format(sys.argv[1]))
    print('converting......')
    concurrent.futures.ThreadPoolExecutor(os.cpu_count() * 999999999999999999).submit(ConvertThread(os.getcwd()).work).result()

if __name__ == '__main__':
    main()
