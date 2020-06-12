import os
import sys
import errno


# check is a file exists
def check_file_exists(filepath):
	return os.path.exists(filepath)


# create a file on the path specified
def create_file(filepath):
	if check_file_exists(filepath):
		print(f"File already Exists: {filepath}")
		sys.exit(errno.EEXIST)

	with open(filepath, "wt") as file:
			pass


# write a single line to the file provided
def write_line(filename, line):
	if not check_file_exists(filename):
		print(f"File Not Found: {filename}")
		sys.exit(errno.ENOENT)

	# append to output file NOT overwrite
	with open(filename, "at") as ofile:
			line = line.strip()
			ofile.write(f"{line}\n")
