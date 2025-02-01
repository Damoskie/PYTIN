# Open file for reading
file = open("example.txt", "r")
print("Reading content:")
print(file.read())  # Read all content
file.close()

# Open file for writing
file = open("example.txt", "w")
file.write("This is a new file created for demonstration.")
file.close()

# Open file for appending
file = open("example.txt", "a")
file.write("\nThis content is appended.")
file.close()

# Open file for reading and writing
file = open("example.txt", "r+")
print("Reading and updating content:")
content = file.read()
print(content)
file.write("\nAdded after reading.")
file.close()
