#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os, shutil, sys
from PIL import Image
from PIL import ImageFilter

def convert(fname):
    if fname.split('.')[-1].lower() == 'png':
        img = Image.open(fname).convert('RGBA')
        try:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.Resampling.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        except AttributeError:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        try:
            os.remove(fname)
        except:
            print('Error! Old File Not Removed!')
    elif fname.split('.')[-1].lower() == 'jpg':
        img = Image.open(fname).convert('RGBA')
        try:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.Resampling.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        except AttributeError:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        try:
            os.remove(fname)
        except:
            print('Error! Old File Not Removed!')
    elif fname.split('.')[-1].lower() == 'jpeg':
        img = Image.open(fname).convert('RGBA')
        try:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.Resampling.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        except AttributeError:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        try:
            os.remove(fname)
        except:
            print('Error! Old File Not Removed!')
    elif fname.split('.')[-1].lower() == 'tiff':
        img = Image.open(fname).convert('RGBA')
        try:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.Resampling.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        except AttributeError:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        try:
            os.remove(fname)
        except:
            print('Error! Old File Not Removed!')
    elif fname.split('.')[-1].lower() == 'bmp':
        img = Image.open(fname).convert('RGBA')
        try:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.Resampling.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        except AttributeError:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))    
        try:
            os.remove(fname)
        except:
            print('Error! Old File Not Removed!')
    elif fname.split('.')[-1].lower() == 'rgb':
        img = Image.open(fname).convert('RGBA')
        try:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.Resampling.LANCZOS).filter(ImageFilter.MedianFilter()).save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        except AttributeError:
            img.resize((img.width * round(float(sys.argv[2])), img.height * round(float(sys.argv[2]))), Image.LANCZOS).filter(ImageFilter.MedianFilter()) .save('{} (x{}).png'.format(fname.split('.')[0], sys.argv[2]))
        try:
            os.remove(fname)
        except:
            print('Error! Old File Not Removed!')

def File_Rename(fName):
    if ' (x{})'.format(sys.argv[2]) in fName:
        os.rename(fName, fName.replace(' (x{})'.format(sys.argv[2]), ''))

def Find_All_Files(Dir):
    for r, Dirs, File, in os.walk(Dir):
        yield r
        for F in File:
            yield os.path.join(r, F)

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
    workpath = os.getcwd()
    print('Please Wait.....................')
    for Files2 in Find_All_Files(os.curdir):
        if os.path.exists(os.path.dirname(Files2)):
            os.chdir(os.path.dirname(Files2))
        else:
            os.chdir(os.path.dirname(os.path.abspath(Files2)))
        if not '(x{})'.format(sys.argv[2]) in Files2.split('/')[-1:][0]:
            convert(Files2.split('/')[-1])
        os.chdir(workpath)
    for Files3 in Find_All_Files(workpath):
        if os.path.exists(os.path.dirname(Files3)):
            os.chdir(os.path.dirname(Files3))
        else:
            os.chdir(os.path.dirname(os.path.abspath(Files3)))
        File_Rename(Files3.split('/')[-1])
        os.chdir(workpath)

    print('\nConverting Done!')

if __name__ == '__main__':
    main()

