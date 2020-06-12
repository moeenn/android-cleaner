import adb
import filecmp
from os import remove

def test_parse_disable_package_list():
	mock_input = "./tests/raw_package_details.txt"
	produced_output = "./tests/example_output.txt"
	expected_output = "./tests/clean_package_details.txt"

	adb.parse_disable_package_list(mock_input, produced_output)
	is_same = filecmp.cmp(produced_output, expected_output)
	remove(produced_output)
	assert is_same
