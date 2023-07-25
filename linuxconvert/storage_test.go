package linuxconvert

import (
	"os"
	"path"
	"path/filepath"
	"strings"
	"testing"
)

func TestApplicationPath(t *testing.T) {
	response, _ := GetApplicationPath("test_app")
	var expected string = path.Join(appStorage.Path, "applications", "test_app")

	t.Logf("recieved path: %s", response)
	t.Logf("expected path: %s", expected)

	if !strings.Contains(response, expected) {
		t.Errorf("%s is not in %s", expected, response)
	}

	DeleteStorageDir()
}

func TestArchiving(t *testing.T) {
	GetApplicationPath("test_app")

	ArchiveStorage()

	expected := path.Join(path.Dir(appStorage.Path), archiveName+".zip")

	var found bool = false
	// check for expected in dir
	walker := func(path string, info os.FileInfo, err error) error {
		if path == expected {
			found = true
		}
		return nil
	}
	err := filepath.Walk(path.Dir(appStorage.Path), walker)
	if err != nil {
		panic(err)
	}

	if !found {
		t.Errorf("%s not found in %s", expected, path.Dir(appStorage.Path))
	}

	DeleteStorageDir()
}
