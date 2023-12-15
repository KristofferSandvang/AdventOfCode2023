import re
file = open("input.txt","r")
text = file.readlines()

# Total number of different colored cubes:
# red = 12
# green = 13
# blue = 14

# Requires that the list is of form [redCubes, greenCubes, blueCubes]
def gamePossible(combination: list, maxRed = 12, maxGreen = 13, maxBlue = 14) -> bool:
    result = False
    if (combination[0] <= maxRed and combination[1] <= maxGreen and combination[2] <= maxBlue):
        result = True
    return result

# Splits the string after each semicolon
def splitString(everyCombination: str) -> list:
    splitPattern = r":|;|\n"
    return re.split(splitPattern, everyCombination)

# skal bare lige lave en liste for hvert ting
def createCubeCombination(cubeCombination: str) -> list:
    cubePattern = r"(\d+) (green|red|blue)"
    matches = re.findall(cubePattern, cubeCombination)
    combinationList = [0, 0, 0]
    for match in matches:
        if match[1] == "red":
            combinationList[0] = int(match[0])
        elif match[1] == "green":
            combinationList[1] = int(match[0])
        elif match[1] == "blue":
            combinationList[2] = int(match[0])
    return combinationList

def fewestCubesNeeded(cubeCombinations: list) -> list:
    minRed = 0
    minGreen = 0
    minBlue = 0
    for cubeCombination in cubeCombinations:
        if (minRed < cubeCombination[0]):
            minRed = cubeCombination[0]
        if (minGreen < cubeCombination[1]):
            minGreen = cubeCombination[1]
        if (minBlue < cubeCombination[2]):
            minBlue = cubeCombination[2]
    return [minRed, minGreen, minBlue]

def checkAllgames(gameData : list) -> int:
    gameIDPattern = r"Game (\d+):"
    idSum = 0
    powerSum = 0
    for line in gameData:
        id = re.search(gameIDPattern, line).group(1)
        cubesShown = splitString(line)
        possible = True
        listOfShownCubes = []
        for combination in cubesShown:
            cubeCombination = createCubeCombination(combination)
            listOfShownCubes.append(cubeCombination)
            if (gamePossible(cubeCombination) and possible != False):
               possible = True
            else:
                possible = False
        minCubesNeeded = fewestCubesNeeded(listOfShownCubes)
        product = minCubesNeeded[0] * minCubesNeeded[1] * minCubesNeeded[2]
        powerSum += product
        if possible:
            idSum += int(id)
    
    print(f"gameID sum = {idSum}")
    print(f"power sum = {powerSum}")


checkAllgames(text)