# Hangman
# Zoe DeGuzman

word = list(input("Player 1, what's the word? ").upper()) #gets word
print("\n" * 40)

guessed = list("_" * len(word)) # makes list of guesses same length as word
already_guessed = []
letter = ""
num_guesses = 5 #sets number of allowed wrong guesses to 5
print("Player 2, try to guess the word before Graham's face is printed out")

# this function prints out graham's face
def draw(n):
    f = open("graham.txt", "r") # opens graham.txt
    for x in range(0, (5-n) * 4 + 1): #for loop to print out specific sections of the text file
        print(f.readline(), end="")

while True:
    print("-" * 40)
    letter = input("Player 2, guess a letter: ").upper()

    if letter in already_guessed: #checks to see if the letter has already been guesses
        letter = ""
        print("Player 2, you already guessed this letter")

    elif letter in word: #checks to see if the letter in in the word
        already_guessed.append(letter)
        indices = [i for i, x in enumerate(word) if x == letter] #finds all indices of letter in word
        for x in range(0, len(indices)): #loops through the indices list
            guessed[indices[x]] = letter #adds each index to guessed
            word[indices[x]] = "_" #sets indices in word to _
        print("".join(guessed)) #prints out the guessed word so far

    else: # this runs if the guessed letter is not in word
        already_guessed.append(letter) 
        num_guesses -= 1
        print("Wrong! Guesses left: " + str(num_guesses)) #prints out number of guesses left
        print("")
        draw(num_guesses) #prints out section of graham's face depending on the amount of guesses left
        print("")

        if num_guesses == 0: #runs if player 2 has no guesses left
            print("Player 2, you ran out of guesses. You lose!")
            break            
        
    if "_" not in guessed: #checks to see if the word has been totally guesses
        print("Player 2, you won")
        break
