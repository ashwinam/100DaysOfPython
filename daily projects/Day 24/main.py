# traditional to open & write file, but here need to explicitly close the file.
file = open("C:\\Users\\A_MAN\\Desktop\\my_file.txt")
contents = file.read()
print(contents)
file.close()

# another way to open file
# read file
with open("C:\\Users\\A_MAN\\Desktop\\my_file.txt") as file:
    contents = file.read()
    print(contents)

# write file  (this mode remove everything and it newly write) and if file not exist it creates them.
with open("new_file.txt", mode="w") as file:
    file.write("Hello world")

# append in file (it dont remove previous)
with open("C:\\Users\\A_MAN\\Desktop\\my_file.txt", mode="a") as file:
    file.write("\nHello world.")
