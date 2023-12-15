# STOLEN FROM GITHUB SORRY

file = open("input.txt","r")
text = file.readlines()
ans = 0

dictionary = {
    "one":"o1e",
    "two":"t2o",
    "three":"t3e",
    "four":"f4r",
    "five":"f5e",
    "six":"s6x",
    "seven":"s7n",
    "eight":"e8t",
    "nine":"n9e",
    "zero":"z0o"
}

for line in text:
    firstDigit = None
    lastDigit = None
    translatedLine = line
    
    for key,value in dictionary.items():
        translatedLine = translatedLine.replace(key,value)
        
    for character in translatedLine:
        if character.isdigit() and firstDigit is None:
            firstDigit = character
            lastDigit = character
        
        elif character.isdigit():
            lastDigit = character
        
    if firstDigit is not None and lastDigit is not None:
        joined = firstDigit + lastDigit
        ans += int(joined)

file.close()
print(ans)
