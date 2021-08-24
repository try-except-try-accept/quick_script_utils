


from os import listdir, getcwd, path

from shutil import move


for fn in listdir():


     if fn.endswith(".md"):

          file_code = fn[:10].replace(",", "")

          for folder_name in listdir():
               if path.isdir(folder_name) and folder_name.startswith(file_code):
                    break
          else:
               print(f"Folder not found for {fn}")
               continue


          move(getcwd()+"/"+fn, getcwd()+"/"+folder_name+"/"+fn)
          print(f"Moved {fn} to {folder_name}")
