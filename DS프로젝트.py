import re

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

def sum():
    res = 0
    for i in m:
        res += m[i]
    return res

def count(word):
    if m.get(word):
        m[word] += 1
    else: m[word] = 1

# Take action as per selected menu-option
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
if choice == 0:
    print("Reading Data Files...")
    read_file()
elif choice == 1:
    print("Displaying Statistics...")
    f = open('friend.txt')
    for line in f:
        line = line[0:-1]
        count(line)
    del m['']
    maximumf = max(m, key = m.get)
    minimumf = min(m, key = m.get)
    print("Average Number of Friends:", sum()/len(m))
    print("Maximum Number of Friends:", maximumf, "=>", m[maximumf])
    print("Minimum Number of Friends:", minimumf, "=>", m[minimumf])
    m.clear()

    for i,l in enumerate(open('word.txt')):
        if i%4 == 0:
            count(l)
    maximumt = max(m, key = m.get)
    minimumt = min(m, key = m.get)
    print("Average Tweet per User:", sum()/len(m))
    print("Maximum Tweet per User:", maximumt.rstrip(), "=>", m[maximumt])
    print("Minimum Tweet per User:", minimumt.rstrip(), "=>", m[minimumt])
    m.clear()
elif choice == 2:
    print("Showing Top 5 Most Tweeted Words...")
    for i, l in enumerate(open('word.txt')):
        if i % 4 == 2:
            count(l)
    top = sorted(m, key=m.get, reverse=True)[:5]
    for i in range(5):
        print(top[i].rstrip(), ":", m[top[i]])
elif choice == 3:
    print("Showing Top 5 Most Tweeted Users...")
    for i, l in enumerate(open('word.txt')):
        if i % 4 == 2 and '@' in l:
            count(l)
    top = sorted(m, key=m.get, reverse=True)[:5]
    for i in range(5):
        print(top[i].rstrip(), ":", m[top[i]])
elif choice == 4:
    print("Finding Users who tweeted a word...")
    text = str(input("Word: "))
    total = 0
    lst = []
    for l in open('word.txt'):
        lst.append(l)
        total += 1
        if text == l[:-1]:
            print(lst[total-3].rstrip(), "=>", l)
elif choice == 5:
    print("Find All People who are friends of the above users...")
    text = str(input("Word: "))
    totalw = 0
    totalf = 0
    lstw = []
    lstf = []
    for l in open('word.txt'):
        lstw.append(l)
        totalw += 1
        if text == l[:-1]:
            print("User who tweet a word: ", lstw[totalw - 3].rstrip())
            break
    for ll in open('friend.txt').read().split():
        lstf.append(ll)
        totalf += 1
    print(lstf)
        #if lstw[totalw - 3].rstrip() == ll[:-1]:
            #print("All Users who are Friend: ", lstf[totalf])
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
