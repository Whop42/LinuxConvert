package windows

import (
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
func GenerateWindowsState() (*WindowsState, error) {
	ws := WindowsState{
		InstalledApplications: make([]apps.Application, 0),
		CollectedApplications: make([]apps.Application, 0),
		StorageDir:            filepath.Join(os.TempDir(), "linuxconvert-"+string(time.Now().Unix())),
	}

	util.InfoLogger.Printf("Created Windows State: storage directory = %s", ws.StorageDir)
	return &ws, nil
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
			installedApplications = append(installedApplications, a)
		}
		if err != nil {
			//TODO: handle error
		}
	}
}

func CollectApplicationConfigs(ws *WindowsState) {
	//TODO: implement
}
