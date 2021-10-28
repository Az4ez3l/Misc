import os
import os.path


# Deletes all non-english srt subtitles from directory.
# Needs to be run in the directory containing the subtitles.

for root, dirs, files in os.walk('.', topdown=False):
	for name in files:
		if ".srt" in name and "en." not in name:
			path = os.path.join(root, name)
			os.remove(path)


print("done")