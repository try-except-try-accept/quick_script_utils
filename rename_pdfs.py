from os import listdir, rename, getcwd

rem = input("Text to remove: ")

add = input("Text to append: ")

path = input("Enter path: ") + "/"

x = [rename(path+fn, path+fn.replace(rem, "").replace(".pdf", add+".pdf")) for fn in listdir(path) if fn.endswith(".pdf")]

input(f"{x.count(None)} pdfs renamed")
