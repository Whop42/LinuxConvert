package linuxconvert

import (
	"log"
	"os"
	"path"
	"path/filepath"
)

// organizing the directory structure of archive file
func GetApplicationPath(appName string) (string, error) {
	var p string = path.Join(AppStorage.Path, "applications", appName)

	//if it already exists, return it
	if stat, err := os.Stat(p); err == nil && stat.IsDir() {
		return p, nil
	}

	//create dir. if it doesn't work, fatal error occurs.
	if err := os.MkdirAll(p, os.ModePerm); err != nil {
		log.Fatal(err)
	}

	return p, nil
}

// delete the storage directory once done (wait until it's zipped!)
func DeleteStorageDir() error {
	removeAll := os.RemoveAll(AppStorage.Path)

	if removeAll != nil {
		log.Fatal(removeAll.Error())
	}

	return nil
}

// convert unzipped archive to application storage
func ReadUnzippedDir(dirName string) {
	AppStorage.Path = dirName
	applicationsDir := path.Join(dirName, "applications")

	// iterate over all application dirs
	walker := func(path string, info os.FileInfo, err error) error {
		if info.IsDir() {
			app, err := FindApplicationByName(path)
			if err == nil {
				AppStorage.InstalledApplications = append(AppStorage.InstalledApplications, app)
			}
			log.Printf("dir %s is not a recognized application", path)
		}
		return nil
	}

	err := filepath.Walk(applicationsDir, walker)
	if err != nil {
		log.Fatal(err)
	}
}
