import os

Cur_Wrk_dir = os.getcwd()   # Returns Current working directory

#list the files in the current directory
files= os.listdir('C:/Users/Nirmala/PycharmProjects/PyATB5xLearning')
print(f"Curret working files{files}")

#create new directory
# os.mkdir("Test2")

file_exist = os.path.exists("Gajen.txt")
print(file_exist)

print(os.name)  # Windows= NT