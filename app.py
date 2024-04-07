from collections import deque

# USED FOR TESTING
# file = open("text.txt", "r")
# ciphertext = file.read()
# file.close()

ciphertext = input("Enter your ciphertext: ")

ciphertext = ciphertext.upper()

# Freq is an ordered list of characters from most frequent to least frequent in the english language
freq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'L', 'D', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

# Count is a dictionary that represents the frequencies of all letters in the ciphertext
count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
         'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

print("The origional cipher text: \n" + ciphertext)

# Function to fill up dictionary and sort it 
def tally(text):
    for char in text:
        char = char
        if char in count:
            count[char] += 1
    return sorted(count.items(), key=lambda x: x[1], reverse=True)

# Array of tuples that represents the ordered count dictionary
ordered = tally(ciphertext)

# Map the most frequent characters to their assigned character in the frequency list
orgionals = deque([])
for item in ordered:
    orgionals.append(item[0])


# Replace characters function
# 1. For every character in the text do the following:
# 2. Define newText to be the new text
# 3. If the character is orgional, add alternate to the new text
# 4. If the character is alternate, add orgional to the new text
# 5. Else add the character to the new text
def substitute(orgional, alternate, text):
    newText = ""
    for char in text:
        if char == orgional:
            newText += alternate
        elif char == alternate:
            newText += orgional
        else:
            newText += char
    return newText

alternates = deque(freq)

seen = [] # an array of characters that have already been seen in the de-cipher process

# Decode function
# 1. While orgionals is not empty or alternates is not empty do the following:
# 2. Pop from the beginning of the count dictionary and assign it to a variable called orgional
# 3. Pop from the beginning of the freq array and assign it to a variable called alternate
# 4. If old char or new char is found in the seen array, repeat step 1 and 2
# 5. Run replace characters with orgional, alternate, and text
# 6. orgional and alternate to seen, and repeat from step 1.
def decode(ciphertext):
    text = ciphertext
    while len(orgionals) > 0 and len(alternates) > 0:
        orgional = orgionals.popleft()
        alternate = alternates.popleft()
        if orgional in seen or alternate in seen:
            continue
        text = substitute(orgional, alternate, text)
        seen.append(orgional)
        seen.append(alternate)
    return text

text = decode(ciphertext)
print("\nThe decoded text from frequency analysis: \n" + text)

# User input
# Prompt user to begin replacing letters manually 
user_input = input("\nWould you like to replace letters? (y) yes or (n) no: ")
if user_input == "y":
    while user_input != "-":
        orgional = input("\nEnter the letter that you wish to replace (or submit '-'): ")
        if orgional == "-":
            break
        if orgional not in text:
            print(f"'{orgional}' is not in the text")
            continue
        alternate = input("\nEnter the character you would like to replace it with: ")
        text = substitute(orgional, alternate, text)
        print("\n" + text)