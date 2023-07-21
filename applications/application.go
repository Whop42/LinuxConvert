package applications

import (
	"path"
)

type Application interface {
	CheckInstalledWindows() (bool, error)
	CopyConfigsWindows() error
	GetPackageLinux() (string, error)
	InstallConfigsLinux() error
	GetName() (string, error)
	SetName(string) error
}

//TODO: move the rest to somewhere better.

type Storage struct {
	Path            string
	ApplicationList []Application
}

var s Storage = Storage{
	Path:            "temp_dir",
	ApplicationList: []Application{},
}

func GetApplicationPath(appName string) (string, error) {
	return path.Join(s.Path, "applications", appName), nil
}
