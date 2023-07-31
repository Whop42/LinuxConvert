package linuxconvert

import (
	"errors"
	"fmt"
)

type Application interface {
	CheckInstalledWindows() (bool, error)
	CopyConfigsWindows() error
	GetPackageLinux() (Package, error)
	InstallConfigsLinux() error
	GetName() (string, error)
	SetName(string) error
}

type Package struct {
	name           string
	packageManager string // which package manager to download from: apt, snap, flatpak, etc.
}

// applications that are available
var Applications []Application = []Application{}

func FindApplicationByName(name string) (Application, error) {
	for _, application := range Applications {
		// TODO: handle error once errors are handled by function
		if appName, _ := application.GetName(); appName == name {
			return application, nil
		}
	}
	return nil, errors.New(fmt.Sprintf("Application %s not found", name))
}

// ignores the fact that the element may not be in the slice
func RemoveApplicationFromSlice(a Application, s []Application) (out []Application) {
	j := 0
	for _, i := range s {
		// copy over the elements that are NOT a
		if i != a {
			s[j] = i
			j++
		}
	}
	out = s[:j]
	return out
}
