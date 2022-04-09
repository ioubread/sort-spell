from pathlib import Path
import os
import datetime
from configs import *
import shutil

def readConfigFile(inputPath):

    returnList = []

    openedFile = open(inputPath)
    fileContent = openedFile.read()
    openedFile.close()

    splitBySection = fileContent.split("\n\n")

    for section in splitBySection:
        splitByLine = section.split("\n")
        sectionName = str(splitByLine[0])
        sectionWhitelist = list(splitByLine[1:])

        returnList.append([sectionName, sectionWhitelist])

    return returnList

def printDigestedConfigWhitelist(inputPath):
    for item in inputPath:
        print(f"PathName: {item[0]}")

        for items in item[1]:
            print(f"- {items}")

        print("\n")


def initialisePaths(pathnameDelete, pathnameSort):
    dirSortspell = Path.cwd()
    dirDelete = dirSortspell / Path(pathnameDelete)
    dirSort = dirSortspell / Path(pathnameSort)

    return dirSortspell, dirDelete, dirSort



def returnTotalUnsortedFiles(configs):

    totalUnsortedFiles = []

    for section in configs:
        sectionPath = section[0]
        sectionWhitelist = section[1]

        filesFound = []

        for file in os.listdir(Path(sectionPath)):
            filesFound.append(file)

        nonWhitelistedFiles = list(set(filesFound) - set(sectionWhitelist))

        toAddToTotal = []

        for index, item in enumerate(nonWhitelistedFiles):
            toAddToTotal.append(Path(sectionPath) / Path(item))
            # nonWhitelistedFiles[index] = Path(sectionPath) / Path(item)

        totalUnsortedFiles += toAddToTotal

    return totalUnsortedFiles


def checkIsDatefolder(inputDir):
    justTheFilename = str(Path(inputDir).name)
    justTheFilenameSplitted = justTheFilename.split(" ")
    firstPartOfName = (justTheFilenameSplitted[0]).lower()

    if (len(justTheFilenameSplitted) == 2) and ((justTheFilenameSplitted[1]).isnumeric) and (firstPartOfName == "jan" or firstPartOfName == "feb" or firstPartOfName == "mar" or firstPartOfName == "apr" or firstPartOfName == "may" or firstPartOfName == "jun" or firstPartOfName == "jul" or firstPartOfName == "aug" or firstPartOfName == "sep" or firstPartOfName == "oct" or firstPartOfName == "nov" or firstPartOfName == "dec"):
        return True
    else:
        return False


def checkMatchesCurrentDay(inputDir):
    
    # print(f"bzzz running the checkMatchesCurrentDay function")

    datetimeToday = datetime.datetime.today()
    datetimeMonth = datetimeToday.month
    datetimeDay = datetimeToday.day

    justTheFilename = str(Path(inputDir).name)
    dirPartMonth, dirPartDay = justTheFilename.split(" ")
    theMonths = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

    try:
        dirPartMonthNumber = int(theMonths.index(dirPartMonth.lower())) + 1
    except:
        # print(f"Triggered the except thooo")
        return False

    # print(f"strDirPartMontNumber{str(dirPartMonthNumber)}")
    # print(f"strDatetimeMonth{str(datetimeMonth)}")
    # print(f"strpartday{str(dirPartDay)}")
    # print(f"strdatetimeday{str(datetimeDay)}")

    dirPartDay = dirPartDay.lstrip("0")

    # print(f"Para1: {str(dirPartMonthNumber)}")
    # print(f"Para2: {str(datetimeMonth)}")
    # print(f"Para3: {str(dirPartDay)}")
    # print(f"Para4: {str(datetimeDay)}")



    if (str(dirPartMonthNumber) == str(datetimeMonth)) and (str(dirPartDay) == str(datetimeDay)):
        return True
    else:
        return False




def safemove(source, destination):

    source = str(source)
    destination = str(destination)

    if not os.path.exists(str(destination)):
        shutil.move(source, destination)
        print(f"SUCCESS: {source} -> {destination}\n")

    else:
        print(f"FAILURE: {source} -> {destination}\n")



# configFilePath = "config.txt"

# configfile = open("config.txt")

# configcontent = configfile.read()

# configfile.close()

# hnng = (configcontent.split("\n"))[0]

# allotherfiles = (configcontent.split("\n"))[1:]

# configFilePath = "config.txt"

digestedConfig = readConfigFile(configFilePath)

# printDigestedConfigWhitelist(digestedConfig)

dirSortspell, dirDelete, dirSort = initialisePaths(todeletePath, tosortPath)


# dirDesktop = hnng

# everysinglefile = []

# for file in os.listdir(Path(dirDesktop)):

#     everysinglefile.append(str(file))


# z = list(set(everysinglefile) - set(allotherfiles))

# for line in z:
#     print(line)



totalUnsortedFiles = returnTotalUnsortedFiles(digestedConfig)


inputList = totalUnsortedFiles


# for line in inputList:
#     pprint.pprint(line)





hasTodayDateFolder = False

# Sorting portion already
for thePath in inputList:
    thePath = str(thePath)

    if os.path.isdir(thePath):

        if checkIsDatefolder(thePath):

            if checkMatchesCurrentDay(thePath):
                hasTodayDateFolder = True
                # print(f"well, it matches today's date")
                # input()

            else:
                # print(f"it doesn't match today's date. weird.")
                # input()
                newPath = Path(hibiPath) / Path(thePath).name
                safemove(thePath, newPath)
                
                # print(newPath)

        else:
            newPath = Path(dirSort) / Path(thePath).name
            safemove(thePath, newPath)
            # print(newPath)

    elif os.path.isfile(thePath):
        newPath = Path(dirSort) / Path(thePath).name
        safemove(thePath, newPath)
        # print(newPath)


    # print(f"{str(thePath)} -> {str(newPath)}\n")


if not hasTodayDateFolder:

    currentDir = Path.cwd()

    os.chdir(hibiPath)

    # print(Path.cwd())

    dateFoldersSorted = sorted(filter(os.path.isdir, os.listdir('.')), key=os.path.getmtime)

    latestFolder = dateFoldersSorted[-1]

    os.chdir(latestFolder)

    allFilesHere = []

    filesHereSorted = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)

    # for file in os.listdir("."):
    for file in filesHereSorted:
        allFilesHere.append(file)

    latestFile = allFilesHere[-1]

    dateTxtfile = open(latestFile)
    dateFilecontent = dateTxtfile.read()
    dateTxtfile.close()

    todayis = datetime.datetime.today()

    currentMonth = todayis.month
    currentDay = todayis.day

    theMonths = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

    currentMonthWord = (theMonths[int(currentMonth) - 1]).title()

    if len(str(currentDay)) == 1:
        currentDayWord = "0" + str(currentDay)

    elif len(str(currentDay)) == 2:
        currentDayWord = str(currentDay)

    finalDatefolderName = currentMonthWord + " " + currentDayWord
    finalDateTxtfileName = "1.txt"

    os.chdir(Path.home() / "Desktop")

    os.mkdir(finalDatefolderName)

    os.chdir(finalDatefolderName)

    finalDateTxtFile = open(finalDateTxtfileName, "w")
    finalDateTxtFile.write(dateFilecontent)
    finalDateTxtFile.close()

    
    




# for hibi in os.listdir(hibiPath):
#     print(hibi)



input()