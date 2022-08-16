import subprocess

class Software:
    """
    the base class for each software script supported

    params:
        * name: name of software

    note: sets installed status to False as default
    """

    name = ""

    def __init__(self, name):
        self.name = name
        #installed status
        self.status = check_install()
        self.run_cmd = ""
        self.generic_name = name
        self.icon = ""

    def install(self):
        """
        installs the software
        """
        
        pass

    def uninstall(self):
        """
        uninstalls the software
        """

        pass

    def check_install(self):
        """
        checks if the software is installed on the system

        note: returns False by default
        """

        return False

    def get_name(self):
        return self.name
    
    def run(self):
        """
        runs the application
        """
        
        output = subprocess.run(self.run_cmd, stdout=subprocess.PIPE)
        print(output)
    
    def create_desktop(self, path):
        """
        creates a .desktop file for the installed application
        """
        output = "[Desktop Entry]\n"
        + "Type=Application\n"
        + "Name=" + self.name + "\n"
        + "GenericName=" + self.generic_name + "\n"
        + "Icon=" + self.icon + "\n"
        + "Exec=" + self.run_cmd + "\n"
        + "Terminal=false"

        f = open(path, "w")
        f.write(output)
        f.close()