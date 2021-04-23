

from shutil import copy
from os import listdir, getcwd
from random import choice

for class_folder in listdir():

     if class_folder[0] == '9':
          for stu_folder in listdir(class_folder+"/"):
               orig = choice(listdir('random_db/'))
               path = getcwd()+"/"+class_folder+"/"+stu_folder+"/"
               d = stu_folder.split(" ")
               nick, roll, class_ = d[0], [i for i in d if i[0]=="["][0], [i for i in d if i[0]=="9"][0]
               copy(getcwd()+"/random_db/"+orig, path+"Users - {} [{}] {}.db".format(nick, roll, class_))
