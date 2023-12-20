import re
file = open("input.txt","r")
text = file.readlines()

def getSeeds(seedLine: str) -> list:
    seedList = []
    seedPattern = r"\d+"
    matches = re.findall(seedPattern, seedLine)
    for match in matches:
        seedList.append(int(match))
    return seedList


def createDict4Map(inputText: list) -> list:
    dictMap = {}
    for line in inputText:
        # extract the numbers from the line and append them to soil list
        rangeList = []
        numberPattern = r"\d+"
        matches = re.findall(numberPattern, line)
        for match in matches:
            rangeList.append(int(match))

        if (len(rangeList) <= 0):
            continue

        destination = rangeList[0]
        source = rangeList[1]
        infoRange = rangeList[2]

        for i in range(infoRange):
            dictMap[source + i] = destination + i
    return dictMap

def findIndicesForMap(inputText: list, mapIdentifier: str) -> (int, int):
    startIndex = -1
    endIndex = -1
    for i in range(len(inputText)):
        line = inputText[i]
        if mapIdentifier in line:
            startIndex = i
        elif line == "\n" and startIndex != -1:
            endIndex = i
            break 
        elif i == len(inputText) -1:
            endIndex = i
    return int(startIndex), int(endIndex)

def seeds2Location(seeds: list, maps: dict) -> list:
    locations = []
    for seed in seeds:
        soil = -1
        if seed in maps['seed2Soil']:
            soil = maps['seed2Soil'].get(seed)
        else:
            soil = seed
        
        fertilizer = -1
        if soil in maps['soil2Fert']:
            fertilizer = maps['soil2Fert'].get(soil)
        else: 
            fertilizer = soil

        water = -1
        if fertilizer in maps['fert2Water']:
            water = maps['fert2Water'].get(fertilizer)
        else:
            water = fertilizer
        

    return locations

def get_value_or_default(key, map_dict, default):
    return map_dict.get(key, default)

def seeds2Location(seeds: list, maps: dict) -> list:
    map_names = ['seed2Soil', 'soil2Fert', 'fert2Water', 'water2Light', 'light2Temp', 'temp2Hum', 'hum2Loc']

    current_value = seeds

    for map_name in map_names:
        current_value = [get_value_or_default(value, maps[map_name], value) for value in current_value]
    
    return current_value


def findLowestLocation4Seed(inputText: list) -> None:
    seeds = []
    maps = {}
    for line in inputText:
        if 'seeds' in line:
            seeds = getSeeds(line)
    soilSection = findIndicesForMap(inputText, 'seed-to-soil map:') 
    maps['seed2Soil'] = createDict4Map(inputText[soilSection[0]:soilSection[1]])
    fertilizerSection = findIndicesForMap(inputText, 'soil-to-fertilizer map:')
    maps['soil2Fert'] = createDict4Map(inputText[fertilizerSection[0]:fertilizerSection[1]])
    
    waterSection = findIndicesForMap(inputText, 'fertilizer-to-water map:')
    maps['fert2Water'] = createDict4Map(inputText[waterSection[0]:waterSection[1]])

    lightSection = findIndicesForMap(inputText, 'water-to-light map:')
    maps['water2Light'] = createDict4Map(inputText[lightSection[0]:lightSection[1]])

    temperatureSection = findIndicesForMap(inputText, 'light-to-temperature map:')
    maps['light2Temp'] = createDict4Map(inputText[temperatureSection[0]:temperatureSection[1]])

    humidtySection = findIndicesForMap(inputText, 'temperature-to-humidity map:')
    maps['temp2Hum'] = createDict4Map(inputText[humidtySection[0]:humidtySection[1]])

    locationSection = findIndicesForMap(inputText, 'humidity-to-location map:')
    maps['hum2Loc'] = createDict4Map(inputText[locationSection[0]:locationSection[1]])

    locations = seeds2Location(seeds, maps)
    print(locations)
    print(min(locations))


findLowestLocation4Seed(text)

print()
# def createSeed2SoilDict():
