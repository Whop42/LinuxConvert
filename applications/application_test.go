package applications

import (
	"fmt"
	"os"
	"testing"
)

func TestCreateDesktopFile(t *testing.T) {
	destDir := t.TempDir() // automatically cleaned up <3

	testDe := DesktopEntry{
		Name:            "Test Application",
		GenericName:     "Test Generic Name",
		ExecPath:        "/path/to/executable",
		Icon:            "test-icon",
		ApplicationType: "Application",
		Categories:      "Utility;",
	}

	filePath, err := createDesktopFile(testDe, destDir)

	if err != nil {
		t.Errorf("could not create .desktop file")
	}

	expectedContent := fmt.Sprintf("[Desktop Entry]\nName=%s\nGenericName=%s\nExec=%s\nIcon=%s\nType=%s\nCategories=%s",
		testDe.Name, testDe.GenericName, testDe.ExecPath, testDe.Icon, testDe.ApplicationType, testDe.Categories)

	fileContent, err := os.ReadFile(filePath)

	if err != nil {
		t.Errorf("error reading desktop file: %v", err)
	}

	if string(fileContent) != expectedContent {
		t.Errorf("desktop file content does not match expected: got %q, want %q", string(fileContent), expectedContent)
	}
}
