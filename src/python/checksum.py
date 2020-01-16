import os, sys
from hashlib import blake2b

def CheckFile(file):
	if file is None or not os.path.exists(file):
		print("File wasn't specified or doesn't exist")
		sys.exit(1)

def GenBlake2BSum(file):
	CheckFile(file)
	p = blake2b()
	with open(file, "rb") as f:
		f = f.read()
		p.update(f)
	return p.hexdigest()

def CompareBlake2BSum(file, hash):
	if hash is None:
		print("Hash wasn't specified")
		sys.exit(1)
	p = GenBlake2BSum(file)
	if p != hash:
		print("File hash and specfied hash are not same")
		sys.exit(1)
