import subprocess
import utils
import shutil
import json
import os

class Software:
    """
    the base class for each software script supported

    note: sets installed status to False as default
    """

    def __init__(self):
        self.name = ""
        #installed status
        self.status = self.check_install()
        self.run_cmd = ""
        self.generic_name = self.name
        self.icon = ""

    def cmd(self, command, sudo=True):
        if sudo:
            command.insert(0, "sudo")
        output = subprocess.run(command, stdout=subprocess.PIPE)
        return str(output.stdout)
    
    def install_package(self, pkg):
        return self.cmd(["pacman", "-Sy", "--noconfirm", "--asdeps", str(pkg)])
    
    def remove_package(self, pkg):
        return self.cmd(["pacman", "-R", "--noconfirm", str(pkg)])
    
    def query_package(self, pkg):
        output = self.cmd(["pacman", "-Q", str(pkg)])
        if pkg in output and "error" not in output:
            return True
        return False

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
        output = "[Desktop Entry]\n" + "Type=Application\n" + "Name=" + self.name + "\n" + "GenericName=" + self.generic_name + "\n" + "Icon=" + self.icon + "\n" + "Exec=" + self.run_cmd + "\n" + "Terminal=false"

        f = open(path, "w")
        f.write(output)
        f.close()
    
    def get_folder(self):
        """
        returns full path of application folder
        """

        return utils.locate_application_path(self.name)
    
    def move_configs(self, dest):
        """
        move configs from this application's config
        folder to the dir "dest"

        WARNING: UNTESTED
        TODO: test this
        """
        output = []
        config_folder = os.path.join(self.get_folder(), "config")
        for f in os.listdir(config_folder):
            shutil.copy(os.path.join(config_folder, f), os.path.join(dest, f))
            output.append("Moving %s to %s" % (f, os.path.join(dest, f)))
        output.append("Moved config files from %s to %s" % (self.name, dest))
        return output
    
    def check_windows(self):
        """
        Checks if the Software is installed on windows

        Note: returns False by default
        """
        return False

    def check_mac(self):
        """
        Checks if the Software is installed on macOS

        Note: returns False by default
        """


        return False
    
    def get_config_windows(self):
        """
        copies windows config to utils.locate_application_path()
        """


        return False
    
    def get_config_mac(self):

        return False
    
    def create_config(self):
        f = open(os.path.join(utils.locate_application_path(self.name), "%s-application.json" % self.name), "w")
        f.write(json.dumps({
            "name": self.name
        }))
        f.close()