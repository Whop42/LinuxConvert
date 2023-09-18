package gui

import (
	"fyne.io/fyne/container"
	"fyne.io/fyne/v2/widget"
)

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
