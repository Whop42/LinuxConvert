package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"

	"github.com/whop42/LinuxConvert/linuxconvert"
)

var (
	wApp    fyne.App
	wWindow fyne.Window
)

func Windows() {
	setupUI()
	linuxconvert.AssignApplications()
	wWindow.ShowAndRun()
}

func setupUI() {
	wApp = app.New()
	wWindow = wApp.NewWindow("LinuxConvert")
	wWindow.Resize(fyne.NewSize(400, 300))
	wWindow.SetCloseIntercept(func() {
		linuxconvert.DeleteStorageDir()
		wWindow.Close()
	})

	showWelcomeScreen()
}
