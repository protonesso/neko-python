import os
import re
import json

def CheckFilePattern(file, pattern):
	if file is None or not os.path.exists(file):
		print("File wasn't specified or doesn't exist")
		sys.exit(1)
	if pattern is None:
		print("Pattern name wasn't specified")
		sys.exit(1)

def CommentVariable(file, pattern):
	CheckFilePattern(file, pattern)
	with open(file, "r+") as kagamibuild:
		text = kagamibuild.read().strip()
		p = re.search("# %s:(.*)" % pattern, text)
		if p:
			p = p.group(0)
			p = p.replace("# %s:" % pattern, "")
			p = p.lstrip()
			print(p)

def JsonVariable(file, pattern, pattern2):
	CheckFilePattern(file, pattern)
	with open(file, "r+") as jsonfile:
		data = json.load(jsonfile)
		if data:
			if data["%s" % pattern]:
				p = data["%s" % pattern]
				p = p["%s" % pattern2]
				print(p)
