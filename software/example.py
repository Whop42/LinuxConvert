from software import Software
from os import system as cmd

class example(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "example_application"
    
    def install(self):
        cmd("echo 'example installed'")
        print(self.name)
    
    def uninstall(self):
        cmd("echo 'example uninstalled'")