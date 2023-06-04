# import pyperclip
import sys
import os
import pprint
import time


unx = str(round(time.time()))

presumedFileName = str(sys.argv[1])

splittedPath = os.path.split(presumedFileName)

# print(str(splittedPath))

folderPath, actualFilename = splittedPath

# print(f"first part: {folderPath}")
# print(f"second part: {actualFilename}")

# input()





configFile = open("config.txt", "r")

configFileContents = configFile.read()
configFile.close()

configFileContentsSplitted = configFileContents.split("\n\n")

configCategories = {}

foundAFolder = False
# foundFolderToUse = ""

for configChunk in configFileContentsSplitted:
    furtherSplitted = configChunk.split("\n")

    categoryName = furtherSplitted[0]
    restOfItems = furtherSplitted[1:]

    configCategories[categoryName] = restOfItems


    # print(f"categoryName according to splitting this chunk: {categoryName}")
    # print(f"folderPath: {folderPath}")

    if categoryName == folderPath:
        # print(f"category name does equal folder path, tho...")
        # print(f"OH I FOUND ONE for {categoryName}")
        # input()
        foundAFolder = True
        # foundFolderToUse = categoryName

        # pprint.pprint(restOfItems)

        if actualFilename in restOfItems:
            pass
        
        else:
            
            restOfItems.append(actualFilename)
            configCategories[categoryName] = restOfItems

            # print(f"Added to whitelist")

        
    

    # print(f"foundAFolder = {foundAFolder}")
    # print(f"foundFolderToUse = {categoryName}")

    # input()


# print(f"it is {foundAFolder} that we've found a folder for this")


if foundAFolder == False:
    print(folderPath)
    itemsToAdd = []
    itemsToAdd.append(actualFilename)
    configCategories[folderPath] = itemsToAdd

# input()

# sys.exit()

# pprint.pprint(configCategories)

# print(configCategories)

combinedListOfThingsToWriteOut = []



for key, value in configCategories.items():
    toWriteOut = []
    toWriteOut.append(key)

    toWriteOut += value

    combinedListOfThingsToWriteOut.append("\n".join(toWriteOut))

    # print(toWriteOut)
    # print(f"{key}")
    # # pprint.pprint(value)

    # for item in value:
    #     print(item)
    
    # print("")


finalToWrite = "\n\n".join(combinedListOfThingsToWriteOut)


# print(finalToWrite)

# print(f"foundAFolder = {foundAFolder}")
# print(f"foundFolderToUse = {categoryName}")

outputFile = open(f"addToWhitelistConfigOutput_{unx}_config.txt", "w")
outputFile.write(finalToWrite)
outputFile.close()




# input()