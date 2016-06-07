print(55 * '-')
print("                      M E N U                      ")
print(55 * '-')
print("0. Read Data Files")
print("1. Display Statistics ")
print("2. Top 5 Most Tweeted Words")
print("3. Top 5 Most Tweeted Users")
print("4. Find Users who tweeted a word")
print("5. Find All People who are friends of the above users")
print("6. Delete Users who mentioned a word ")
print("7. Delete All Users who mentioned a word ")
print("8. Find Strongly Connected Components")
print("9. Find Shortest Path from a given user")
print("99. Quit")
print(55 * '-')

# Get input
choice = input('Select Menu : ')

# Convert string to int type #
choice = int(choice)

# Take action as per selected menu-option
if choice == 0:
    print("Reading Data Files...")
elif choice == 1:
    print("Displaying Statistics...")
elif choice == 2:
    print("Showing Top 5 Most Word...")
elif choice == 3:
    print("Showing Top 5 Most User...")
elif choice == 4:
    print("Finding User...")
elif choice == 5:
    print("Finding All People...")
elif choice == 6:
    print("Deleting Users...")
elif choice == 7:
    print("Deleting All Users...")
elif choice == 8:
    print("Finding SCC...")
elif choice == 9:
    print("Finding Shortest Path...")
elif choice == 99:
    print("Good Bye")
else:  ## default ##
    print("Invalid number. Try again...")