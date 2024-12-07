file_name="Gajendran1.txt"
content="New file opened"

with open(file_name,'w') as file:
    file.write(content)

with open(file_name,'r') as file:
    content1 = file.read()
    print(content1)