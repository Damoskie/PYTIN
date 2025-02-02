# Opening the file in 'read' mode and reading the entire content
with open('@.txt', 'r') as file:
    content = file.read()
    print(content)
# Opening the file and reading it line by line
with open('@.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')  # `end=''` is to avoid adding extra newline
        line = file.readline()
# Opening the file and reading all lines into a list
with open('@.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end='')
# Opening the file and iterating through each line
with open('@.txt', 'r') as file:
    for line in file:
        print(line, end='')
