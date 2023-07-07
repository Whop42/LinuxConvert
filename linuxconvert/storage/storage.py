from io import TextIOWrapper
import json
import os, shutil
from linuxconvert.software import Software, SoftwareManager
import time
from InfoManager import InfoManager

class Storage:
    im: InfoManager

    path: str

    def __init__(self, path: str):
        self.path = path

    def unpack(self, path: str) -> None:
        # ensure path exists
        if not os.path.exists(path):
            os.makedirs(path)

        # ensure path is unzipped
        if os.path.isfile(path) and ".zip" in path:
            new_path: str = path.replace(".zip", "")

            # extract zip and delete .zip file
            shutil.unpack_archive(path, new_path)
            os.remove(path)

            path = new_path
        
        self.path = path
        self.load_config(path)
        self.load_applications(path)

    def load_config(self, path: str) -> None:
        """
        takes json data from path/config.json and puts it in self.config

        throws:
            AssertionError if path/config.json isn't a file

        params:
            path (str) -> path to check for config.json in. usually self.path.

        outputs:
            changes self.config to json file contents
        """

        config_filepath: str = os.path.join(path, "config.json")

        assert os.path.isfile(config_filepath)

        config_file: TextIOWrapper = open(config_filepath)

        # TODO: write tests to make sure config file contains necessary options
        self.im.config = json.load(config_file.read())

    def load_applications(self, path: str) -> None:
        """
        loads applications found in path to self.applications

        throws:
            AssertionError if path/applications/ isn't a dir

        params:
            path (str) -> path to check for applications folder in
        """
        applications_dir: str = os.path.join(path, "applications")

        assert os.path.isdir(applications_dir)

        for fn in os.listdir(applications_dir):
            # skip this filename if it isn't a dir
            if os.path.isdir(os.path.join(applications_dir, fn)):
                continue

            for software in SoftwareManager.softwares:
                if fn == software.name and software not in self.applications:
                    self.im.applications.append(software)

    def store(self, path: str, installed_software: list[Software.Software]) -> None:
        """
        creates .zip with applications (+ configs and config.json) file from the list of installed software.
        this is as a new .zip file WITHIN the path provided. the .zip will be named "linuxconvert-<time.time()>.zip".

        params:
            path (str) -> path to place .zip file in.


        <<WINDOWS ONLY>>
        """

        if not os.path.isdir(path):
            os.makedirs(path)
        
        os.mkdir(os.path.join(path, "linuxconvert-" + str(time.time())))

        # create config.json
        config_filepath: str = os.path.join(path, "")
        config_file: TextIOWrapper = open(config_filepath, "w")
        json.dump(self.config, config_file)
        config_file.close()

        # create applications dir
        applications_dir: str = os.path.join(path, "applications")
        os.mkdir(applications_dir)

        # get configs from each software TODO: update with GUI logging methods!
        for software in installed_software:
            if software.check_windows():
                software.storage = self
                software.get_config_windows()

    def get_application_folder(self, software: Software.Software) -> str:
        """
        returns the folder that a software should store its info in. if the folder doesn't exist,
        it creates it with os.makedirs.

        params:
            software (Software) -> the software instance. needs to have an accessible name.

        throws:
            OSError if os.makedirs doesn't work
        """

        application_folder_path: str = os.path.join(self.path, "applications", software.name)
        if not os.path.exists(application_folder_path):
            os.makedirs(application_folder_path)
        return application_folder_path