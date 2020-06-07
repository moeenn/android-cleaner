# import Python standard modules
import sys
import getopt
import platform
import argparse

# import custom modules
import adb
import fsoperations


# get input and outfile file names from the user
def getArguments(argv):
	input_file = ""
	output_file = ""

	try:
		opts, args = getopt.getopt(argv, "hi:o", ["input=", "output="])
	except getopt.GetoptError:
		print("main.py --input <input_file> --output <output_file>")
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-h":
			print("main.py --input <input_file> --output <output_file>")
			sys.exit()
		elif opt in ("-i", "--input"):
			input_file = arg
		elif opt in ("-o", "--output"):
			output_file = arg

	return (input_file, output_file)

# def getArguments():
# 	parser = argparse.ArgumentParser()
# 	parser.add_argument("-i", "--input", action="store_true")


# only run on supported platforms
def check_platform_compatibility(supported_platforms):
	current_platform = platform.system()
	if current_platform not in supported_platforms:
		print(f"Unsupported Platform: Only the following Platforms are supported: {', '.join(supported_platforms)}")
		sys.exit(1)


# Using the application com.csdroid.pkg get the list of packages to be disabled
# this function takes the raw package details and creates a clean list of packages
def parse_disable_package_list(raw_package_name_file, clean_output_file):
	if not fsoperations.check_file_exists(raw_package_name_file):
		raise Exception(f"File Not Found: {raw_package_name_file}")
		return

	# create output file if it diesn't exist
	if not fsoperations.check_file_exists(clean_output_file):
		fsoperations.create_file(clean_output_file)

	with open(raw_package_name_file, "rt") as ifile:
		for line in ifile:
			line = line.strip()

			if line.startswith("package:"):
				line = line[8:]
				print(line);

				try:
					fsoperations.write_line(clean_output_file, line)
				except Exception as error:
					print(error)


if __name__ == "__main__":
	supported_platforms = ["Linux", "Darwin"]
	check_platform_compatibility(supported_platforms)

	# get arguments from the command line
	raw_package_name_file, clean_output_file = getArguments(sys.argv[1:])
	print("input file: ", raw_package_name_file)
	print("output file: ", clean_output_file)

	# try:
	# 	parse_disable_package_list(raw_package_name_file, clean_output_file)
	# 	# adb.disable_multiple_packages(clean_output_file)
	# except Exception as error:
	# 	print(error)