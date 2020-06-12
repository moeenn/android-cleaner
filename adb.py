# standard modules
import subprocess
import sys
import errno

# custom modules
import fsoperations


# disable a single package using adb
def disable_package(package_name):
	command_string = f"adb shell pm disable-user {package_name}"
	command = subprocess.run(command_string, shell=True, capture_output=True)
	print(command.stdout.decode())


# disable all packages listed in a file
def disable_multiple_packages(package_names_file):
	if not check_file_exists(package_names_file):
		print(f"File Not Found: {package_names_file}")
		sys.exit(errno.ENOENT)

	with open(package_names_file, "rt") as ifile:
		for package in ifile:
			disable_package(package.strip())


# Using the application com.csdroid.pkg get the list of packages to be disabled
# this function takes the raw package details and creates a clean list of packages
def parse_disable_package_list(raw_package_name_file, clean_output_file):
	if not fsoperations.check_file_exists(raw_package_name_file):
		print(f"File Not Found: {raw_package_name_file}")
		sys.exit(errno.ENOENT)

	# create output file if it diesn't exist
	if not fsoperations.check_file_exists(clean_output_file):
		fsoperations.create_file(clean_output_file)

	with open(raw_package_name_file, "rt") as ifile:
		for line in ifile:
			line = line.strip()

			if line.startswith("package:"):
				line = line[8:]
				print(line);
				fsoperations.write_line(clean_output_file, line)