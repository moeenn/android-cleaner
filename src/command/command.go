package command

import (
	"os/exec"
)

func Executor(args ...string) (string, error) {
	cmd := exec.Command(args[0], args[1:]...)
	stdOut, err := cmd.Output()

	if err != nil {
		return "", err
	}

	return string(stdOut[:]), nil
}
