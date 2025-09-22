# Checks the Python version
python --version


git init

# Sets your global user name and email (run once)
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"


# ----- Git Core Workflow -----

# Stages a specific file for a commit
git add testing.py

# Stages all new and modified files in the current directory
git add .

# Checks the status of your working directory
git status

# Commits staged changes with a message
git commit -m "Your commit message"


# ----- Working with a Remote (GitHub) -----

# Links your local repo to a remote one
git remote add origin https://github.com/mounicahudgi/gitcheetsheet.git

# Lists the remote repositories for your project
git remote -v

# Pushes your local commits to GitHub for the first time
git push -u origin master

# Pushes future commits after the first time
git push
now pushing from github or editing or adding from github
