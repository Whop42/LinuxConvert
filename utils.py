import os

def locate_application_path(name):
    """
    returns full path of application folder
    (folder should look like:

    app_name/
        app_name_application.json
        config (optional)/
            ...
    )
    """

    for filename in os.listdir(os.getcwd()):
        if "-linuxconvert" in filename:
            for application_folder in os.listdir(os.path.join(os.getcwd(), filename, "applications")):

                if application_folder == name:
                    return os.path.join(os.path.join(os.getcwd(), filename, "applications", application_folder))
