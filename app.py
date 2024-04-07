from collections import deque

file = open("text.txt", "r")
cyphertext = file.read()
file.close()

freq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'L', 'D', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
         'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

print("The origional cipher text: \n" + cyphertext)

# Function to fill up dictionary
def tally(text):
    for char in text:
        char = char
        if char in count:
            count[char] += 1
    return sorted(count.items(), key=lambda x: x[1], reverse=True)

# Function to clear dictionary
def clear_all():
    for char in count.keys():
        count[char] = 0
        global ordered 
        ordered = []
        

# Array of tuples that represents the ordered count dictionary
ordered = tally(cyphertext)

# Map the most frequent characters to their assigned character in the frequency list
oldChars = deque([])
for item in ordered:
    oldChars.append(item[0])

# Sort the dictionary by values in descending order

# print("\nordered", ordered)

# Create a new variable to store the modified plaintext
decrypted_text = cyphertext

# Replace characters based on frequency analysis
# def decodeOld():
#     for index in range(26):
#         global decrypted_text
#         decrypted_text = decrypted_text.replace(ordered[index][0],freq[index].upper())
# decodeOld()
# print(decrypted_text)

# Replace characters function
# 1. For every character in the text do the following:
# 2. Define newText to be the new text
# 3. If the character is oldChar, add newChar to the new text
# 4. If the character is newChar, add oldChar to the new text
# 5. Else add the character to the new text
def repace_characters(oldChar, newChar, text):
    newText = ""
    for char in text:
        if char == oldChar:
            newText += newChar
        elif char == newChar:
            newText += oldChar
        else:
            newText += char
    return newText

newChars = deque(freq)

seen = [] # an array of characters that have already been seen in the de-cipher process

# Decode function
# 1. While oldChars is not empty or newChars is not empty do the following:
# 2. Pop from the beginning of the count dictionary and assign it to a variable called oldChar
# 3. Pop from the beginning of the freq array and assign it to a variable called newChar
# 4. If old char or new char is found in the seen array, repeat step 1 and 2
# 5. Run replace characters with oldChar, newChar, and text
# 6. oldChar and newChar to seen, and repeat from step 1.
def decode(cyphertext):
    text = cyphertext
    while len(oldChars) > 0 and len(newChars) > 0:
        oldChar = oldChars.popleft()
        newChar = newChars.popleft()
        if oldChar in seen or newChar in seen:
            continue
        text = repace_characters(oldChar, newChar, text)
        seen.append(oldChar)
        seen.append(newChar)
    return text

text = decode(cyphertext)
print("\nThe decoded text from frequency analysis: \n" + text)

# User input
# Prompt user to begin replacing letters manually 
user_input = input("\nWould you like to replace letters? (y) yes or (n) no: ")
if user_input == "y":
    while user_input != "-":
        oldChar = input("\nEnter the letter that you wish to replace (or submit '-'): ")
        if oldChar == "-":
            break
        if oldChar not in text:
            print(f"'{oldChar}' is not in the text")
            continue
        newChar = input("\nEnter the character you would like to replace it with: ")
        text = repace_characters(oldChar, newChar, text)
        print("\n" + text)