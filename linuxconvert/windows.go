package linuxconvert

// returns a slice of the applications that could be found on windows
func FindInstalledApplications() {
	for _, app := range Applications {
		installed, err := app.CheckInstalledWindows()
		if err == nil && installed {
			appStorage.InstalledApplications = append(appStorage.InstalledApplications, app)
		}
	}
}

// copies configs of installed apps
func CopyInstalledConfigs() {
	for _, app := range appStorage.InstalledApplications {
		app.CopyConfigsWindows()
	}
}
