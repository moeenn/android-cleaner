import fsoperations
from os import remove

def test_check_file_exists():
	test_file = "./tests/example_file_exists.txt"
	assert fsoperations.check_file_exists(test_file) == True


def test_create_file():
	test_file = "./tests/example_create_file.txt"
	fsoperations.create_file(test_file)
	assert fsoperations.check_file_exists(test_file) == True
	remove(test_file)


def test_write_line():
	test_file = "./tests/example_write_line.txt"
	test_line = "this is a test line"

	fsoperations.create_file(test_file)

	fsoperations.write_line(test_file, test_line)
	fsoperations.write_line(test_file, test_line)

	expected_file_content = f"{test_line}\n{test_line}\n"
	actual_content = ""

	with open(test_file, "rt") as testfile:
		for line in testfile:
			actual_content += line

	assert expected_file_content == actual_content
	remove(test_file)
