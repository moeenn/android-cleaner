# standard modules
import sys
import errno
import getopt
import platform
import argparse

# custom modules
import adb
import fsoperations

def display_help():
	print("usage: \nmain.py --input <input_file> --output <output_file>")


# get input and outfile file names from the user
def getArguments(argv):
	input_file = ""
	output_file = ""

	try:
		opts, args = getopt.getopt(argv, "hi:o", ["input=", "output="])
	except getopt.GetoptError:
		display_help()
		sys.exit(2)

	for opt, arg in opts:
		if opt == "-h":
			display_help()
			sys.exit()
		elif opt in ("-i", "--input"):
			input_file = arg
		elif opt in ("-o", "--output"):
			output_file = arg

	if not input_file:
		print("Please provide an Input File containing Raw Package Details")
		display_help()
		sys.exit(errno.EINVAL)

	if not output_file:
		output_file = "clean_packages.txt"

	return (input_file, output_file)


# only run on supported platforms
def check_platform_compatibility(supported_platforms):
	current_platform = platform.system()
	if current_platform not in supported_platforms:
		print(f"Unsupported Platform: Only the following Platforms are supported:")
		print(', '.join(supported_platforms))

		sys.exit(errno.EPROTONOSUPPORT)


if __name__ == "__main__":
	supported_platforms = ["Linux", "Darwin"]
	check_platform_compatibility(supported_platforms)

	# get arguments from the command line
	raw_package_name_file, clean_output_file = getArguments(sys.argv[1:])
	print("input file: ", raw_package_name_file)
	print("output file: ", clean_output_file)

	adb.parse_disable_package_list(raw_package_name_file, clean_output_file)
	# adb.disable_multiple_packages(clean_output_file)

	sys.exit(0)