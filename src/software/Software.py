import subprocess
import utils
from utils import dprint, eprint
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

    def cmd(self, command: list[str], sudo: bool = False) -> str:
        """
        cmd runs a command

        params:
            list[str] command -> the command to run (main command followed by args)
            bool sudo -> whether or not to run as sudo (default False)

        returns:
            str -> output of the command
        
        raises:
            Exception -> command fails
        """
        if sudo:
            command.insert(0, "sudo")
        
        output = subprocess.run(command, stdout=subprocess.PIPE)

        # catch errors!
        if output.returncode != 0:
            raise Exception("command " + str(command) + " failed...")

        return str(output.stdout)
    
    def install_packages(self, pkgs: list[str]) -> str:
        """
        install_packages installs a list of packages with yay

        params:
            list[str] pkgs -> the list of packages
        
        returns:
            str -> output of installation
        
        exits:
            Exception in self.cmd()
        """
        cmd: list[str] = ["yay", "-Syyu", "--noconfirm"]

        for pkg in pkgs:
            cmd.append(pkg)

        try:
            output: str = self.cmd(cmd)
        except Exception as e:
            eprint(str(e))
            exit()

        return output
    
    def install_package(self, pkg: str) -> str:
        """
        install_package installs a package with yay
        (an alias for install_packages([pkg]))

        params:
            str pkg -> the package
        
        returns:
            str -> output of installation
        
        exits:
            Exception in self.cmd()
        """
        
        output: str = self.install_packages([pkg])

        return output

    def remove_packages(self, pkgs: list[str]) -> str:
        """
        remove_packages removes a list of packages with yay

        params:
            list[str] pkgs -> the list of packages
        
        returns:
            str -> output of installation
        
        exits:
            Exception in self.cmd()
        """
        cmd: list[str] = ["yay", "-R", "--noconfirm"]

        for pkg in pkgs:
            cmd.append(pkg)

        try:
            output: str = self.cmd(cmd)
        except Exception as e:
            eprint(str(e))
            exit()

        return output
    
    def query_package(self, pkg):
        try:
            output = self.cmd(["yay", "-Q", str(pkg)])
        except Exception as e:
            eprint(pkg + " is not installed yet...")
            return False
        return True

    def query_packages(self, pkgs: list[str]) -> str:
        """
        install_packages installs a list of packages with yay

        params:
            list[str] pkgs -> the list of packages
        
        returns:
            str -> output of installation
        
        exits:
            Exception in self.cmd()
        """
        cmd: list[str] = ["yay", "Q"]

        for pkg in pkgs:
            cmd.append(pkg)

        try:
            output: str = self.cmd(cmd)

            for pkg in pkgs:
                assert pkg in output
        except Exception as e:
            eprint(str(e))
            exit()

        return output

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

        output = f"""[Desktop Entry]
Type=Application
Name={self.name}
GenericName={self.generic_name}
Icon={self.icon}
Exec={self.run_cmd}
Terminal=false
                """

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
        return os.path.join(self.get_folder(), "config")
    
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
    
    def recommend(self, alternative: str, reason: str) -> bool:
        resp: str = input(self.name + " " + reason + " It is recommended to " + alternative + " Would you like to? (Y/n): ").lower()
        
        resp: str = input(
f"""{self.name} {reason}.

LinuxConvert recommends {alternative}.

Would you like to do this? (type "n" to reject): 
"""
        ).lower()

        if resp == "n":
            return False
        return True