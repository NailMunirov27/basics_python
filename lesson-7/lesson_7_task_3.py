from os import path, listdir, walk
import shutil

dir_name = "my_project1"

try:
    for root, dirs, files in walk(dir_name):
        if "templates" in dirs and root != dir_name:
            for entry in listdir(path.join(root, "templates")):
                shutil.copytree(path.join(root, "templates", entry), path.join(dir_name, "templates", entry))

except FileExistsError:
    print("!!!")