import re
file = open("input.txt","r")
text = file.readlines()

def getRaceValues(raceLine: str) -> list:
    raceValues = []
    timePattern = r"\d+"
    matches = re.findall(timePattern, raceLine)
    for match in matches:
        raceValues.append(int(match))
    return raceValues



def determineWinningSpeeds(raceTime: int, raceRecord: int) -> list:
    winningSpeeds = []
    speed = 0
    while (speed < raceTime):
        distanceTravelled = speed * (raceTime - speed)
        if (distanceTravelled > raceRecord):
            winningSpeeds.append(speed)
        speed += 1
    return winningSpeeds

raceTimes = getRaceValues(text[0])
raceRecords = getRaceValues(text[1])

raceInfo = list(zip(raceTimes, raceRecords))

combinations = 1
for raceDuration, raceRecord in raceInfo:
    winningSpeeds = determineWinningSpeeds(raceDuration, raceRecord)
    combinations *= len(winningSpeeds)
print(combinations)

# Part 2
def getRealRaceValues(fakeRaceValues: list) -> int:
    realRaceValue = ""
    for value in fakeRaceValues:
        realRaceValue += str(value)
    return int(realRaceValue)

realRaceTime = getRealRaceValues(raceTimes)
realRaceRecord = getRealRaceValues(raceRecords)

winningSpeedsPart2 = determineWinningSpeeds(realRaceTime, realRaceRecord)

print(len(winningSpeedsPart2))