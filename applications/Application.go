package applications

import (
	"fmt"
	"os"
)

type Application interface {
	IsInstalledWindows() (bool, error)
	CopyConfigFiles() error
	InstallLinux() error
}

type desktopEntry struct {
	Name, GenericName, ExecPath, ApplicationType, Categories, Icon string
}

/*
createDesktopFile creates a Desktop Entry given a struct of type desktopEntry

example:
createDesktopFile(desktopEntry{Name=})
*/
func createDesktopFile(de desktopEntry) error {
	file, err := os.Create(de.Name + ".desktop") // TODO: change location
	if err != nil {
		return err
	}
	defer file.Close()

	_, err = fmt.Fprintf(file,
		"[Desktop Entry]\nName=%s\nExec=%s\nIcon=%s\nType=%s\nCategories=%s;",
		de.Name, de.ExecPath, de.Icon, de.ApplicationType, de.Categories)
	if err != nil {
		return err
	}
	return nil
}
