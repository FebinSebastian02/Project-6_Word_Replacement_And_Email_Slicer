def main():
    print("\n!!!Welcome to the Word Replacer!!!")
    while True:
        choice = int(input("\nDo you wish to use the Word Replacer 1) Yes 2) No..."))
        if choice == 1:
            sent = input("Enter a sentence...")
            print("The entered sentence is:- {}".format(sent))
            wordToBeReplaced = input("\nEnter the word from sentence that needs to be replaced...")
            wordReplacement = input("Enter the word with which you need to replace the word to be replaced...")
            replacedSent = sent.replace(wordToBeReplaced, wordReplacement)
            print("\nThe replaced sentence is:- {}".format(replacedSent))

        elif choice == 2:
            print("\n!!!Bye,See you soon!!!")
            quit()
        else:
            print("\nInvalid choice entered. Please enter a valid choice")
main()