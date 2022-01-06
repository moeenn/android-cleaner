package adb

import (
	"strings"
)

type executor func(...string) (string, error)

func IsInstalled(exec executor) bool {
	output, err := exec("which", "adb")
	if err != nil {
		return false
	}

	if strings.TrimSpace(output) == "" {
		return false
	}

	return true
}
