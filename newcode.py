import os
from operator import itemgetter
from typing import TextIO
# Reading all the files
folder: str = "InputFiles"
for inputFileName in os.listdir(folder):
    inputFile = os.path.join(folder, inputFileName)
    if os.path.isfile(inputFile):
        in_file: TextIO
        with open(inputFile) as in_file:
            guardIndex = 0
            timeList = []
            # Reading all the lines of a file
            for inputLine in in_file:
                inputIndex = inputLine.split()
                if len(inputIndex) == 2:
                    # Creating List of Tuples for time stamp and guard data
                    entryTuple = (int(inputIndex[0]), 'Entry', guardIndex)
                    exitTuple = (int(inputIndex[1]), 'Exit', guardIndex)
                    timeList.append(entryTuple)
                    timeList.append(exitTuple)
                    guardIndex += 1
            sortedTupleList = sorted(timeList, key=lambda x: x[0])
        # Finding minimum Time interval and Total time covered
        totalTimeCovered: int = 0
        timeIntervals = [0 for i in range(0, int(len(sortedTupleList)/2))]
        presentGuards = []
        for index, value in enumerate(sortedTupleList):
            timeInterval = value[0]
            if len(presentGuards) > 0:
                timeDifference = timeInterval - sortedTupleList[index - 1][0]
                totalTimeCovered += timeDifference
            if value[1] == 'Entry':
                presentGuards.append(value[2])
            else:
                presentGuards.remove(value[2])
            if len(presentGuards) == 1:
                timeIntervals[presentGuards[0]] += sortedTupleList[index + 1][0] - timeInterval

        # Finding the maximum time interval after removal of minimum duration
        maximum_interval = str(totalTimeCovered - min(timeIntervals))
        outputFile = open('OutputFiles/' + inputFileName.split('.')[0] + '.out', "w+")
        outputFile.write(maximum_interval)
        outputFile.close()
