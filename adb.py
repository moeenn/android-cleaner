import subprocess

# disable a single package using adb
def disable_package(package_name):
	command_string = f"adb shell pm disable-user {package_name}"
	command = subprocess.run(command_string, shell=True, capture_output=True)
	print(command.stdout.decode())


# disable all packages listed in a file
def disable_multiple_packages(package_names_file):
	if not check_file_exists(package_names_file):
		raise Exception(f"File Not Found: {package_names_file}")
		return

	with open(package_names_file, "rt") as ifile:
		for package in ifile:
			disable_package(package.strip())
