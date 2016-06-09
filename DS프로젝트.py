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


def read_file():
    ucount = 0
    u = open('user.txt')
    for line in u:
        line = line[0:-1]
        ucount += 1
        #print(line)
    print('Total User: ', ucount/4)

    fcount = 0
    f = open('friend.txt')
    for line in f:
        line = line[0:-1]
        fcount += 1
       #print(line)
    print('Total Friendship Records: ', fcount/3*2)

    wcount = 0
    w = open('word.txt')
    for line in w:
        line = line[0:-1]
        wcount += 1
       #print(line)
    print('Total Tweets: ', wcount/4)

m = dict()

def count(word):
    if m.get(word):
        m[word] += 1
    else: m[word] = 1


# Take action as per selected menu-option
if choice == 0:
    print("Reading Data Files...")
    read_file()

elif choice == 1:
    print("Displaying Statistics...")
'''   Top 5 friends
    f = open('friend.txt')
    for line in f:
        line = line[0:-1]
        count(line)
    del m['']
    top = sorted(m, key=m.get, reverse=True)[:5]
    for i in range(5):
        print(top[i],m[top[i]])
'''
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
else:  # default
    print("Invalid number. Try again...")
