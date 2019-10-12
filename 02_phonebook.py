def main():
    names = open("./names.txt", "r")
    dictionary = {}

    for line in names:
        temp = []
        temp = line.split()
        dictionary[temp[0]] += temp[1]

main()