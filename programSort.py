from pathlib import Path
import os
import shutil

configFilePath = "configSort.txt"
tosortPath = "tosort"

def digestConfigFile(configPath):
    configFile = open(configPath)
    configContent = configFile.read()
    configFile.close()

    returnHeaders = []
    returnDestinations = []

    splittedContent = configContent.split("\n")

    for line in splittedContent:

        partitioned = line.partition("|")

        returnHeaders.append(partitioned[0])
        returnDestinations.append(partitioned[2])

    return returnHeaders, returnDestinations


def getDestinationPath(digestedHeaders, digestedDestinations, targetDestination):

    try:

        targetIndex = digestedHeaders.index(targetDestination)
        returnDestination = digestedDestinations[targetIndex]
        return returnDestination

    except:
        return False


    
def safemove(source, destination):

    source = str(source)
    destination = str(destination)

    if not os.path.exists(str(destination)):
        shutil.move(source, destination)
        return True
        # print(f"SUCCESS: {source} -> {destination}\n")

    else:
        return False
        # print(f"FAILURE: {source} -> {destination}\n")








readyHeaders, readyDestinations = digestConfigFile(configFilePath)

print(f"Possible headers: ")
for header in readyHeaders:
    print(f"- {header}")
print("\n")

totalFiles = 0
for file in os.listdir(Path.cwd() / tosortPath):
    totalFiles += 1

counter = 0
for file in os.listdir(Path.cwd() / tosortPath):
    counter += 1

    originalPath = Path.cwd() / tosortPath / file

    userinput = ((input(f"[{counter}/{totalFiles}] {file} -> ")).strip()).lower()

    tryGetDestination = getDestinationPath(readyHeaders, readyDestinations, userinput)

    while (userinput != "") and (not tryGetDestination):
        print("TRY AGAIN (BLANK to skip)\n")
        userinput = ((input(f"{file} -> ")).strip()).lower()
        tryGetDestination = getDestinationPath(readyHeaders, readyDestinations, userinput)

    if tryGetDestination:
        finalPath = Path(tryGetDestination) / file
        moveResult = safemove(originalPath, finalPath)
        if moveResult:

            print(f"{originalPath} -> \n{finalPath}\n")
        else:
            print("safemove() ERROR\n")

    elif userinput == "":
        print("NEXT\n")

    # else:
    #     print("ERROR\n")
    #     continue


    


input()