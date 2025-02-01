file=open('#.txt')
print(file.read())
file.close()
file_write=open('#.txt','w')
file_write.write("WELCOME TO.....")
file_write.write("SAFE HAVEN")
file_write.close()
file_write=open('#.txt','a')
file_write.write("WELCOME TO.....")
file_write.write("SAFE HAVEN")
file_write.close()
file=open("#.txt","r")
counter=0
content=file.read()
coList= content.split("\n")
for i in coList:
   if i:
       counter +=1 
     
print("This is the number of lines in the file")
print(counter)