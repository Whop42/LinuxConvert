package linuxconvert

type Application interface {
	CheckInstalledWindows() (bool, error)
	CopyConfigsWindows() error
	GetPackageLinux() (string, error)
	InstallConfigsLinux() error
	GetName() (string, error)
	SetName(string) error
}

// applications that are available
var Applications []Application = []Application{}
