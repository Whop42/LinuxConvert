package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/widget"
	"github.com/whop42/LinuxConvert/linuxconvert"
)

var (
	wApp    fyne.App
	wWindow fyne.Window
)

func Windows() {
	setupUI()
	wWindow.ShowAndRun()
}

func setupUI() {
	wApp = app.New()
	wWindow = wApp.NewWindow("LinuxConvert")
	wWindow.Resize(fyne.NewSize(400, 300))

	showWelcomeScreen()
}

func showWelcomeScreen() {
	content := container.NewVBox(
		widget.NewLabel("Welcome to LinuxConvert"),
		widget.NewLabel("(this is the windows application)"),
		widget.NewButton("Begin", func() {
			showAppScanningScreen()
		}),
	)
	wWindow.SetContent(content)
}

func showAppScanningScreen() {
	content := container.NewVBox(
		widget.NewLabel("Installed Applications:"),
	)
	for _, application := range linuxconvert.AppStorage.InstalledApplications {
		//TODO: handle errors once function handles errors
		appName, _ := application.GetName()

		content.Add(widget.NewCheck(appName, func(b bool) {
			if !b {
				a, aErr := linuxconvert.FindApplicationByName(appName)
				if aErr != nil {
					linuxconvert.RemoveApplicationFromSlice(a, linuxconvert.AppStorage.InstalledApplications)
				}
			}
		}))
	}
	content.Add(widget.NewButton("Scan Windows (will remove deselected applications)", func() {
		linuxconvert.FindInstalledApplications()
		showAppScanningScreen()
	}))

	content.Add(widget.NewButton("Next", func() {
		showConfigCopyScreen()
	}))

	wWindow.SetContent(content)
}

func showConfigCopyScreen() {
	// screen that copies configs
	// TODO: implement
	// 	- progressbar in the middle
	// 	- max: number of applications
	// 	- increment for each application finished
	//  - under progressbar, "start copying applications/settings"
	// 	- grayed out while copying
	// 	- cancel button appears while copying
}
