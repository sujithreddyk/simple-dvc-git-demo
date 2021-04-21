```bash
conda create -n winequality python=3.7 -y
```
```bash
conda activate winequality
```

** Create requirements.txt file 
	1) dvc
	2) dvc[gdrive]
	3) sklearn
```bash
 pip install -r requirements.txt
```

** Create README.md file
** Create template.py file
	--> Here in this python file, i wrote a code for creating project structure manually.

** Create a folder/directory named "data_given"
	--> Used for keeping winequality data.

```bash
git init	// All files to green means untracked	(Symbol 'U')
```
```bash
dvc init	// .dvcignore got created
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .	// adding the current working directory data to git  (Symbol 'A')
```
```bash
 git commit -m "first commit"	// All 'A' symbols for files are gone.
```
```bash
git add . && git commit -m "update README.md changes to git"
```
Till now we had made changes in local git

Now we will made changes in remote git

```bash
git remote add origin https://github.com/sujithreddyk/simple-dvc-git-demo.git
```
```bash
git branch -M main
```
```bash
git push -u origin main
```
tox command - 
```bash
tox
```
for re-build - 
```bash
tox -r
```
pytest command - 
```bash
pytest -V
```

setup commands - 
```bash
pip install -e .
```
Building own package commands-
```bash
python setup.py sdist bdist_wheel
```