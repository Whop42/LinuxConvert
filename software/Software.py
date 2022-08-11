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