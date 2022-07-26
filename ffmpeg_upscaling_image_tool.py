#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CommandName: ffmupimg
ScriptName: ffmpeg_upscaling_image_tool.py
Description: Auto image Resizing tool
Author: DarkRix
"""

import os, shutil, sys, locale

try:
    Lang, coding = locale.getlocale()
    if Lang == 'ja_JP':
        setLanguage = 'JP'
    else:
        setLanguage = 'EN'
except:
    setLanguage = 'EN'

class setLocaling:
    if setLanguage == 'JP':
        helpText = '{} [入力フォルダ] [拡大するサイズの倍率(例: 3)]'.format(sys.argv[0].split('/')[-1])
        CreateErrorText = 'エラー! フォルダが作成できませんでした!'
        RemoveError = 'エラー! 変換前のファイルが削除できませんでした!'
        ConvertedText = '\n変換が完了しました!'
    else:
        helpText = '{} [input_directory] [scale_value(example: 3)]'.format(sys.argv[0].split('/')[-1])
        CreateErrorText = 'Error! Folder not Created!'
        RemoveError = 'Error! Old File Not Removed!'
        ConvertedText = '\nConverting Done!'

def convert(fname):
    if fname.split('.')[-1].lower() == 'png':
        os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}_tmpfile).png'.format(fname.split('.')[0], sys.argv[2])))
        try:
            os.remove(fname)
        except:
            print(setLocaling().RemoveError)
    elif fname.split('.')[-1].lower() == 'jpg':
        os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}_tmpfile).png'.format(fname.split('.')[0], sys.argv[2])))
        try:
            os.remove(fname)
        except:
            print(setLocaling().RemoveError)
    elif fname.split('.')[-1].lower() == 'jpeg':
        os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}_tmpfile).png'.format(fname.split('.')[0], sys.argv[2])))
        try:
            os.remove(fname)
        except:
            print(setLocaling().RemoveError)
    elif fname.split('.')[-1].lower() == 'gif':
        os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}_tmpfile).png'.format(fname.split('.')[0], sys.argv[2])))
        try:
            os.remove(fname)
        except:
            print(setLocaling().RemoveError)
    elif fname.split('.')[-1].lower() == 'tiff':
        os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}_tmpfile).png'.format(fname.split('.')[0], sys.argv[2])))
        try:
            os.remove(fname)
        except:
            print(setLocaling().RemoveError)
    elif fname.split('.')[-1].lower() == 'bmp':
        os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}_tmpfile).png'.format(fname.split('.')[0], sys.argv[2])))
        try:
            os.remove(fname)
        except:
            print(setLocaling().RemoveError)
    elif fname.split('.')[-1].lower() == 'rgb':
        os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}_tmpfile).png'.format(fname.split('.')[0], sys.argv[2])))
        try:
            os.remove(fname)
        except:
            print(setLocaling().RemoveError)

def File_Rename(fName):
    if ' (x{})'.format(sys.argv[2]) in fName:
        os.rename(fName, fName.replace(' (x{}_tmpfile)'.format(sys.argv[2]), ''))

def Find_All_Files(Dir):
    for r, Dirs, File, in os.walk(Dir):
        yield r
        for F in File:
            yield os.path.join(r, F)

def main():
    try:
            if sys.argv[1] == '-h':
                print(setLocaling().helpText)
                sys.exit(0)
            elif sys.argv[1] == '--help':
                print(setLocaling().helpText)
                sys.exit(0)
    except IndexError:
            print(setLocaling().helpText)
            sys.exit(0)
    if sys.argv[1][-1] == os.sep:
        sys.argv[1] = sys.argv[1].split(os.sep)[0]
    output_dir = '{}(scale_{}.000x)'.format(sys.argv[1], sys.argv[2])
    try:
        shutil.copytree(sys.argv[1], output_dir)
    except:
        print(setLocaling().CreateErrorText)
        sys.exit(1)
    os.chdir(output_dir)
    workpath = os.getcwd()
    for Files2 in Find_All_Files(os.curdir):
        if os.path.exists(os.path.dirname(Files2)):
            os.chdir(os.path.dirname(Files2))
        else:
            os.chdir(os.path.dirname(os.path.abspath(Files2)))
        if not '(x{}_tmpfile)'.format(sys.argv[2]) in Files2.split('/')[-1:][0]:
            convert(Files2.split('/')[-1])
        os.chdir(workpath)
    for Files3 in Find_All_Files(workpath):
        if os.path.exists(os.path.dirname(Files3)):
            os.chdir(os.path.dirname(Files3))
        else:
            os.chdir(os.path.dirname(os.path.abspath(Files3)))
        File_Rename(Files3.split('/')[-1])
        os.chdir(workpath)

    print(setLocaling().ConvertedText)

if __name__ == '__main__':
    main()
