"""
this project is supposed to work on the failure of the first walk method, except that this is the main deal right here.
I think I really got it this time. Thank God all and everything.

first off import path.
and then i will create the class and then initialize it and then.
the class will require the directory only.
okay, so i think that is all its there.
"""
from paths import *
import sys
if sys:
    sys.path.append("/media/danny_mcwaves/CODE_BASE/pyPROJECTS")
__Author__ = "Danny mcwaves"


class Walk:
    """
    this is the function supposed to find all the elements in a directory until there is no
    other directory to open to find all the files in that dir. so until then, it will call the walk function
    recursively
    :return: None
    """
    def __init__(self, directory="/media/danny_mcwaves/CODE_BASE/pyPROJECTS"):
        self.__path = path(directory)

    def startWalk(self, fmt=""):

        try:
            for file in self.__path.getFullPaths():
                if path(file).isFile():
                    print(fmt + file)

                elif path(file).isDir():
                    print("\n"+fmt+" DIRECTORY_NAME --> " + file.split("/")[-1])
                    print(fmt + file)
                    Walk(file).startWalk("\t")

        except PermissionError:
            print(" PERMISSION ERROR -- YOU ARE NOT ALLOWED TO ACCESS FILE")
            pass

if __name__ == '__main__':
    walk = Walk()
    walk.startWalk()