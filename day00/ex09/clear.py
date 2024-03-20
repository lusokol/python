import os


def uninstall():
    """
Uninstall my package 'ft_package'
    """
    os.system("rm -rf build")
    os.system("rm -rf dist")
    os.system("rm -rf ft_package.egg-info")
    os.system("pip3 uninstall ft_package")


if __name__ == "__main__":
    uninstall()
