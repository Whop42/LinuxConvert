package gui

import (
	"fmt"

	"fyne.io/fyne/container"
	"fyne.io/fyne/v2/data/binding"
	"fyne.io/fyne/v2/widget"
	"github.com/whop42/LinuxConvert/linuxconvert"
)

func showConfigCopyScreen() {
	progress := binding.NewString()
	progress.Set("not copied")

	// TODO: Change to infinite progressbar?
	ProgressLabel := widget.NewLabelWithData(progress)

	CopyingButton := widget.NewButton("Begin copying applications/settings", func() {
		progress.Set("copying...")
		CopyInstalledConfigs()
		progress.Set("copied!")
	})

	NextButton := widget.NewButton("Next", func() {
		showArchiveScreen()
	})

	content := container.NewCenter(container.NewVBox(
		ProgressLabel,
		CopyingButton,
		NextButton,
	))

	for index, app := range linuxconvert.AppStorage.InstalledApplications {
		fmt.Printf("%s: %#v\n", fmt.Sprint(index), app)
	}

	wWindow.SetContent(content)
}

func CopyInstalledConfigs() {
	for _, app := range linuxconvert.AppStorage.InstalledApplications {
		name, _ := app.GetName()
		linuxconvert.GetApplicationPath(name)
		err := app.CopyConfigsWindows()
		if err != nil {
			panic(err)
		}
		fmt.Println("configs copied from " + name)
	}
}
