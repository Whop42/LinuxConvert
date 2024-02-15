package applications

/*
Example app for debug purposes
*/

type ExampleApplication struct {
	Application
}

func (a ExampleApplication) GetApplicationInformation() ApplicationInformation {
	return ApplicationInformation{
		Name:      "Example Application",
		Developer: "whop42",
		Icon:      "file",
	}
}

func (a ExampleApplication) IsInstalledWindows() (bool, error) {
	return false, nil
}

func (a ExampleApplication) CopyConfigFiles(destDir string) error {
	return nil
}

func (a ExampleApplication) InstallLinux() error {
	return nil
}
