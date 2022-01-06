package input

import (
	"os"
	"testing"
)

func TestExtractPackageName(t *testing.T) {
	testCases := []struct {
		input  string
		output string
	}{
		{
			input:  "package:com.samsung.android.app.clipboardedge\n",
			output: "com.samsung.android.app.clipboardedge",
		},
		{
			input:  "package:com.android.managedprovisioning",
			output: "com.android.managedprovisioning",
		},
		{
			input:  "app:EmergencyProvider",
			output: "",
		},
		{
			input:  "Launcher:null",
			output: "",
		},
	}

	for _, testCase := range testCases {
		got := extractPackageName(testCase.input)
		if got != testCase.output {
			t.Errorf("Failed: Input: '%s' Expected: '%s' Output: '%s'", testCase.input, testCase.output, got)
		}
	}
}

func TestCleanse(t *testing.T) {
	testFilePath := "./test/sample.packages.txt"
	file, err := os.Open(testFilePath)
	defer file.Close()

	if err != nil {
		t.Errorf("Failed to open file: '%s'", testFilePath)
	}

	expected := []string{
		"com.google.android.apps.turbo",
		"com.samsung.android.themestore",
		"com.sec.android.app.ve.vebgm",
		"com.samsung.android.mobileservice",
		"com.samsung.android.app.clipboardedge",
	}

	got, err := Cleanse(file)
	if err != nil {
		t.Errorf("Failed to process input file: %v", err)
	}

	if len(expected) != len(got) {
		t.Errorf("Length of Expected slice different from Got slice: Got slice length: %v", len(got))
	}

	for i := 0; i < len(got); i++ {
		if got[i] != expected[i] {
			t.Errorf("Got result different from expected result: Got: '%s' Expected: '%s'", got[i], expected[i])
		}
	}
}
