def how_to_play():
    print("Hello! Welcome to Floodit!")
    print("Please enter matching symbols in order to fill in the entire board.")

def handle_input(gameboard):
    
    while true:
        # Check for gameboard end here
        while true:
            color = input("Enter a character: ")

            if len(color) != 1:
                print("Not a valid character.")
                continue

            print("Print gameboard here")

        # Check for gameboard victory vs failure
        if true:
            print("Victory!")
        else:
            print("Defeat!")

        try_again = input("Try again (y/n): ")
        if try_again == 'y':
            print("Trying again")
        else:
            print("Exiting")
            break