from software import Software
import os
import shutil
import utils

class vscode(Software.Software):
    
    def __init__(self):
        super(Software.Software, self).__init__()
        self.name = "vscode"

        self.run_cmd = "code"
        self.generic_name = "screenshot"
        self.icon = "screengrab"

        self.pkg_names = ["vscodium-bin", "vscodium-bin-marketplace"]
    
    def install(self):
        output = ""
        # install "Code - OSS" w/ package manager
        for pkg in self.pkg_names:
            output += self.install_package(pkg)
        # move configs
        self.move_configs("~/.config/Code - OSS")
        
        return output

    
    def uninstall(self):
        output = ""
        for pkg in self.pkg_names:
            output += str(self.remove_package(pkg))
        return output

    
    def check_install(self):
        return self.query_package(self.pkg_names[0])
    
    def check_windows(self):
        if shutil.which("code"):
            return True
        return False
    
    def get_config_windows(self):
        """
        copies windows config,
        returns true on success, false on failure
        """


        programs_path = os.path.expandvars("%APPDATA%\\Code")
        program_files_x86_path = "C:\\Program Files (x86)\\Microsoft VS Code"
        program_files_x64_path = "C:\\Program Files\\Microsoft VS Code"
        path = 1 # 1 for programs, 2 for x86, 3 for x64

        dirs = ["CachedExtensions", "CachedExtensionVSIXs", "User"]
        files = ["languagepacks.json", "Network Persistent State", "Preferences", "TransportSecurity"]

        full_dirs = [os.path.join(programs_path, d) for d in dirs]

        if utils.copy_dirs(full_dirs, self.get_config_folder()):
            path = 1
        elif utils.copy_dirs([os.path.join(program_files_x86_path, d) for d in dirs], self.get_config_folder()):
            path = 2
        elif utils.copy_dirs([os.path.join(program_files_x64_path, d) for d in dirs], self.get_config_folder()):
            path = 3
        else:
            return False

        if utils.copy_files([os.path.join(programs_path, f) for f in files], self.get_config_folder()):
            return True
        elif utils.copy_files([os.path.join(program_files_x86_path, f) for f in files], self.get_config_folder()):
            return True
        elif utils.copy_files([os.path.join(program_files_x64_path, f) for f in files], self.get_config_folder()):
            return True
        else:
            return False
