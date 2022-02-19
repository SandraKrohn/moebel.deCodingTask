def nameSum(name):
    nameSum = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
               'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
               'x': 24, 'y': 25, 'z': 26}
    sum = 0
    index = 0

    while type(name) is str and index < len(name):
        if name.lower()[index] in nameSum:
            sum += nameSum[name.lower()[index]]
        index += 1
    return sum

inputString = input("Enter a name: ")

print(nameSum(inputString))