package gui

import (
	"fmt"

	"fyne.io/fyne/container"
	"fyne.io/fyne/v2/widget"
	"github.com/whop42/LinuxConvert/linuxconvert"
)

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
