import os
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
	print(p.hexdigest())
