package gui

import (
	"path"

	"fyne.io/fyne/container"
	"fyne.io/fyne/v2/widget"
	"github.com/whop42/LinuxConvert/linuxconvert"
)

func showFinishedScreen() {
	content := container.NewVBox(
		widget.NewLabel("finished!"),
		widget.NewLabel("file: "+path.Join(linuxconvert.AppStorage.Path, linuxconvert.ArchiveName)+".zip"),
	)

	linuxconvert.DeleteStorageDir()

	wWindow.SetContent(content)
}
