

from os import listdir, mkdir, path, getcwd
from shutil import move, rmtree
from datetime import datetime


stamp = datetime.now().strftime("%y.%m.%d")

backup_folder = f"csexam_backup_{stamp}"


try:
    mkdir(backup_folder)
except FileExistsError:
    pass
    


for fnum in range(1, 31):

    exam_folder = f"csexam{str(fnum).zfill(2)}"
    exam_folder_backup_path = "/".join((getcwd(), backup_folder, exam_folder))

    try:
        mkdir(exam_folder_backup_path)
    except FileExistsError:
        pass

    for child in listdir(exam_folder):

        this_path = "/".join((getcwd(), exam_folder, child))
        if path.isdir(this_path):
            rmtree(this_path)
            print(f"Deleted folder at {this_path}")
        else:
            try:
                move(this_path, exam_folder_backup_path+f"/{child}")
                print(f"Relocated file at {this_path}")
            except PermissionError:
                pass
            
            
