package gui

import (
	"fyne.io/fyne/container"
	"fyne.io/fyne/v2/data/binding"
	"fyne.io/fyne/v2/widget"
	"github.com/whop42/LinuxConvert/linuxconvert"
)

func showArchiveScreen() {
	ArchivingProgress := widget.NewProgressBarInfinite()
	ArchivingProgress.Hide()

	ArchiveDisplay := widget.NewLabelWithData(binding.BindString(&linuxconvert.ArchiveName))

	ArchiveButton := widget.NewButton("Begin archival process", func() {
		ArchivingProgress.Show()
		ArchivingProgress.Start()
		linuxconvert.ArchiveStorage()
		ArchivingProgress.Stop()
	})

	NextButton := widget.NewButton("Next", func() {
		showFinishedScreen()
	})

	content := container.NewCenter(container.NewVBox(
		ArchiveDisplay,
		ArchivingProgress,
		ArchiveButton,
		NextButton,
	))

	wWindow.SetContent(content)
}
