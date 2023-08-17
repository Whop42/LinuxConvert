package utils

import "os/exec"

func CheckWindowsCommandSuccess(command string) bool {
	cmd := exec.Command(command)

	err := cmd.Run()

	return err == nil
}
