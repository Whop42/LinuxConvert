from software import Software
from os import system as cmd

class neofetch(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "neofetch"
    
    def install(self):
        cmd("apt install neofetch -y")
        print(1)
    
    def uninstall(self):
        cmd("apt remove neofetch")