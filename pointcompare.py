#!/usr/bin/python3

###################################################################################################
# This is an example of comparing two sets of points by using a simple eucledian distance forumla #
# creator: Markus Mayr, 2017                                                                      #
###################################################################################################

import csv
import math

vergleichsdistanz = 1 # Meter

def getSquareDistance(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


with open('a.csv', 'r') as setAfile, open('b.csv', 'r') as setBfile, open('results.csv', 'w') as resultsFile:
    # lets read these files into memory to speed up the process
    listA = list(csv.reader(setAfile))
    listB = list(csv.reader(setBfile))

    resultsWriter = csv.writer(resultsFile)
    resultsWriter.writerow(["PunktA", "istIdentMitPunktB", "Distanz"])
    for i, pointA in enumerate(listA):
        # ignore the first line, since it includes only the headers
        if i == 0: continue
        print("Prüfe Punkt A {}".format(i))
        for j, pointB in enumerate(listB):
            # ignore the first line, since it includes only the headers
            if j == 0: continue
            squareDistance = getSquareDistance(float(pointA[0]),float(pointA[1]),float(pointB[0]),float(pointB[1]))
            if squareDistance <= vergleichsdistanz ** 2:
                resultsWriter.writerow([pointA[2],pointB[2],math.sqrt(squareDistance)])
