package adb

import (
	"errors"
	"testing"
)

func TestInInstalled(t *testing.T) {
	testCases := []struct {
		input    []string
		executor executor
		output   bool
	}{
		{
			input: []string{"which", "adb"},
			executor: func(args ...string) (string, error) {
				return "", errors.New("Error: adb not found")
			},
			output: false,
		},
		{
			input: []string{"which", "adb"},
			executor: func(args ...string) (string, error) {
				return "/bin/adb", nil
			},
			output: true,
		},
		{
			input: []string{"which", "adb"},
			executor: func(args ...string) (string, error) {
				return "", nil
			},
			output: false,
		},
	}

	for _, testCase := range testCases {
		got := IsInstalled(testCase.executor)

		if got != testCase.output {
			t.Errorf("Failed: Expected: %v Got: %v", testCase.output, got)
		}
	}
}
