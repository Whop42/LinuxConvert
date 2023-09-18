package linuxconvert

import (
	"fmt"
	"os"
	"path"
	"time"
)

var ArchiveName = fmt.Sprintf("linuxconvert-%d", time.Now().Unix())

// global Storage object
var AppStorage *Storage = &Storage{
	Path:                  path.Join(os.TempDir(), ArchiveName),
	InstalledApplications: []Application{},
}

type Storage struct {
	Path                  string        //root path of directory to dump configs into
	InstalledApplications []Application //list of installed applications
}
