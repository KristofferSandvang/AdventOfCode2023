import re
file = open("input.txt","r")
text = file.readlines()


def splitString(orginialString: str, pattern: str) -> list:
    return re.split(pattern, orginialString)

def cleanNumberList(inputList: list) -> list:
    cleaned_list = [char for char in inputList if char != "" and char != " "]
    return cleaned_list
    
def determinePointsFromCards(text: str) -> None:
    points = 0
    for line in text:
        firstSplit = splitString(line, r"[:|]")
        numbers = []
        for split in firstSplit:
            if bool(re.match(r"Card( +)\d+", split)):
                continue
            numberSplit = splitString(split.strip(), r" ")
            cleanedNumberList = cleanNumberList(numberSplit)
            numbers.append((cleanedNumberList))
        tmpPoints = 0
        for number in numbers[1]:
            if number in numbers[0] and tmpPoints == 0 and number != " ":
                tmpPoints += 1
            elif number in numbers[0]:
                tmpPoints = tmpPoints * 2
        points += tmpPoints
    print(f"points = {points}")

def determineNumberMatches(cardInfo: str) -> None:
    firstSplit = splitString(cardInfo, r"[:|]")
    numbers = []
    for split in firstSplit:
        matched = re.match(r"Card( +)\d+", split)
        if bool(matched):
            continue
        numberSplit = splitString(split.strip(), r" ")
        cleanedNumberList = cleanNumberList(numberSplit)
        numbers.append((cleanedNumberList))
    matches = 0
    for number in numbers[1]:
        if number in numbers[0]:
            matches += 1
    return matches


def determineTotalCards(gameInfo: list) -> None:
    cards = [int(re.findall(r"Card +(\d+)", line)[0]) - 1 for line in gameInfo]
    cardResults = {}
    totalNumberofCards = len(cards)

    for card in cards:
        matches = determineNumberMatches(gameInfo[card])
        results = []
        if card in cardResults:
            resultingCards = cardResults.get(card)

            for resultCard in resultingCards:
                cards.append(resultCard)
                totalNumberofCards += 1
            continue

        for i in range(card, card + matches):
            cards.append(i + 1)
            results.append(i + 1)
            totalNumberofCards += 1

        cardResults[card] = results
    print(f"Total number of cards: {totalNumberofCards}")

determinePointsFromCards(text)
determineTotalCards(text)
