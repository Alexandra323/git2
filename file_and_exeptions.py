with open('input_data.txt') as file_object:
    print(file_object.read())

print("UUUUUUUUUUUUUUUUUUUUUUU")


print("Reading a txt file completed")

# for line in contents:
#     print(line)

filename = 'input_data.txt'
with open(filename, "a") as file_object:
    file_object.write("I love programming\n")

print("!!!!!!!!!!!!!!!!!")

# try:
#     print(with open('input_data.txt').read())
# except:
#     print("Doesn't work")

with open('input_data.txt') as file_object:
    for line in file_object:
        print(line)

with open(filename, 'a') as f:
    f.write("ttttttttttttttt\n")
    f.write("i am working\n")

print("####################")

