import adb
import filecmp
from os import remove

def test_parse_disable_package_list():
	mock_input = "./test_files/raw_package_details.txt"
	produced_output = "./test_files/example_output.txt"
	expected_output = "./test_files/clean_package_details.txt"

	adb.parse_disable_package_list(mock_input, produced_output)
	is_same = filecmp.cmp(produced_output, expected_output)
	remove(produced_output)
	assert is_same
