package input

import (
	"bufio"
	"os"
	"strings"
)

// package names in input file start with the prefix "com."
// extract the relevant bit and return.
func extractPackageName(line string) string {
	prefix := "com."

	if strings.HasPrefix(line, prefix) {
		return strings.TrimSpace(line)
	}

	return ""
}

func ReadContent(file *os.File) ([]string, error) {
	lines := []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		lines = append(lines, line)
	}

	if err := scanner.Err(); err != nil {
		return []string{}, err
	}

	return lines, nil
}

// extract clean package names from an input text file.
func Cleanse(lines []string) ([]string, error) {
	var pkgs []string

	for _, line := range lines {
		packageName := extractPackageName(line)
		if packageName != "" {
			pkgs = append(pkgs, packageName)
		}
	}

	return pkgs, nil
}
