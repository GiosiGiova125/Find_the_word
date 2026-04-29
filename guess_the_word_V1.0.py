print("Hi! Welcome to find the word!")
clues = input("Do you want some clues? (yes or no): ")

if clues.lower() == "yes":
    print("Ok, let's start: first clue: Five letters for the first part, five for the second. In between? Pure emptiness (a space)")
    answare = input("Do you know it? (yes or no): ")
    
    if answare.lower() == "yes":
        guess = input("Write the secret word: ")
        if guess.lower() == "hello world":
            print("Good job! You found the secret word!")
        else:
            print("Wrong! Try again.")
            
    if answare.lower() == "no":
        print("Ok, second clue: In Italian, it sounds like 'Ciao Mondo', but in the coding world we use english")
        answare = input("Do you know it? (yes or no): ")
        
        if answare.lower() == "yes":
            guess = input("Write the secret word: ")
            if guess.lower() == "hello world":
                print("Good job! You found the secret word!")
        
        if answare.lower() == "no":
            print("Ok, third clue: It is the very first thing every programmer makes the computer say when a new code is born.")
            guess = input("Last chance! Write the word: ")
            if guess.lower() == "hello world":
                print("Good job! You found the secret word!")
            else:
                print("Retry! The word was: hello world")
else:
    print("Ok, no clues! See you later.")