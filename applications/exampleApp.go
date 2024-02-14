package applications

/*
Example app for debug purposes
Specify all of the info in a constructor
*/

type ExampleApplication struct {
	Application
}

func (a ExampleApplication) IsInstalledWindows() (bool, error) {
	return false, nil
}

func (a ExampleApplication) CopyConfigFiles() error {
	return nil
}

func (a ExampleApplication) InstallLinux() error {
	return nil
}
