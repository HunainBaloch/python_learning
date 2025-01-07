# # Writing a file

s = "Hunain is a good boy"

with open("test.txt", "w") as f:
    f.write(s)

# Reading a file

with open("test.txt", "r") as f:
    s = f.read()
    print(s)