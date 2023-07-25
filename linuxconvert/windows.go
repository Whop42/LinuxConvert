package linuxconvert

// returns a slice of the applications that could be found on windows
// TODO: untested! must have applications to test.
func FindInstalledApplications() {
	for _, app := range Applications {
		installed, err := app.CheckInstalledWindows()
		if err == nil && installed {
			appStorage.InstalledApplications = append(appStorage.InstalledApplications, app)
		}
	}
}

// copies configs of installed apps
// TODO: untested! must have applications to test.
func CopyInstalledConfigs() {
	for _, app := range appStorage.InstalledApplications {
		app.CopyConfigsWindows()
	}
}

// what to run on windows
func Windows() {
	FindInstalledApplications()
	CopyInstalledConfigs()
	ArchiveStorage()
}
