import os
import shutil
from send2trash import send2trash
from vinTextTools import listOfAlphabets_small as vinlistOfAlphabets_small
import vinTerminalFormatting as vinTF
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

def trueIfFile_falseIfFolder__dangerDueToPriority(filePath, checkForFileNotFolder = True):
    """simple"""
    if checkForFileNotFolder:
        if os.path.isfile(filePath):
            return True
        else:
            return False
    else:
        if os.path.isdir(filePath):
            return False
        else:
            return True

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
    Gives a unique folder name for a folder name in a folder/drive.
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

def doesFileOrFolderExist(folderPath, fileName="", alsoReturn_trueIfFile_falseIfFolder=False):
    """
    if alsoReturn_trueIfFile_falseIfFolder==True, then the fuction returns 2 variables
    """
    if fileName:
        folderPath = os.path.join(folderPath, fileName)
    ####
    if os.path.isfile(folderPath):
        if alsoReturn_trueIfFile_falseIfFolder:
            return True, True
        else:
            return True
    ##
    if os.path.isdir(folderPath):
        if alsoReturn_trueIfFile_falseIfFolder:
            return True, False
        else:
            return True
    ##
    if alsoReturn_trueIfFile_falseIfFolder:
        return False, False
    else:
        return False

def createUniqueUniversalName_rec(folderPath, fileName="", inputIsAFolder_withDot=False, preIdString=" ", postIdString=""):
    rrrrrrrrrrrrrrrrrrr"""
    CAUTION: Set inputIsAFolder_withDot==True, if fileName is a folder, with dot/s.
    """
    ###
    if fileName:
        fileNameWithPath = os.path.join(folderPath, fileName)
    else:
        fileNameWithPath = folderPath
        folderPath, fileName = separate_fileNameAndPath(folderPath, False)
    ###
    if not os.path.isfile(fileNameWithPath):
        if not os.path.isdir(fileNameWithPath):
            return fileName
    else:





        if "." not in fileName:
            isFile = False
        if inputIsAFolder_withDot: ok
        
        
        
        
        
        
        
        
        
        
        
        
        
        uniqueNumber = 0
        fileNameList = separate_fileNameAndExtension(fileName)
        while True:
            uniqueNumber += 1
            fileName = fileNameList[0] + preIdString + str(uniqueNumber) + postIdString + "." + fileNameList[1]
            if not os.path.isfile(os.path.join(folderPath, fileName)):
                if not os.path.isdir(os.path.join(folderPath, fileName)):
                    break
        return fileName

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

##### working on this

def move_AndOrOr_Rename(initialFolderPath, finalFolderPath, initialFileName="", finalFileName="", fileExtensionAutoAdd=True, getFinalFileNameAuto_0fFN=False, preIdString=" ", postIdString=""):
    """
    CAUTION: getFinalFileNameAuto_0fFN works only if finalFileName is empty, nevertheless it must be kept False to keep fileExtensionAutoAdd enabled. (Check for the code::: #VINEEL_CODE_REFERENCE_1)
    CAUTION: If, both, fileExtensionAutoAdd==False and getFinalFileNameAuto_0fFN==False, then (and only then) the file extension will not be copied from initialFileName. (This can lead to an extensionless file, if not accounted for.)
    """
    try:
        ####
        if initialFileName:
            initialFilePath_full = os.path.join(initialFolderPath, initialFileName)
        else:
            initialFilePath_full = initialFolderPath
            initialFolderPath, initialFileName = separate_fileNameAndPath(initialFolderPath, False)
        fileIfTrue_folderIfFalse_var = trueIfFile_falseIfFolder__dangerDueToPriority(initialFilePath_full) ###
            ##
        if not finalFileName:
            if getFinalFileNameAuto_0fFN:
                finalFileName = initialFileName
            else:
                finalFolderPath, finalFileName = separate_fileNameAndPath(finalFolderPath, False)
        if not doesFolderExist(finalFolderPath): ###
            createFolderPath(finalFolderPath)
        ####
        if fileIfTrue_folderIfFalse_var:
            if not getFinalFileNameAuto_0fFN: #VINEEL_CODE_REFERENCE_1
                if fileExtensionAutoAdd:
                    finalFileName = copyExtension_FromWithToWithout(initialFileName, finalFileName)
            ##
        if fileIfTrue_folderIfFalse_var:
            finalFileName = createUniqueFileName(finalFolderPath, finalFileName, preIdString, postIdString)
        else:
            finalFileName = createUniqueFolderName(finalFolderPath, finalFileName, preIdString, postIdString)
        ####
        shutil.move(initialFilePath_full, os.path.join(finalFolderPath, finalFileName))
        return finalFileName
    except Exception as e:
        print("ERROR in vinFileManagement.move_AndOrOr_Rename(): ", end="")
        vinTF.printSpecial(e, vinTF.Red + vinTF.Bold)
        return False
