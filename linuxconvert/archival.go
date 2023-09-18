package linuxconvert

import (
	"archive/zip"
	"fmt"
	"io"
	"os"
	"path"
	"path/filepath"
	"strings"
)

// zip up storage (thanks, danneu! [https://stackoverflow.com/a/63233911/15187279])
func ArchiveStorage() {
	// create .zip file in the temporary dir
	// (TODO: decide if this is the right way. maybe get users to decide for themselves?)
	ArchiveName := path.Join(path.Dir(AppStorage.Path), ArchiveName+".zip")
	file, err := os.Create(ArchiveName)
	if err != nil {
		panic(err)
	}
	defer file.Close()

	w := zip.NewWriter(file)
	defer w.Close()

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
	err = filepath.Walk(AppStorage.Path, walker)
	if err != nil {
		panic(err)
	}
}

// unzip the archive provided, thanks Astockwell! https://stackoverflow.com/questions/20357223/easy-way-to-unzip-file#24792688
func ExtractArchive(src string) error {
	_, dest := path.Split(src)
	dest = strings.Replace(dest, ".zip", "", -1)
	dest = os.TempDir() + dest

	r, err := zip.OpenReader(src)
	if err != nil {
		return err
	}
	defer func() {
		if err := r.Close(); err != nil {
			panic(err)
		}
	}()

	os.MkdirAll(dest, 0755)

	// Closure to address file descriptors issue with all the deferred .Close() methods
	extractAndWriteFile := func(f *zip.File) error {
		rc, err := f.Open()
		if err != nil {
			return err
		}
		defer func() {
			if err := rc.Close(); err != nil {
				panic(err)
			}
		}()

		path := filepath.Join(dest, f.Name)

		// Check for ZipSlip (Directory traversal)
		if !strings.HasPrefix(path, filepath.Clean(dest)+string(os.PathSeparator)) {
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
					panic(err)
				}
			}()

			_, err = io.Copy(f, rc)
			if err != nil {
				return err
			}
		}
		return nil
	}

	for _, f := range r.File {
		err := extractAndWriteFile(f)
		if err != nil {
			return err
		}
	}

	return nil
}
