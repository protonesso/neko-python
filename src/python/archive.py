import os
import sys
import zipfile
import tarfile

def CreateCheck(path, file):
	if file is None:
		print("File name wasn't specified")
		sys.exit(1)
	if path is None or not os.path.exists(path):
		print("Path wasn't specified or doesn't exist")
		sys.exit(1)

def UnpackCheck(path, file):
	if file is None or not os.path.exists(file):
		print("File wasn't specified or doesn't exist")
		sys.exit(1)
	if path is None or not os.path.exists(path):
		print("Path wasn't specified or doesn't exist")
		sys.exit(1)

def CreateZipArchive(path, file):
	CreateCheck(path, file)
	myzip = zipfile.ZipFile(file, 'w', zipfile.ZIP_DEFLATED)
	for root, dirs, files in os.walk(path):
		for file in files:
			myzip.write(os.path.join(root, file))
	myzip.close()

def UnpackZipArchive(path, file):
	UnpackCheck(path, file)
	with zipfile.ZipFile(file,"r") as myzip:
		myzip.extractall(path)

def ListZipContents(file):
	if file is None or not os.path.exists(file):
		print("File wasn't specified or doesn't exist")
		sys.exit(1)
	myzip = zipfile.ZipFile(file,"r")
	for member in myzip.namelist():
		print(member)
	myzip.close()

def CreateXZArchive(path, file):
	CreateCheck(path, file)
	with tarfile.open(file, "w:xz") as mytar:
		mytar.add(path, arcname=os.path.basename(path))

def UnpackXZArchive(path, file):
	UnpackCheck(path, file)
	mytar = tarfile.open(file)
	mytar.extractall(path)
	mytar.close()

def ListXZContents(file):
	if file is None or not os.path.exists(file):
		print("File wasn't specified or doesn't exist")
		sys.exit(1)
	mytar = tarfile.open(file)
	for member in mytar.getnames():
		print(member)
	mytar.close()
