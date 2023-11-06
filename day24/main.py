path = '../../OneDrive/Desktop/my_file.txt'
with open(path) as file:
    contents = file.read()
    print(contents)
# with open("my_file.txt", mode= "a") as file:
#     file.write("/nNew text.")