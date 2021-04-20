-->conda create -n winequality python=3.7 -y
-->conda activate winequality

** Create requirements.txt file 
	1) dvc
	2) dvc[gdrive]
	3) sklearn
--> pip install -r requirements.txt

** Create README.md file
** Create template.py file
	--> Here in this python file, i wrote a code for creating project structure manually.

** Create a folder/directory named "data_given"
	--> Used for keeping winequality data.

--> git init	// All files to green means untracked	(Symbol 'U')

--> dvc init	// .dvcignore got created

--> dvc add data_given/winequality.csv

--> git add .	// adding the current working directory data to git  (Symbol 'A')

--> git commit -m "first commit"	// All 'A' symbols for files are gone.

--> git add . && git commit -m "update README.md changes to git"

Till now we had made changes in local git

Now we will made changes in remote git

--> git remote add origin https://github.com/sujithreddyk/simple-dvc-git-demo.git

--> git branch -M main

--> git push -u origin main

