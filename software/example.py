from software import Software
import subprocess

class example(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "example"

        self.installed = False
    
    def install(self):
        output = subprocess.run(["sudo", "pacman", "-Sy", "cmatrix"], stdout=subprocess.PIPE)
        #if it fails, return error
        return output.stdout
    
    def uninstall(self):
        output = subprocess.run(["echo", "'example uninstalled'"], stdout=subprocess.PIPE)
        return output.stdout
    
    def check_install(self):
        return self.installed