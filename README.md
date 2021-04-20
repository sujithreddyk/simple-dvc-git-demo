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
