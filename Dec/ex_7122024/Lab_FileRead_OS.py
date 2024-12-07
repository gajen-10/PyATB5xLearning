import os

try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path + "\example.txt"
    print(full_path_file)

    #Read the file
    file = open(full_path_file)

except Exception as fnfe:
    print("File Not found, fix the path or create a file")

finally:
    print("This code will be executed anyhow")
