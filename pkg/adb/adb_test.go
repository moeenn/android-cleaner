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

func TestDisablePackage(t *testing.T) {
	testCases := []struct {
		input         string
		executor      executor
		outputIsError bool
	}{
		{
			input: "com.google.android.apps.turbo",
			executor: func(args ...string) (string, error) {
				return "", errors.New("Package not found")
			},
			outputIsError: true,
		},
		{
			input: "com.google.android.apps.turbo",
			executor: func(args ...string) (string, error) {
				return "package disabled", nil
			},
			outputIsError: false,
		},
	}

	for _, testCase := range testCases {
		got := DisablePackage(testCase.input, testCase.executor)

		if testCase.outputIsError {
			if got == nil {
				t.Errorf("Failed: Expected error to be thrown but no error was thrown")
			}
		}

		if !testCase.outputIsError {
			if got != nil {
				t.Errorf("Failed: Didn't expect an error but an error was thrown")
			}
		}
	}
}
