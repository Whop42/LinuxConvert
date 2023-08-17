package gui

import (
	"fmt"
	"path"

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
	wWindow.SetCloseIntercept(func() {
		linuxconvert.DeleteStorageDir()
		wWindow.Close()
	})

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

func RemoveDuplicateApplications(apps []linuxconvert.Application) []linuxconvert.Application {
	// Create a map to track seen applications
	seen := make(map[string]struct{})
	result := []linuxconvert.Application{} // Slice to store unique applications
	for _, app := range apps {
		name, _ := app.GetName()
		if _, ok := seen[name]; !ok {
			seen[name] = struct{}{}
			result = append(result, app)
		}
	}
	return result
}

func showAppScanningScreen() {
	linuxconvert.FindInstalledApplications()

	content := container.NewVBox(
		widget.NewLabel("Installed Applications:"),
	)

	// Create checkboxes for each installed application
	checkboxes := make([]*widget.Check, 0)
	for _, app := range linuxconvert.AppStorage.InstalledApplications {
		name, _ := app.GetName()
		checkbox := widget.NewCheck(name, nil)
		checkbox.Checked = true
		checkboxes = append(checkboxes, checkbox)
	}

	checkboxesContainer := container.NewVBox()
	for _, check := range checkboxes {
		checkboxesContainer.Add(check)
	}

	saveChecks := func() {
		// Update InstalledApplications based on checkbox states
		updatedInstalledApplications := make([]linuxconvert.Application, 0)
		for i, checkbox := range checkboxes {
			if checkbox.Checked {
				updatedInstalledApplications = append(updatedInstalledApplications, linuxconvert.AppStorage.InstalledApplications[i])
			}
		}
		linuxconvert.AppStorage.InstalledApplications = updatedInstalledApplications

		// Print updated InstalledApplications for demonstration
		for _, app := range linuxconvert.AppStorage.InstalledApplications {
			name, _ := app.GetName()
			fmt.Println(name)
		}
	}

	// Create a button to process checkbox changes
	saveButton := widget.NewButton("Save", saveChecks)

	content.Add(checkboxesContainer)
	content.Add(saveButton)

	content.Add(widget.NewButton("Next", func() {
		saveChecks()
		fmt.Println(linuxconvert.AppStorage.InstalledApplications)
		showConfigCopyScreen()
	}))

	wWindow.SetContent(content)
}

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

func showFinishedScreen() {
	content := container.NewVBox(
		widget.NewLabel("finished!"),
		widget.NewLabel("file: "+path.Join(linuxconvert.AppStorage.Path, linuxconvert.ArchiveName)+".zip"),
	)

	linuxconvert.DeleteStorageDir()

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
