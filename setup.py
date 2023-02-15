from distutils.core import setup

setup(
    name="LinuxConvert",
    version="1.0.0",
    description="Convert a Windows installation's personalization and applications to Linux",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="https://github.com/whop42/LinuxConvert",
    author="whop42",
    author_email="whop42@icloud.com",
    license="GPL v3",
    packages=["linuxconvert"],
    include_package_data=True,
    install_requires=[
        "requests", "darkdetect", "py-wallpaper", "time"
    ],
    entry_points={"console_scripts": ["linuxconvert=linuxconvert.__main__:main"]},
)
