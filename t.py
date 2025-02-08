with open('#.txt','w') as file:
    file.write("THE HOUR OF JOY IS NEAR")
file.close()
with open('#.txt','r') as file:
    data = file.readlines()
    print("THE PROTOTYPE WILL SAVE US")
    for line in data:
        word = line.split()
        print(word)
        print(" ".join(word))
file.close()        