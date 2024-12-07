import os
import shutil
from send2trash import send2trash
from vinTextTools import listOfAlphabets_small as vinlistOfAlphabets_small
### this symbol means that the function is tested and stable::: """< text >"""

## VARIABLES
illegalChars_inWinFiles = ['\\', '<', '>', ':', '"', '/', '|', '?', '*']
illegalFileNames_inWin = [
    "CON", "PRN", "AUX", "NUL",
    "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
    "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"
]

## FUNCTIONS
# FILE EXTENSION TOOLS
def separate_fileNameAndExtension(fileName, returnAsList=True):
    """
    Separates extension from file/folder name.
    Returns as '2 element list' / '2 variables'.
    """
    ###
    fileName = fileName.rsplit(".", 1)
    if len(fileName) == 1:
        fileName = [fileName[0], ""]
    ###
    if returnAsList:
        return fileName
    else:
        return fileName[0], fileName[1]

def copyExtension_FromWithToWithout(fileWithExtension, fileWithoutExtension):
    """
    Copies extension to B from A (file/folder name).
    """
    fileWithExtension = separate_fileNameAndExtension(fileWithExtension)
    if fileWithExtension[1]:
        fileWithoutExtension = fileWithoutExtension + "." + fileWithExtension[1]
    return fileWithoutExtension

# FOLDER TOOLS
def removeTrailingBackSlashes(String):
    """Simple"""
    while True:
        if String[-1] != "\\":
            break
        else:
            String = String[:-1]
    return String

def separate_fileNameAndPath(fileName_withPath, returnAsList=True):
    """
    Separates file/folder and its path.
    Returns as '2 element list' / '2 variables'.
    """
    fileName_withPath = removeTrailingBackSlashes(fileName_withPath)
    fileName_withPath = fileName_withPath.rsplit("\\", 1) # note this
    if returnAsList:
        return fileName_withPath
    else:
        return fileName_withPath[0], fileName_withPath[1]

# DOES FILE/FOLDER EXIST
def doesFileExist(folderPath, fileName=""):
    """Simple"""
    if fileName:
        folderPath = os.path.join(folderPath, fileName)
    if os.path.isfile(folderPath):
        return True
    else:
        return False

def doesFolderExist(folderPath, folderName=""):
    """Simple"""
    if folderName:
        folderPath = os.path.join(folderPath, folderName)
    if os.path.isdir(folderPath):
        return True
    else:
        return False

def createUniqueFileName(folderPath, fileName="", preIdString=" ", postIdString=""):
    """
    Gives a unique file name for a file name in a folder.
    """
    ###
    if fileName:
        fileNameWithPath = os.path.join(folderPath, fileName)
    else:
        fileNameWithPath = folderPath
        folderPath, fileName = separate_fileNameAndPath(folderPath, False)
    ###
    if not os.path.isfile(fileNameWithPath):
        return fileName
    else:
        uniqueNumber = 0
        fileNameList = separate_fileNameAndExtension(fileName)
        while True:
            uniqueNumber += 1
            fileName = fileNameList[0] + preIdString + str(uniqueNumber) + postIdString + "." + fileNameList[1]
            if not os.path.isfile(os.path.join(folderPath, fileName)):
                break
        return fileName

def createUniqueFolderName(folderPath, folderName="", preIdString=" ", postIdString=""):
    """
    Gives a unique file name for a file name in a folder/drive.
    """
    ###
    if folderName:
        folderName_withPath = os.path.join(folderPath, folderName)
    else:
        folderName_withPath = folderPath
        folderPath, folderName = separate_fileNameAndPath(folderName_withPath, False)
    ###
    if not os.path.isdir(folderName_withPath):
        return folderName
    else:
        uniqueNumber = 0
        while True:
            uniqueNumber += 1
            newFolderName = folderName + preIdString + str(uniqueNumber) + postIdString
            if not os.path.isdir(os.path.join(folderPath, newFolderName)):
                break
        return newFolderName

# FOLDER CREATION TOOLS
def createFolderPath(folderPath):
    """Simple"""
    os.makedirs(folderPath, exist_ok=True)

# FILE/FOLDER NAME TOOLS
def isValidFileName(fileName):
    """simple"""
    global illegalChars_inWinFiles, illegalFileNames_inWin
    if len(fileName) > 255:
        return False
    for character in fileName:
        if character in illegalChars_inWinFiles:
            return False
    if fileName.upper() in illegalFileNames_inWin:
        return False
    return True

def isValidFilePath(filePath):
    """simple"""
    global illegalFileNames_inWin, vinlistOfAlphabets_small
    if len(filePath) > 260:
        return False
    if filePath[0].lower() not in vinlistOfAlphabets_small:
        return False
    if filePath[1:3] != ":\\":
        return False
    for characterIndex in range(len(filePath)):
        if characterIndex == 1:
            continue
        if filePath[characterIndex] in ['<', '>', ':', '"', '/', '|', '?', '*']:
            return False
    for folderInPath in filePath.split("\\"):
        if folderInPath.upper() in illegalFileNames_inWin:
            return False
    return True

def convertIllegalToLegalStr_inWinFiles(String):
    """simple"""
    String = list(String)
    inputList  = ['\\', '<', '>', ':', '"' , '/', '|', '?', '*']
    outputList = ['⧵' , '˂', '˃', '꞉', "''", '⧸', 'ǀ', 'ॽ', '∗']
    for characterIndex in range(len(String)):
        if String[characterIndex] in inputList:
            String[characterIndex] = outputList[ inputList.index(String[characterIndex]) ]
    String = "".join(String)
    return String

def convertToValidFileName(fileName, preIllegalFileName="", postIllegalFileName="_"):
    """simple"""
    global illegalFileNames_inWin
    if len(fileName) > 255:
        fileName = fileName[0:255]
    fileName = convertIllegalToLegalStr_inWinFiles(fileName)
    if fileName.upper() in illegalFileNames_inWin:
        fileName = preIllegalFileName + fileName + postIllegalFileName
    return fileName

# FILE RENAME, MOVE, COPY, DELETE
def deleteToRecycleBin(filePath):
    """simple"""
    try:
        send2trash(filePath)
        return True
    except:
        return False
