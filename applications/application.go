package applications

type Application interface {
	IsInstalledWindows() (bool, error)
	CopyConfigFiles() error
	InstallLinux() error
}
