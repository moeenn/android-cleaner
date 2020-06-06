from adb import disable_multiple_packages
import fsoperations


# Using the application com.csdroid.pkg get the list of packages to be disabled
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
	raw_package_name_file = "./remove_apps"
	clean_output_file = "./clean_remove_packages"

	try:
		parse_disable_package_list(raw_package_name_file, clean_output_file)
		# disable_multiple_packages(clean_output_file)
	except Exception as error:
		print(error)