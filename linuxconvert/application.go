package linuxconvert

import (
	"fmt"
)

type Application interface {
	CheckInstalledWindows() (bool, error)
	CopyConfigsWindows() error
	PreInstallLinux() error
	GetPackageLinux() (Package, error)
	InstallConfigsLinux() error
	GetName() (string, error)
	SetName(string) error
}

type Package struct {
	Name           string
	PackageManager string // which package manager to download from: apt, snap, flatpak, etc.
}

// applications that are available
var Applications []Application = []Application{}

func AssignApplications() {
	Applications = append(Applications, &VSCode{})
}

func FindApplicationByName(name string) (Application, error) {
	for _, application := range Applications {
		// TODO: handle error once errors are handled by function
		if appName, _ := application.GetName(); appName == name {
			return application, nil
		}
	}
	return nil, fmt.Errorf("Application %s not found", name)
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

// test application!! do not use!!
// type TestApp struct {
// 	// fields here
// }

// func (a *TestApp) CheckInstalledWindows() (bool, error) {
// 	return true, nil
// }

// func (a *TestApp) CopyConfigsWindows() error {
// 	return nil
// }

// func (a *TestApp) GetPackageLinux() (Package, error) {
// 	return Package{
// 		Name:           "test_app",
// 		PackageManager: "flatpak",
// 	}, nil
// }

// func (a *TestApp) InstallConfigsLinux() error {
// 	return nil
// }

// func (a *TestApp) GetName() (string, error) {
// 	return "test app1", nil
// }

// func (a *TestApp) SetName(name string) error {
// 	return nil
// }
