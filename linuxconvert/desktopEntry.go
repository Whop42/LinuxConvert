package linuxconvert

import (
	"fmt"
	"os"
	"path/filepath"

	"github.com/whop42/linuxconvert/util"
)

type DesktopEntry struct {
	Name, GenericName, ExecPath, ApplicationType, Categories, Icon string
}

/*
createDesktopFile creates a Desktop Entry given a struct of type desktopEntry

params:
- de: Desktop Entry struct
- destDir: directory to dump the desktop entry in

output:
- string: filepath where .desktop file was dumped
- error

example:

	createDesktopFile(desktopEntry{
		Name: "Example Application",
		GenericName: "Example",
		ExecPath: "/usr/bin/cat",
		...
	})
*/
func createDesktopFile(de DesktopEntry, destDir string) (string, error) {
	filename := filepath.Join(destDir, de.Name+".desktop")
	file, err := os.Create(filename)
	if err != nil {
		return filename, err
	}
	defer file.Close()

	_, err = fmt.Fprintf(file,
		"[Desktop Entry]\nName=%s\nGenericName=%s\nExec=%s\nIcon=%s\nType=%s\nCategories=%s;",
		de.Name, de.GenericName, de.ExecPath, de.Icon, de.ApplicationType, de.Categories)

	if err != nil {

		return filename, err
	}

	util.InfoLogger.Printf("Desktop Entry %s created", filepath.Base(filename))

	return filename, nil
}
