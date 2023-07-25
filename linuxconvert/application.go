package linuxconvert

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
