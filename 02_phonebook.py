def main():
    names = open("./names.txt", "r")
    shared_first = {}
    shared_last = {}

    for line in names:
        temp = []
        temp = line.split()
        temp[0] = temp[0].title()
        temp[1] = temp[1].title()
        temp_first = shared_first.get(temp[0])
        temp_last = shared_last.get(temp[1])
        if temp_first != None:
            shared_first.update({temp[0]: [*temp_first, temp[1]]})
        else:
            shared_first[temp[0]] = [temp[1]]

        if temp_last != None:
            shared_last.update({temp[1]: [*temp_last, temp[0]]})
        else:
            shared_last[temp[1]] = [temp[0]]


    print("Shared First Names:")
    for key in shared_first:
        if len(shared_first[key]) > 1:
            print("{} ({}): {}".format(key, len(shared_first[key]), shared_first[key]))
    print()
    print("Shared Last Names:")
    for key in shared_last:
        if len(shared_last[key]) > 1:
            print("{} ({}): {}".format(key, len(shared_last[key]), shared_last[key]))
    names.close()
main()