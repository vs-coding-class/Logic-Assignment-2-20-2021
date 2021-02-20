fileName = input('''Please input a file name...
''')

k = 0

for i in fileName:
    k += 1
    if i == '.':
        print(fileName[k:])
