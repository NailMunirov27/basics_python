import os

dir2 = ["settings", "mainapp", "adminapp", "authapp"]
for name in dir2:
    dir_name = os.path.join("my_project", name)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
