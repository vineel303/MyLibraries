import shutil
import os

# rename, move and copy
def simpleRename_AndOrOr_Move(initialFolderPath, initialFileName, finalFolderPath, finalFileName):
    shutil.move(os.path.join(initialFolderPath, initialFileName), os.path.join(finalFolderPath, finalFileName))

def simpleRename_And_Copy(initialFolderPath, initialFileName, finalFolderPath, finalFileName):
    shutil.copy(os.path.join(initialFolderPath, initialFileName), os.path.join(finalFolderPath, finalFileName))

# check if file/folder exists
def doesFileExist(folderPath, fileName):
    if os.path.isfile(os.path.join(folderPath, fileName)):
        return True
    else:
        return False

def doesFolderExist(folderPath):
    if os.path.isdir(folderPath):
        return True
    else:
        return False

def createUniqueFile(folderPath, fileName, pre_folderName_add = " ", post_folderName_add = ""):
    if not os.path.isfile(os.path.join(folderPath, fileName)):
        return fileName
    else:
        uniqueNumber = 0
        while True:
            uniqueNumber+=1
            fileNameList = separateFileNameAndExtension(fileName)
            fileName = fileNameList[0] + pre_folderName_add + uniqueNumber + post_folderName_add + "." + fileNameList[1]
            if not os.path.isfile(os.path.join(folderPath, fileName)):
                break
        return fileName

def createUniqueFolder(folderPath, folderName, pre_folderName_add = " ", post_folderName_add = ""):
    if not os.path.isdir(os.path.join(folderPath, folderName)):
        return folderName
    else:
        uniqueNumber = 0
        while True:
            uniqueNumber += 1
            folderName = folderName + pre_folderName_add + uniqueNumber + post_folderName_add
            if not os.path.isdir(os.path.join(folderPath, folderName)):
                break
        return folderName

# more functions
def separateFileNameAndExtension(fileName, returnAsList = True):
    if returnAsList:
        return fileName.rsplit(".", 1)
    else:
        fileName = fileName.rsplit(".", 1)
        return fileName[0], fileName[1]
