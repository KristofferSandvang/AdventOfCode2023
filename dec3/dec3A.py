import re
file = open("input.txt","r")
text = file.readlines()
maxRowIndex = len(text) - 1
maxColIndex = len(text[0]) - 2 # - 2 to avoid dealing with \n

print(f"Maxrow = {maxRowIndex}")
print(f"Maxcol = {maxColIndex}")

def findNumbersAndIndices (lines: list) -> (list, list):
    parts = []
    indices = []
    current_number = ""

    for row_index, row in enumerate(lines):
        for col_index, char in enumerate(row):
            if char.isdigit():
                current_number += char
            elif current_number:
                parts.append(current_number)
                indices.append(((row_index, col_index - len(current_number)), (row_index, col_index - 1)))
                current_number = ""
    
    return parts, indices

# Generates a list of adjecent indices to check
def generateAdjecentIndices(indices: list) -> list:
    indicesToCheck = []
    if (indices[0][0] != indices[1][0]):
        raise ValueError("Numbers can't span mulitple rows")
    row = indices[0][0]

    # Adds indices above and below the found number
    for col in range(indices[0][1], indices[1][1] + 1):
        if row > 0:
            indicesToCheck.append((row - 1, col))
        if row < maxRowIndex:
            indicesToCheck.append((row + 1, col))

    # Adds Indices before and after the found number
    if indices[0][1] > 0:
        indicesToCheck.append((row, indices[0][1] - 1))
    if indices[1][1] < maxColIndex:
        indicesToCheck.append((row, indices[1][1] + 1))

    # Adds indices diagonally to the found number
    if (row - 1 >= 0 and indices[0][1] - 1 >= 0):
        indicesToCheck.append((row - 1, indices[0][1] - 1))
    if (row + 1 <= maxRowIndex and indices[0][1] - 1 >= 0):
        indicesToCheck.append((row + 1, indices[0][1] - 1))

    if (row - 1 >= 0 and indices[1][1] + 1 <= maxColIndex):
        indicesToCheck.append((row - 1, indices[1][1] + 1))
    if (row + 1 <= maxRowIndex and indices[1][1] + 1 <= maxColIndex):
        indicesToCheck.append((row + 1, indices[1][1] + 1))
    return indicesToCheck

def isPart(text: list,indices: list) -> bool:
    adjecentIndices = generateAdjecentIndices(indices)
    symbolPattern = r"[^a-zA-Z0-9_.]"

    for index in adjecentIndices:
        row, col = index
        # used to check everything was working
        # print(f"{index} = {text[row][col]} = {bool(re.match(symbolPattern, text[row][col]))}")
        if bool(re.match(symbolPattern, text[row][col])):
            return True
    return False


# def removeNonParts(text: list,parts: list, indices: list) -> list:
#     for i in range(len(parts) - 1):
#         if not(isPart(text, indices[i])):
#             del(parts[i])
#     print(parts)
#     return parts


def removeNonParts(text: list, parts: list, indices: list) -> list:
    parts_to_keep = [part for part, index in zip(parts, indices) if isPart(text, index)]
    # print(parts_to_keep)
    return [int(part) for part in parts_to_keep]

def calculateSumOfParts(parts: list):
    return sum(parts)

tmp = findNumbersAndIndices(text)
print(calculateSumOfParts(removeNonParts(text, tmp[0], tmp[1])))
