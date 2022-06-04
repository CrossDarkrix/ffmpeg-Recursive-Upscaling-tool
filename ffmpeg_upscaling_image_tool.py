#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, glob, os, os.path, shutil, pathlib

currentdir = os.getcwd()

def one_convert(fname):
	if fname.split('.')[-1].lower() == 'png':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{}_#x{}.png'.format(fname.split('.')[0], sys.argv[2])))
	elif fname.split('.')[-1].lower() == 'jpg':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{}_#x{}.png'.format(fname.split('.')[0], sys.argv[2])))
	elif fname.split('.')[-1].lower() == 'jpeg':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{}_#x{}.png'.format(fname.split('.')[0], sys.argv[2])))
	elif fname.split('.')[-1].lower() == 'gif':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{}_#x{}.png'.format(fname.split('.')[0], sys.argv[2])))
	elif fname.split('.')[-1].lower() == 'tiff':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{}_#x{}.png'.format(fname.split('.')[0], sys.argv[2])))
	elif fname.split('.')[-1].lower() == 'bmp':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{}_#x{}.png'.format(fname.split('.')[0], sys.argv[2])))
	elif fname.split('.')[-1].lower() == 'rgb':
		os.system('ffmpeg -i "{}" -vf scale=iw*{}:ih*{} "{}"'.format(fname, sys.argv[2], sys.argv[2], '{}_#x{}.png'.format(fname.split('.')[0], sys.argv[2])))
	try:
		os.remove(fname)
	except:
		pass

def DetectDirectorys(ListFiles, rootdir):
	Dirs = []
	File = []
	for Files in ListFiles:
		if os.path.isfile(os.path.join(rootdir, Files)):
			File.append(Files)
		elif os.path.islink(os.path.join(rootdir, Files)):
			_ = ''
		else:
			Dirs.append(Files)

	return Dirs, File

def WorkFiles(FilesLists):
	returnpath = ['']
	returnpathsub = ['']
	WorkPath = os.getcwd()
	for Files2 in FilesLists:
		if not '_#x' in Files2:
			one_convert(Files2)
	while True:
		if not ''.join(DetectDirectorys(os.listdir(), os.getcwd())[0]) == '':
			if not d_back == os.getcwd():
				for subs in DetectDirectorys(os.listdir(), os.getcwd())[0]:
					if not os.path.isfile(subs):
						returnpath[0] = '{}/../'.format(os.getcwd())
						returnpathsub[0] = '../../'
						subds = os.path.join(os.getcwd(), subs)
						try:
							os.chdir(subds)
						except FileNotFoundError:
							try:
								os.chdir(subs)
							except FileNotFoundError:
								try:
									os.chdir('{}/{}'.format(os.getcwd().replace(os.getcwd().split('/')[-1], ''), subs))
								except FileNotFoundError:
									try:
										os.chdir('../{}'.format(subs))
									except FileNotFoundError:
										try:
											os.chdir('{}/{}'.format(WorkPath, subs))
										except FileNotFoundError:
											try:
												os.chdir(returnpath[0])
												P1 = pathlib.Path(returnpath[0])
												for PP in P1.glob(subs):
													if os.path.isdir(PP):
														os.chdir(PP)
														break
													elif os.path.islink(PP):
														os.chdir(os.path.realpath(PP))
														break
													elif os.path.isfile(PP):
														continue
											except:
												try:
													os.chdir(returnpathsub[0])
													P2 = pathlib.Path(returnpathsub[0])
													for PP2 in P2:
														if os.path.isdir(PP2):
															os.chdir(PP2)
															break
														elif os.path.islink(PP2):
															os.chdir(os.path.realpath(PP2))
															break
														elif os.path.isfile(PP2):
															continue
												except:
													try:
														os.chdir(WorkPath)
														P = pathlib.Path(WorkPath)
														for pp in P.glob(subs):
															os.chdir(pp)
															break
													except Exception as E:
														print('[{}] Path: {}'.format(E, os.getcwd()))
														sys.exit(0)
						for F in DetectDirectorys(os.listdir(), os.getcwd())[1]:
							if not '_#x' in F:
								one_convert(F)
						try:
							os.chdir(os.getcwd().replace(os.getcwd().split('/')[-1], ''))
						except FileNotFoundError:
							os.chdir('../')
					else:
						if not '_#x' in subs:
							one_convert(subs)
					try:
						os.chdir(os.getcwd().replace(os.getcwd().split('/')[-1], ''))
					except FileNotFoundError:
						try:
							os.chdir('../')
						except:
							os.chdir(WorkPath)
			else:
					break
		else:
			break

def RecursiveDirectory(f):
	if sys.argv[1] == './':
		sys.argv[1] = '.'
	pPath = os.getcwd()
	for DetectFile in DetectDirectorys(os.listdir(), os.getcwd())[1]:
		if not '_#x' in DetectFile:
			if os.path.isfile(DetectFile):
				one_convert(DetectFile)
	for i in DetectDirectorys(f, pPath)[0]:
		if os.path.isdir(i):
			os.chdir(i)
			if ''.join(DetectDirectorys(os.listdir(), os.getcwd())[0]) == '':
				WorkFiles(DetectDirectorys(os.listdir(), os.getcwd())[1])
			else:
				subPaths = os.getcwd()
				for s in DetectDirectorys(os.listdir(), os.getcwd())[0]:
					os.chdir(s)
					WorkFiles(DetectDirectorys(os.listdir(), os.getcwd())[1])
					os.chdir(subPaths)
		os.chdir(d_back)
	os.chdir(currentdir)
	print('\nDone!')

def main():
	global d_back
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
	d_back = os.getcwd()
	RecursiveDirectory(FilesList)

if __name__ == '__main__':
	main()