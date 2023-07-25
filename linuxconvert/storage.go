package linuxconvert

import (
	"archive/zip"
	"fmt"
	"io"
	"log"
	"os"
	"path"
	"path/filepath"
	"time"
)

var archiveName = fmt.Sprintf("linuxconvert-%d", time.Now().Unix())

// global Storage object
var appStorage *Storage = &Storage{
	Path:                  path.Join(os.TempDir(), archiveName),
	InstalledApplications: []Application{},
}

type Storage struct {
	Path                  string        //root path of directory to dump configs into
	InstalledApplications []Application //list of installed applications
}

func GetApplicationPath(appName string) (string, error) {
	var p string = path.Join(appStorage.Path, "applications", appName)

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
	removeAll := os.RemoveAll(appStorage.Path)

	if removeAll != nil {
		log.Fatal(removeAll.Error())
	}

	return nil
}

// zip up storage (thanks, danneu! [https://stackoverflow.com/a/63233911/15187279])
func ArchiveStorage() {
	// create .zip file in the temporary dir
	// (TODO: decide if this is the right way. maybe get users to decide for themselves?)
	archiveName := path.Join(path.Dir(appStorage.Path), archiveName+".zip")
	file, err := os.Create(archiveName)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	w := zip.NewWriter(file)
	defer w.Close()

	walker := func(path string, info os.FileInfo, err error) error {
		fmt.Printf("Crawling: %#v\n", path)
		if err != nil {
			return err
		}
		if info.IsDir() {
			// add a trailing slash for creating dir
			path = fmt.Sprintf("%s%c", path, os.PathSeparator)
			_, err = w.Create(path)
			return err
		}
		file, err := os.Open(path)
		if err != nil {
			return err
		}
		defer file.Close()

		// Ensure that `path` is not absolute; it should not start with "/".
		// This snippet happens to work because I don't use
		// absolute paths, but ensure your real-world code
		// transforms path into a zip-root relative path.
		f, err := w.Create(path)
		if err != nil {
			return err
		}

		_, err = io.Copy(f, file)
		if err != nil {
			return err
		}

		return nil
	}
	err = filepath.Walk(appStorage.Path, walker)
	if err != nil {
		panic(err)
	}
}
