file = open("text.txt", "r")
cyphertext = file.read()
file.close()

freq = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'L', 'D', 'C', 'U', 'M', 'W', 'F', 'G', 'Y', 'P', 'B', 'V', 'K', 'J', 'X', 'Q', 'Z']

count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0,
         'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}

# Function to fill up dictionary
def tally(text):
    for char in text:
        char = char
        if char in count:
            count[char] += 1
    global ordered 
    ordered = sorted(count.items(), key=lambda x: x[1], reverse=True)


# Function to clear dictionary
def clear_all():
    for char in count.keys():
        count[char] = 0
        global ordered 
        ordered = []
        

tally(cyphertext)

# Sort the dictionary by values in descending order

print("\nordered", ordered)

# Create a new variable to store the modified plaintext
decrypted_text = cyphertext

# Replace characters based on frequency analysis
def decode():
    for index in range(26):
        global decrypted_text
        decrypted_text = decrypted_text.replace(ordered[index][0],freq[index].lower())
decode()
print("\nBefore: " + cyphertext)
print("\nAfter: " + decrypted_text.upper()+"\n")

clear_all()

# Now using this as a base and add make it read a user input just replace 'file' with input

input = input("Enter your cyphertext: \n")
print("Cyphertext is: " + input)