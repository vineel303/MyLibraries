import shutil
import os

def simpleRenameAndMove(initialFolderPath, initialFileName, finalFolderPath, finalFileName):
    shutil.move(os.path.join(initialFolderPath, initialFileName), os.path.join(finalFolderPath, finalFileName))
def simpleRenameAndCopy(initialFolderPath, initialFileName, finalFolderPath, finalFileName):
    shutil.copy(os.path.join(initialFolderPath, initialFileName), os.path.join(finalFolderPath, finalFileName))
