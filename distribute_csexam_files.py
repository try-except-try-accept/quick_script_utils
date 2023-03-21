

from os import listdir, mkdir, path, getcwd
from shutil import move, rmtree, copy
from datetime import datetime


stamp = datetime.now().strftime("%y.%m.%d")

backup_folder = f"csexam_backup_{stamp}"


try:
    mkdir(backup_folder)
except FileExistsError:
    pass
    

num = input("How many students? ")
valid = False
while not valid:
    if num.isdigit():
        num = int(num)
        if 1 <= num <= 30:
            valid = True
            continue

    print("Invalid - max 30")


file_folder = input("Enter folder name of files to distribute: ")
while not path.exists(getcwd()+"/"+file_folder):
    file_folder = input("Enter folder name of files to distribute: ")


for fnum in range(1, num+1):

    exam_folder = f"csexam{str(fnum).zfill(2)}"
    
    for file in listdir(file_folder):

        path = getcwd()+"/"+file_folder+"/"+file
        new_path = getcwd()+"/"+exam_folder+"/"+file
        copy(path, new_path)

    print("Copied files into", exam_folder)
        
            
            
