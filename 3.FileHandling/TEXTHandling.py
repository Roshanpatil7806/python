# ==========================================
# 1. Create and write to a text file
# ==========================================

with open("student.txt", "w") as file:
    file.write("Name: Roshan\n")
    file.write("Age: 22\n")
    file.write("Course: Python\n")
    file.write("Topic: File Handling\n")

print("File created and data written successfully!")


# ==========================================
# 2. Read the complete file
# ==========================================

with open("student.txt", "r") as file:
    data = file.read()

print("\nFile Content:")
print(data)


# ==========================================
# 3. Append data to the file
# ==========================================

with open("student.txt", "a") as file:
    file.write("Status: Learning Python\n")

print("Data appended successfully!")


# ==========================================
# 4. Read file line by line
# ==========================================

with open("student.txt", "r") as file:

    print("\nReading file line by line:")

    for line in file:
        print(line.strip())


# ==========================================
# 5. Count number of characters
# ==========================================

with open("student.txt", "r") as file:
    data = file.read()

print("\nNumber of characters:", len(data))