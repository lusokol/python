import os
from tqdm import tqdm
from colorama import Fore, Style


def build():
    """
Build my package 'ft_package'
    """
    with tqdm(total=100, desc="Build  ") as pbar:
        os.system("python setup.py sdist bdist_wheel > /dev/null 2>&1")
        pbar.update(100)
    print()


def install():
    """
Install my package 'ft_package'
    """
    with tqdm(total=100, desc="Install") as pbar:
        os.system("pip3 install ./dist/ft_package-0.0.1.tar.gz >\
                  /dev/null 2>&1")
        pbar.update(100)
    print()


def show():
    """
Show details of my package 'ft_package'
    """
    with tqdm(total=100, desc="Display") as pbar:
        pbar.update(100)
    print()
    print(Fore.BLUE)
    os.system("pip3 show -v ft_package")
    print(Style.RESET_ALL)
    print()


def test(file):
    """
Start a test file to test my package 'ft_package'
    """
    with tqdm(total=100, desc="Tester ") as pbar:
        pbar.update(100)
    print()
    os.system("python3.10 "+file+".py")


if __name__ == "__main__":
    build()
    install()
    show()
    test("test/test2")
    test("test/test")
