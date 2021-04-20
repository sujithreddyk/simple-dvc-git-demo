## This process of creating template for project structure can be done automatically with Cookiecutter
import os

dirs = [
os.path.join("data","raw"),
os.path.join("data","processed"),
"notebooks",
"saved_models",
"src"
]

for dir_ in dirs:
    os.makedirs(dir_,exist_ok=True)                   # Creating directories,and ignoring the creation of directories if already exist.
    with open(os.path.join(dir_,".gitkeep"), "w") as f:    # To initialize git with empty folders we have to keep .gitkeep empty file
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",    # In .gitignore file will keep information like which files don't need to push into git repo
    os.path.join("src","__init__.py")
]

for file_ in files:
    with open(file_, "w") as f:
        pass