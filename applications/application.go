package applications

type Application interface {
	IsInstalledWindows() (bool, error)
	CopyConfigFiles(string) error
	InstallLinux() error
	GetApplicationInformation() ApplicationInformation
}

/*
maybe a little redundant, idgaf. it's only reused in CreateDesktopFile so
it's not important enough to think about.

TODO: maybe add some more here?
- who implemented
*/
type ApplicationInformation struct {
	Name, Developer, Icon string
}
