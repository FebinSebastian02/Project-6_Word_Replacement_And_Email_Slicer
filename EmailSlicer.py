def main():
    print("\n!!!Welcome to the Email Slicer!!!")
    while True:
        choice = int(input("\nDo you wish to use the Email Slicer 1) Yes 2)No..."))
        if choice == 1:
            email = input("Enter an email to slice...")
            userName, rest = email.split("@")
            print("\nThe user name is:- {}".format(userName))
            domain, extension = rest.split(".")
            print("The domain name is:- {}".format(domain))
            print("The extension is:- {}".format(extension))
        elif choice == 2:
            print("!!!Bye, See you soon!!!")
            quit()
        else:
            print("Invalid choice entered. Enter a valid choice")
main()