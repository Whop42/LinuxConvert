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
- ws.InstalledApplications updated
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
	for _, app := range ws.InstalledApplications {
		appDir := filepath.Join(applicationsPath, app.GetApplicationInformation().Name)
		err = os.Mkdir(appDir, os.ModeDir)
		if err != nil {
			util.ErrorLogger.Panicf("couldn't create %s. err: %s\n", appDir, err)
		}

		err = app.CopyConfigFiles(appDir)
		if err != nil {
			util.ErrorLogger.Panicf("couldn't copy config files from %s to %s\n", app.GetApplicationInformation().Name, appDir)
		}

		ws.CollectedApplications = append(ws.CollectedApplications, app)
	}

	//TODO: unsupported application system
}
