package util

import (
	"os"
	"path/filepath"
	"testing"
)

func TestArchiveAndExtract(t *testing.T) {
	// Create a temporary directory for testing
	tempDir := t.TempDir()

	// Create some test files and directories inside the temporary directory
	testFiles := []struct {
		Name, Content string
	}{
		{"file1.txt", "This is file 1."},
		{"file2.txt", "This is file 2."},
	}

	for _, file := range testFiles {
		filePath := filepath.Join(tempDir, file.Name)
		t.Error(filePath)
		if err := os.WriteFile(filePath, []byte(file.Content), os.ModeAppend); err != nil {
			t.Fatalf("Error creating test file %s: %v", file.Name, err)
		}
	}

	// Define paths for the archive and extracted files
	archivePath := filepath.Join(tempDir, "test_archive.zip")
	extractedDir := filepath.Join(tempDir, "extracted")

	// Test Archive Functionality
	Archive(tempDir, archivePath)

	// Verify that the archive file is created
	if _, err := os.Stat(archivePath); os.IsNotExist(err) {
		t.Errorf("Archive file not created: %v", err)
	}

	// Test Extract Functionality
	Extract(archivePath, extractedDir)

	// Verify that all files and directories from the archive are successfully extracted
	for _, file := range testFiles {
		filePath := filepath.Join(extractedDir, file.Name)
		if _, err := os.Stat(filePath); os.IsNotExist(err) {
			t.Errorf("Expected file %s not found in extracted directory: %v", file.Name, err)
		}
	}

	// Verify that the content of the extracted files matches the content of the original files
	for _, file := range testFiles {
		filePath := filepath.Join(extractedDir, file.Name)
		content, err := os.ReadFile(filePath)
		if err != nil {
			t.Errorf("Error reading extracted file %s: %v", file.Name, err)
		}
		if string(content) != file.Content {
			t.Errorf("Content of extracted file %s does not match expected content", file.Name)
		}
	}
}
