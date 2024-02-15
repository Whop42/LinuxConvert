package windows

import (
	"fmt"
	"os"
	"path/filepath"
	"time"

	apps "github.com/whop42/linuxconvert/applications"
	"github.com/whop42/linuxconvert/util"
)

type WindowsState struct {
	InstalledApplications, CollectedApplications []apps.Application
	StorageDir                                   string
}

/*
GenerateWindowsState returns a reference to a fresh windows state

output:
- WindowsState
  - InstalledApplications: empty slice of Applications
  - CollectedApplications: empty slice of Applications
  - StorageDir: <temp dir>/linuxconvert-<unix time>
*/
func GenerateWindowsState() *WindowsState {
	ws := WindowsState{
		InstalledApplications: make([]apps.Application, 0),
		CollectedApplications: make([]apps.Application, 0),
		StorageDir:            filepath.Join(os.TempDir(), "linuxconvert-"+fmt.Sprint(time.Now().Unix())),
	}

	// ensure storage dir is created
	os.MkdirAll(ws.StorageDir, os.ModeDir)

	util.InfoLogger.Printf("Created Windows State: storage directory = %s", ws.StorageDir)
	return &ws
}

/*
GetApplications finds every installed application

output:
- []app.Application: a slice of installed applications
- error
*/
func GetApplications(ws *WindowsState) {
	//TODO: create test case

	supportedApplications := apps.GetSupportedApplications()

	for _, a := range supportedApplications {
		installed, err := a.IsInstalledWindows() //TODO: concurrent method?
		if installed {
			ws.InstalledApplications = append(ws.InstalledApplications, a)
		}
		if err != nil {
			//TODO: handle error better
			util.ErrorLogger.Printf("detecting of %s is installed", a.GetApplicationInformation().Name)
		}
	}
}

func CollectApplicationConfigs(ws *WindowsState) {
	//TODO: implement

	// create root directory structure
}
