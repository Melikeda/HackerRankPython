if __name__ == '__main__':
    N = int(input())
    
    mylist = []

for _ in range(N):
    command_line = input()        # Komutu satır satır oku
    parts = command_line.split()  # Komutu ve parametreleri ayır

    command = parts[0]            # Komut adı

    if command == "insert":
        i = int(parts[1])
        e = int(parts[2])
        mylist.insert(i, e)

    elif command == "print":
        print(mylist)

    elif command == "remove":
        e = int(parts[1])
        mylist.remove(e)

    elif command == "append":
        e = int(parts[1])
        mylist.append(e)

    elif command == "sort":
        mylist.sort()

    elif command == "pop":
        mylist.pop()

    elif command == "reverse":
        mylist.reverse()
