from os import listdir, getcwd, path
from shutil import move
from re import search

r = getcwd()

remove_file = "T2 Spreadsheet Assessment"

for folder in listdir():
    if path.isdir(folder):
        for fn in listdir(folder):
            if remove_file in fn:               
    
                move(getcwd()+"/"+folder+"/"+fn, getcwd()+"/"+fn)
