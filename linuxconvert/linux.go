package linuxconvert

import apps "github.com/whop42/linuxconvert/applications"

// do any necessary bootstrapping work pre-install
func Bootstrap() error {
	return nil
}

// will get .zip location from user in the future
func GetZipPath() (string, error) {
	return "", nil
}

/*
- make a dir for the data to live in temporarily -> `~/.local/share/linuxconvert`
- extract the .zip to that, applications should look like `~/.local/share/linuxconvert/supported-applications`
*/
func Extract() error {
	return nil
}

// iterate over every folder in `supported-applications` and match it to an `Application` type,
// then instantiate that with the information in the folder and store the object in a list that
// is given to the install step
func LoadApplications() ([]apps.SupportedApplication, error) {
	return nil, nil
}

/*
- call `installLinux()` on each supported application slated to be installed
  - if it works, mark the application as installed
  - if it doesn't, this will show which applications were not installed at the end
  - store logs?

- call `createDesktopFile(dest)` on each that properly installed to create a .desktop file
*/
func InstallApplications(installedApplications []apps.SupportedApplication) error {
	return nil
}
