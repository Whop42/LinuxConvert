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

        self.package_manager = "yay"

    def cmd(self, command, sudo=False):
        if sudo:
            command.insert(0, "sudo")
        output = subprocess.run(command, stdout=subprocess.PIPE)
        return str(output.stdout)
    
    def install_package(self, pkg):
        output = self.cmd(["yay", "-Sy", "--noconfirm", str(pkg)], sudo=True)
        # if "error:" in output:
        #     return False
        return output
    
    def remove_package(self, pkg):
        return self.cmd(["yay", "-R", "--noconfirm", str(pkg)], sudo=True)
    
    def query_package(self, pkg):
        output = self.cmd(["yay", "-Q", str(pkg)], sudo=True)
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
        if self.name == "backups":
            return
        output = "[Desktop Entry]\n" + "Type=Application\n" + "Name=" + self.name + "\n" + "GenericName=" + self.generic_name + "\n" + "Icon=" + self.icon + "\n" + "Exec=" + self.run_cmd + "\n" + "Terminal=false"

        f = open(path, "w")
        f.write(output)
        f.close()
    
    def get_folder(self):
        """
        returns full path of application folder
        """

        return os.path.join(utils.locate_application_path(self.name))

    def get_config_folder(self):
        """
        returns full path of application's config folder
        """
        return os.path.join(self.get_folder, "config")
    
    def move_configs(self, dest):
        """
        move configs from this application's config
        folder to the dir "dest"

        WARNING: UNTESTED
        TODO: test this
        """
        output = []
        config_folder = os.path.join(self.get_folder(), "config")
        utils.copy_dir(config_folder, dest)
        output.append("Moved config files from %s to %s" % (self.name, dest))
        return output
    
    def check_windows(self):
        """
        Checks if the Software is installed on windows

        Note: returns False by default
        """
        return False
    
    def get_config_windows(self):
        """
        copies windows config to utils.locate_application_path()

        Note: returns False by default
        """

        return False
    
    def create_config(self):
        os.mkdir(os.path.join(os.getcwd(), utils.get_root_folder(), "applications", self.name))
        f = open(os.path.join(self.get_folder(), "%s-application.json" % self.name), "w")
        f.write(json.dumps({
            "name": self.name
        }))
        f.close()
        utils.dprint("created application.json for " + self.name)

        os.mkdir(self.get_config_folder())
