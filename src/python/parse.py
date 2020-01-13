import os
import re

def CommentVariable(file, pattern):
	with open(file, "r+") as kagamibuild:
		text = kagamibuild.read().strip()
		p = re.search("# %s:(.*)" % pattern, text)
		p = p.group(0)
		p = p.replace("# %s:" % pattern, "")
		p = p.lstrip()
		print(p)
