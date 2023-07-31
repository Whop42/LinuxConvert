package gui

import (
	"fyne.io/fyne/v2"
	"fyne.io/fyne/v2/app"
	"fyne.io/fyne/v2/container"
	"fyne.io/fyne/v2/data/binding"
	"fyne.io/fyne/v2/widget"
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

		checkWidget := widget.NewCheck(appName, func(b bool) {
			if !b {
				a, aErr := linuxconvert.FindApplicationByName(appName)
				if aErr != nil {
					linuxconvert.RemoveApplicationFromSlice(a, linuxconvert.AppStorage.InstalledApplications)
				}
			}
		})

		checkWidget.Checked = true

		content.Add(checkWidget)
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

	CopyingProgress := widget.NewProgressBar()
	CopyingProgress.Max = float64(len(linuxconvert.AppStorage.InstalledApplications))

	CopyingButton := widget.NewButton("Begin copying applications/settings", func() {
		CopyInstalledConfigs(CopyingProgress)
	})

	NextButton := widget.NewButton("Next", func() {
		showArchiveScreen()
	})

	content := container.NewCenter(container.NewVBox(
		CopyingProgress,
		CopyingButton,
		NextButton,
	))

	wWindow.SetContent(content)
}

func showArchiveScreen() {
	// TODO: implement
}

func CopyInstalledConfigs(progress *widget.ProgressBar) {
	var value float64 = 0
	progress.Bind(binding.BindFloat(&value))
	for _, app := range linuxconvert.AppStorage.InstalledApplications {
		err := app.CopyConfigsWindows()
		if err != nil {
			panic(err)
		}
		value += 1
	}
}
