package linuxconvert

import (
	"path"
	"strings"
	"testing"
)

func TestApplicationPath(t *testing.T) {
	response, _ := GetApplicationPath("test_app")
	var expected string = path.Join(AppStorage.Path, "applications", "test_app")

	t.Logf("recieved path: %s", response)
	t.Logf("expected path: %s", expected)

	if !strings.Contains(response, expected) {
		t.Errorf("%s is not in %s", expected, response)
	}

	DeleteStorageDir()
}

// TODO: test basic usage of ReadUnzippedDir
// func ReadUnzippedDirTest1(t *testing.T) {
// 	return
// }
