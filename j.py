var =int(input("Enter the number of rows"))
for i in range(1, var+1):
     for j in range(i):
         print('*', end='')
     print()