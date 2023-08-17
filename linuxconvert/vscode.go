package linuxconvert

import (
	"os/exec"

	"github.com/whop42/LinuxConvert/linuxconvert/utils"
)

type VSCode struct {
	// fields here
}

func (a *VSCode) CheckInstalledWindows() (bool, error) {
	return utils.CheckWindowsCommandSuccess("code --version"), nil
}

func (a *VSCode) CopyConfigsWindows() error {
	// get %APPDATA%\Code\User content?

	// code --list-extensions?

	return nil
}

func (a *VSCode) PreInstallLinux() error {
	// see here: https://vscodium.com/#install-on-debian-ubuntu-deb-package
	// add gpg of repo
	gpgCMD := exec.Command("wget -qO - https://gitlab.com/paulcarroty/vscodium-deb-rpm-repo/raw/master/pub.gpg | gpg --dearmor | sudo dd of=/usr/share/keyrings/vscodium-archive-keyring.gpg")
	err := gpgCMD.Run()
	if err != nil {
		return err
	}

	// add repo
	repoCMD := exec.Command("echo 'deb [ signed-by=/usr/share/keyrings/vscodium-archive-keyring.gpg ] https://download.vscodium.com/debs vscodium main' | sudo tee /etc/apt/sources.list.d/vscodium.list")
	err = repoCMD.Run()
	if err != nil {
		return err
	}

	return nil
}

func (a *VSCode) GetPackageLinux() (Package, error) {
	return Package{
		Name:           "codium",
		PackageManager: "apt",
	}, nil
}

func (a *VSCode) InstallConfigsLinux() error {
	// copy over configs gathered in CopyConfigsWindows

	return nil
}

func (a *VSCode) GetName() (string, error) {
	return "test app1", nil
}

func (a *VSCode) SetName(name string) error {
	return nil
}
