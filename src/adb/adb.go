package adb

import (
	"strings"
)

type executor func(...string) (string, error)

/**
 *  checks if adb is installed on the system or not
 *
 */
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

/**
 *  disable a given package on the connected android device
 *
 */
func DisablePackage(pkg string, exec executor) error {
	_, err := exec("adb", "shell", "pm", "disable-user", pkg)
	return err
}
