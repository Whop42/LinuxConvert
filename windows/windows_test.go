package windows

import (
	"fmt"
	"os"
	"slices"
	"testing"

	apps "github.com/whop42/linuxconvert/applications"
)

func TestGetApplications(t *testing.T) {
	// TODO: implement

	expectedResult := []apps.Application{}
	expectedResult = append(expectedResult, apps.ExampleApplication{})

	ws := GenerateWindowsState()

	ws.AvailableApplications = expectedResult

	defer os.RemoveAll(ws.StorageDir)

	GetApplications(ws)

	if !slices.Equal(expectedResult, ws.AvailableApplications) {
		t.Error("AvailableApplications was changed")
	}

	if !slices.Equal(expectedResult, ws.InstalledApplications) {
		t.Errorf("Expected %s, got %s", fmt.Sprint(expectedResult), fmt.Sprint(ws.InstalledApplications))
	}

	t.Logf("Expected %s, got %s", fmt.Sprint(expectedResult), fmt.Sprint(ws.InstalledApplications))
}

func TestCollectApplicationConfigs(t *testing.T) {
	// TODO: implement (very complicated test smh)
	t.Skip("TODO: implement")
}
