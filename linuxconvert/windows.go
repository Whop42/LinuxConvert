package linuxconvert

import (
	"fmt"
)

// returns a slice of the applications that could be found on windows
// TODO: untested! must have applications to test.
func FindInstalledApplications() {
	for _, app := range Applications {
		installed, err := app.CheckInstalledWindows()

		name, _ := app.GetName()
		fmt.Printf("application: %s (installed: %t) (err: %s)", name, installed, err)
		if err == nil && installed {
			AppStorage.InstalledApplications = append(AppStorage.InstalledApplications, app)
		}
	}
}

// copies configs of installed apps
// TODO: untested! must have applications to test.
func CopyInstalledConfigs() {
	for _, app := range AppStorage.InstalledApplications {
		app.CopyConfigsWindows()
	}
}

// what to run on windows
func Windows() {
	// FindInstalledApplications()
	// CopyInstalledConfigs()
	// ArchiveStorage()
	DeleteStorageDir()
}
