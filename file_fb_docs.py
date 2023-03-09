from os import listdir, getcwd
from shutil import move
from re import search

r = getcwd()

for fn in listdir():
    if fn.endswith("gsheet"):
        z = search("z\d{5}", fn).group()
        for fold in listdir():
            if not fold.endswith("gsheet") and z in fold:
                move(getcwd()+"/"+fn, getcwd()+"/"+fold+"/"+fn)
