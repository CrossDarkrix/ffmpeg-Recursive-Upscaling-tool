#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, pathlib, shutil, sys

def one_convert(fname):
	if fname.split('.')[-1].lower() == 'png':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
		try:
			os.remove(fname)
		except:
			pass
	elif fname.split('.')[-1].lower() == 'jpg':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
		try:
			os.remove(fname)
		except:
			pass
	elif fname.split('.')[-1].lower() == 'jpeg':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
		try:
			os.remove(fname)
		except:
			pass
	elif fname.split('.')[-1].lower() == 'gif':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
		try:
			os.remove(fname)
		except:
			pass
	elif fname.split('.')[-1].lower() == 'tiff':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
		try:
			os.remove(fname)
		except:
			pass
	elif fname.split('.')[-1].lower() == 'bmp':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
		try:
			os.remove(fname)
		except:
			pass
	elif fname.split('.')[-1].lower() == 'rgb':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{} (x{}).png'.format(fname.split('.')[0], sys.argv[2])))
		try:
			os.remove(fname)
		except:
			pass

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

	FilesList = os.listdir(sys.argv[1])
	output_dir = '{}(scale_{}.000x)'.format(sys.argv[1], sys.argv[2])
	try:
		shutil.copytree(sys.argv[1], output_dir)
	except:
		pass
	os.chdir(output_dir)
	workpath = os.getcwd()
	for Files2 in Find_All_Files('./'):
		Files2 = '{}'.format(Files2.replace('./', workpath+'/'))
		try:
			try:
				os.chdir('{}'.format(Files2.replace(Files2.split('/')[-1:][0], '')))
			except FileNotFoundError:
				for pp in pathlib.Path(os.getcwd()).glob('{}'.format(Files2.replace(Files2.split('/')[-1:][0], '')).split('/')[-2]):
					if os.path.isdir(pp):
						os.chdir(pp)
						break
					elif os.path.islink(pp):
						os.chdir(os.path.realpath(pp))
					elif os.path.isfile(pp):
						continue
		except Exception as E:
			print(E)
			sys.exit(1)
		if not '(x{})'.format(sys.argv[2]) in Files2.split('/')[-1:][0]:
			one_convert(Files2.split('/')[-1])
		os.chdir(workpath)
	print('\nDone!')

if __name__ == '__main__':
	main()