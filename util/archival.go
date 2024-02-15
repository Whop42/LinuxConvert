package util

import (
	"archive/zip"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
)

// zip up storage, thanks, danneu! https://stackoverflow.com/a/63233911/15187279
// func Archive(srcDir, dest string) {
// 	//TODO: test case

// 	// create zip
// 	file, err := os.Create(dest) //TODO: parent dir might not exist??
// 	if err != nil {
// 		ErrorLogger.Panic(err)
// 	}
// 	defer file.Close()

// 	// create writer for zip
// 	w := zip.NewWriter(file)
// 	defer w.Close()

// 	// walker function to deep iterate over everything and zip it up
// 	// thanks again to danneu on stackoverflow
// 	walker := func(path string, info os.FileInfo, err error) error {
// 		fmt.Printf("Archiving: %#v\n", path)
// 		if err != nil {
// 			return err
// 		}
// 		if info.IsDir() {
// 			// add a trailing slash for creating dir
// 			path = fmt.Sprintf("%s%c", path, os.PathSeparator)
// 			_, err = w.Create(path)
// 			return err
// 		}

// 		file, err := os.Open(path)
// 		if err != nil {
// 			return err
// 		}
// 		defer file.Close()

// 		// Ensure that `path` is not absolute; it should not start with "/".
// 		// This snippet happens to work because I don't use
// 		// absolute paths, but ensure your real-world code
// 		// transforms path into a zip-root relative path.
// 		f, err := w.Create(path)
// 		if err != nil {
// 			return err
// 		}

// 		_, err = io.Copy(f, file)
// 		if err != nil {
// 			return err
// 		}

// 		return nil
// 	}

// 	// walk over the whole srcDir
// 	err = filepath.Walk(srcDir, walker)
// 	if err != nil {
// 		ErrorLogger.Panic("failed archiving: " + fmt.Sprint(err))
// 	}
// }

func Archive(srcDir, dest string) {
	//TODO: test case

	// create zip
	file, err := os.Create(dest) //TODO: parent dir might not exist??
	if err != nil {
		ErrorLogger.Panic(err)
	}
	defer file.Close()

	// create writer for zip
	w := zip.NewWriter(file)
	defer w.Close()

	// walker function to deep iterate over everything and zip it up
	// thanks again to danneu on stackoverflow
	walker := func(path string, info os.FileInfo, err error) error {
		fmt.Printf("Archiving: %#v\n", path)
		if err != nil {
			return err
		}
		if info.IsDir() {
			// add a trailing slash for creating dir
			path = fmt.Sprintf("%s%c", path, os.PathSeparator)
			_, err = w.Create(path)
			return err
		}

		// Get the relative path from srcDir to the current file or directory
		relPath, err := filepath.Rel(srcDir, path)
		if err != nil {
			return err
		}

		f, err := w.Create(relPath)
		if err != nil {
			return err
		}

		file, err := os.Open(path)
		if err != nil {
			return err
		}
		defer file.Close()

		_, err = io.Copy(f, file)
		if err != nil {
			return err
		}

		return nil
	}

	// walk over the whole srcDir
	err = filepath.Walk(srcDir, walker)
	if err != nil {
		ErrorLogger.Panic("failed archiving: " + fmt.Sprint(err))
	}
}

// unzip the archive provided, thanks Astockwell! https://stackoverflow.com/questions/20357223/easy-way-to-unzip-file#24792688
func Extract(src, destDir string) {
	//TODO: test case

	// open the src file with a zip reader
	r, err := zip.OpenReader(src)
	if err != nil {
		ErrorLogger.Panic(err)
	}
	defer r.Close()

	// make sure destDir exists already
	os.MkdirAll(destDir, os.ModeDir)

	// thanks again to Astockwell on stackoverflow!!
	// Closure to address file descriptors issue with all the deferred .Close() methods
	extractAndWriteFile := func(f *zip.File) error {
		rc, err := f.Open()
		if err != nil {
			return err
		}
		defer func() {
			if err := rc.Close(); err != nil {
				ErrorLogger.Panic(err)
			}
		}()

		path := filepath.Join(destDir, f.Name)

		// Check for ZipSlip (Directory traversal)
		if !strings.HasPrefix(path, filepath.Clean(destDir)+string(os.PathSeparator)) { // TODO: filepath.Join?
			return fmt.Errorf("illegal file path: %s", path)
		}

		if f.FileInfo().IsDir() {
			os.MkdirAll(path, f.Mode())
		} else {
			os.MkdirAll(filepath.Dir(path), f.Mode())
			f, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, f.Mode())
			if err != nil {
				return err
			}
			defer func() {
				if err := f.Close(); err != nil {
					ErrorLogger.Panic(err)
				}
			}()

			_, err = io.Copy(f, rc)
			if err != nil {
				return err
			}
		}
		return nil
	}

	// do the actual extraction
	for _, f := range r.File {
		err := extractAndWriteFile(f)
		if err != nil {
			ErrorLogger.Panic(err)
		}
	}
}
