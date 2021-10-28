#!python3
"""
Rename.py takes a diretory as an argument, it then walks that directory
and rename all music file with track number in their names.

Warning!!!!
	This script will also rename othe file types so be careful of the
	directory it is run in.
"""

import re
import os
import os.path
from sys import argv

pattern  = re.compile(r'^\d+.?\s')
os.chdir(argv[1])

for root, dirs, files in os.walk('.', topdown=False):
	for name in files:
		if pattern.match(name):
			path = os.path.join(root, name)
			os.rename(path, os.path.join(root, pattern.sub('', name)))