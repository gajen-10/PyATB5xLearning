# write s program to take a user age and
# let him knw if he can go to the club or not. Age criteria 21

# Logic Building formula

# Step 1
# User input i/p -> data type -> int
# o/p -> String -> user if he can go or not

# Step 2. Rough logic (brute force)
# age > 21 -> print can go
# age < 21 -> print can't go

# step 3. write the logic
age = int(input("Enter the age:\n"))

if age >= 21:
    print("You can go to the club")
else:
    print("You cannot go to the club")

# Step4. check for edge case
# we should consider edge cases such as:
# Negative ages or exteremely high values -> program will break
# Non-numeric input - ABC
# Age which is valid. >130

# Step5. Optimize the code.
# Handle all the edges.
