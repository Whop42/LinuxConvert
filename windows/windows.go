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
	AvailableApplications, InstalledApplications, CollectedApplications []apps.Application
	StorageDir                                                          string
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
		AvailableApplications: apps.GetSupportedApplications(), // debug purposes
		InstalledApplications: make([]apps.Application, 0),
		CollectedApplications: make([]apps.Application, 0),
		StorageDir:            filepath.Join(os.TempDir(), "linuxconvert-"+fmt.Sprint(time.Now().Unix())),
	}

	// ensure storage dir is created
	os.MkdirAll(ws.StorageDir, os.ModeDir)

	util.InfoLogger.Printf("created Windows State: storage directory = %s\n", ws.StorageDir)

	return &ws
}

/*
GetApplications finds every installed application

output:
- ws.InstalledApplications updated
*/
func GetApplications(ws *WindowsState) {
	supportedApplications := apps.GetSupportedApplications()

	for _, a := range supportedApplications {
		installed, err := a.IsInstalledWindows() //TODO: concurrent method?
		if installed {
			ws.InstalledApplications = append(ws.InstalledApplications, a)
			util.InfoLogger.Printf("%s found", a.GetApplicationInformation().Name)
		}
		if err != nil {
			//TODO: handle error better: shouldn't just panic here
			util.ErrorLogger.Panicf("detecting of %s installation status failed", a.GetApplicationInformation().Name)
		}
	}

	util.InfoLogger.Printf("these installed applications were found: %s\n", fmt.Sprint(ws.InstalledApplications))
	//TODO: unsupported applications system
}

/*
CollectApplicationConfigs calls each Application's CopyConfigs() function with the correct dir

output:
- config files copied, directory structure put in place
- ws.CollectedApplications updated
*/
func CollectApplicationConfigs(ws *WindowsState) {
	//TODO: create test case

	// create root directory structure
	applicationsPath := filepath.Join(ws.StorageDir, "applications")
	err := os.Mkdir(applicationsPath, os.ModeDir)
	if err != nil {
		util.ErrorLogger.Panicf("couldn't create applications folder. error: %s\n", err)
	}

	// create config.json
	configJSONPath := filepath.Join(ws.StorageDir, "config.json")
	configJSON, err := os.Create(configJSONPath)
	if err != nil {
		util.ErrorLogger.Panicf("couldn't create config.json. error: %s\n", err)
	}
	defer configJSON.Close()

	// copy configs from supported applications
	for _, a := range ws.InstalledApplications {
		appDir := filepath.Join(applicationsPath, a.GetApplicationInformation().Name)
		err = os.Mkdir(appDir, os.ModeDir)
		if err != nil {
			util.ErrorLogger.Panicf("couldn't create %s. err: %s\n", appDir, err)
		}

		err = a.CopyConfigFiles(appDir)
		if err != nil {
			util.ErrorLogger.Panicf("couldn't copy config files from %s to %s\n", a.GetApplicationInformation().Name, appDir)
		}

		ws.CollectedApplications = append(ws.CollectedApplications, a)
		util.InfoLogger.Printf("%s configs collected", a.GetApplicationInformation().Name)
	}

	util.InfoLogger.Printf("copied config files for: %s\n", fmt.Sprint(ws.CollectedApplications))

	//TODO: unsupported application system
}
