import re

m = dict()

def sum():
    res = 0
    for i in m:
        res += m[i]
    return res

def count(word):
    if m.get(word):
        m[word] += 1
    else:
        m[word] = 1

def read_file():
    print("Reading Data Files...")
    ucount = 0
    u = open('user.txt')
    for line in u:
        line = line[0:-1]
        ucount += 1
        # print(line)
    print('Total User: ', ucount / 4)
    fcount = 0
    f = open('friend.txt')
    for line in f:
        line = line[0:-1]
        fcount += 1
        # print(line)
    print('Total Friendship Records: ', fcount / 3 * 2)
    wcount = 0
    w = open('word.txt')
    for line in w:
        line = line[0:-1]
        wcount += 1
        # print(line)
    print('Total Tweets: ', wcount / 4)

def statistic():
    print("Displaying Statistics...")
    f = open('friend.txt')
    for line in f:
        line = line[:-1]
        count(line)
    del m['']
    maximumf = max(m, key=m.get)
    minimumf = min(m, key=m.get)
    print("Average Number of Friends:", sum() / len(m))
    print("Maximum Number of Friends:", maximumf, "=>", m[maximumf])
    print("Minimum Number of Friends:", minimumf, "=>", m[minimumf])
    m.clear()

    for i, l in enumerate(open('word.txt')):
        if i % 4 == 0:
            count(l)
    maximumt = max(m, key=m.get)
    minimumt = min(m, key=m.get)
    print("Average Tweet per User:", sum() / len(m))
    print("Maximum Tweet per User:", maximumt.rstrip(), "=>", m[maximumt])
    print("Minimum Tweet per User:", minimumt.rstrip(), "=>", m[minimumt])
    m.clear()

def mostword():
    print("Showing Top 5 Most Tweeted Words...")
    for i, l in enumerate(open('word.txt')):
        if i % 4 == 2:
            count(l)
    top = sorted(m, key=m.get, reverse=True)[:5]
    for i in range(5):
        print(top[i].rstrip(), ":", m[top[i]])
    m.clear()

def mostuser():
    print("Showing Top 5 Most Tweeted Users...")  # Tweet 많이 한 사람
    for i, l in enumerate(open('word.txt')):
        if i % 4 == 0:
            count(l)
    top = sorted(m, key=m.get, reverse=True)[:5]
    for i in range(5):
        print(top[i].rstrip(), ":", m[top[i]])
    m.clear()

def userfind():
    print("Finding Users who tweeted a word...")
    text = str(input("Word: "))
    lst = []
    buffer = 0
    for i, l in enumerate(open('word.txt')):
        l = l[:-1]
        if i % 4 == 0:
            buffer = l
        if i % 4 == 2 and text == l:
            if buffer not in lst:
                lst.append(buffer)
    return lst

def userfriend():
    print("Finding All People who are friends of the above users...")
    users = userfind()
    d = {}
    buffer = 0
    for i, l in enumerate(open('friend.txt')):
        l = l[:-1]
        if i % 3 == 0:
            if l in users:
                if d.get(l) is None:
                    d[l] = []
                buffer = l
        if i % 3 == 1 and buffer in d:
            d[buffer].append(l)
            buffer = 0
    return d

def delword():
    print("Deleting Words which is mentioned")
    text = str(input("Word: "))
    lst = []
    for i, l in enumerate(open('word.txt')):
        l = l[:-1]
        if i % 4 == 2 and text != l:
            if l not in lst:
                lst.append(l)
    return lst

def deluser():
    print("Deleting Users who mentioned a word")
    text = str(input("Word: "))
    people = []
    for i, l in enumerate(open('word.txt')):
        l = l[:-1]
        if i % 4 == 0:
            if l not in people:
                people.append(l)
    lst = []
    buffer = 0
    for ii, ll in enumerate(open('word.txt')):
        ll = ll[:-1]
        if ii % 4 == 0:
            buffer = ll
        if ii % 4 == 2 and text == ll:
            if buffer not in lst:
                lst.append(buffer)
    for k in lst:
        if k in people:
            people.remove(k)
    return people

if __name__ == '__main__':
    class Choice():
        def __init__(self, desc, fn):
            self.desc, self.fn = desc, fn


    choices = list(map(Choice, ('Read Data Files', 'Display Statistics', 'Top 5 Most Tweeted Words',
                                'Top 5 Most Tweeted Users', 'Find Users who tweeted a word',
                                'Find All People who are friends of the above users',
                                'Delete Words which is mentioned',
                                'Delete Users who mentioned a word', 'Find Strongly Connected Components',
                                'Find Shortest Path from a given user'),
                       (read_file, statistic, mostword, mostuser, userfind, userfriend, delword, deluser, None, None)))

    while True:
        print(55 * '-')
        print("                      M E N U                      ")
        print(55 * '-')
        for i, c in enumerate(choices):
            print(i, ":", c.desc)
        print("99. Quit")
        print(55 * '-')

        # Get input
        choice = input('Select Menu : ')
        # Convert string to int type #

        if choice == '99':
            print("Good Bye")
            exit()
        elif not choice.isdecimal() or int(choice) > len(choices):  # default
            print("Invalid input. Try again...")
        else:
            choice = int(choice)
            print(choices[choice].fn())