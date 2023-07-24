package linuxconvert

import (
	"path"
	"strings"
	"testing"
)

func TestApplicationPath(t *testing.T) {
	response, _ := GetApplicationPath("test_app")
	var expected string = path.Join("applications", "test_app")

	t.Logf("recieved path: %s", response)

	if !strings.Contains(response, expected) {
		t.Errorf("%s is not in %s", expected, response)
	}

	DeleteStorageDir()
}
