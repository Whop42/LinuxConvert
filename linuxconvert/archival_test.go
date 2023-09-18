package linuxconvert

import (
	"os"
	"path"
	"path/filepath"
	"testing"
)

func TestArchiving(t *testing.T) {
	GetApplicationPath("test_app")

	ArchiveStorage()

	expected := path.Join(path.Dir(AppStorage.Path), ArchiveName+".zip")

	var found bool = false
	// check for expected in dir
	walker := func(path string, info os.FileInfo, err error) error {
		if path == expected {
			found = true
		}
		return nil
	}
	err := filepath.Walk(path.Dir(AppStorage.Path), walker)
	if err != nil {
		panic(err)
	}

	if !found {
		t.Errorf("%s not found in %s", expected, path.Dir(AppStorage.Path))
	}

	DeleteStorageDir()
}

func TestExtraction(t *testing.T) {
	GetApplicationPath("test_app")

	ArchiveStorage()

	ExtractArchive(path.Join(path.Dir(AppStorage.Path), ArchiveName+".zip"))

	expected := path.Join(path.Dir(AppStorage.Path), ArchiveName)

	var found bool = false
	// check for expected in dir
	walker := func(path string, info os.FileInfo, err error) error {
		if path == expected {
			found = true
		}
		return nil
	}

	err := filepath.Walk(path.Dir(AppStorage.Path), walker)
	if err != nil {
		panic(err)
	}

	if !found {
		t.Errorf("%s not found in %s", expected, path.Dir(AppStorage.Path))
	}

	DeleteStorageDir()
}
