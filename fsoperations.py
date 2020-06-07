import os

# check is a file exists
def check_file_exists(filepath):
	return os.path.exists(filepath)


# create a file on the path specified
def create_file(filepath):
	if check_file_exists(filepath):
		raise Exception(f"File already Exists: {filepath}")
		return

	os.mknod(filepath)


# write a single line to the file provided
def write_line(filename, line):
	if not check_file_exists(filename):
		raise Exception(f"File Not Found: {filename}")
		return

	# append to output file NOT overwrite
	with open(filename, "at") as ofile:
			line = line.strip()
			ofile.write(f"{line}\n")
