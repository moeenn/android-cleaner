package input

import (
	"bufio"
	"os"
	"strings"
)

/**
 *  package names in input file start with the prefix "package:"
 *  extract the relevant bit and return
 */
func extractPackageName(line string) string {
	prefix := "package:"

	if strings.HasPrefix(line, prefix) {
		line := line[len(prefix):]
		return strings.TrimSpace(line)
	}

	return ""
}

/**
 *  extract clean package names from an input text file
 *
 */
func Cleanse(file *os.File) ([]string, error) {
	var pkgs []string
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		packageName := extractPackageName(line)
		if packageName != "" {
			pkgs = append(pkgs, packageName)
		}
	}

	if err := scanner.Err(); err != nil {
		return []string{}, err
	}

	return pkgs, nil
}
