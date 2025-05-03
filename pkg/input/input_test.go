package input

import (
	"strings"
	"testing"
)

func TestExtractPackageName(t *testing.T) {
	testCases := []struct {
		input  string
		output string
	}{
		{
			input:  "com.samsung.android.app.clipboardedge\n",
			output: "com.samsung.android.app.clipboardedge",
		},
		{
			input:  "com.android.managedprovisioning",
			output: "com.android.managedprovisioning",
		},
		{
			input:  "EmergencyProvider",
			output: "",
		},
		{
			input:  "null",
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
	testInput := `
app:Device Health Services
package:com.google.android.apps.turbo
Launcher:null
app:Galaxy Themes
package:com.samsung.android.themestore
Launcher:null
app:Samsung Editing Assets
package:com.sec.android.app.ve.vebgm
Launcher:null
app:Group Sharing
package:com.samsung.android.mobileservice
Launcher:null
app:Clipboard edge
package:com.samsung.android.app.clipboardedge
Launcher:null		
	`

	expected := []string{
		"com.google.android.apps.turbo",
		"com.samsung.android.themestore",
		"com.sec.android.app.ve.vebgm",
		"com.samsung.android.mobileservice",
		"com.samsung.android.app.clipboardedge",
	}

	lines := strings.Split(testInput, "\n")
	got, err := Cleanse(lines)
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
