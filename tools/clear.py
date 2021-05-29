import os
from sys import platform


def clear():
    if platform.startswith(("linux", "freebsd", "darwin", "aix")):
        os.system("clear")

    elif platform.startswith("win"):
        os.system("cls")
