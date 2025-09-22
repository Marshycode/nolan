# File: homework2.py

# Your file path should look like:
# python_decal_fa25/yourname/homework2/homework2.py

# Questions (Answer these in the homework2.py file as comments):

# 1) What’s the difference between Git, GitHub, and Git Bash?
# Git is a command line tool that runs on a local machine while Git Hub is a storage space for code on the cloud.Git bash is the windows version.
# 2) What’s the difference between the terminal and the command line?
# The terminal is the actual location on your computer to give it commands. The commands are given through the command line, where you call them. (such as calling ls)
# 3) How does Windows PowerShell differ from Git Bash?
# They originate from different ecosystems. 
# 4) What’s the difference between Anaconda, conda, and Python?
#Anaconda is a specific type of python and conda is the envinronment mangement system ans poackage. 
# 5) What is VS Code? 
#Vs code is a coding studio to produce python scripts and interface with python. 
# 6) What is a Jupyter Notebook? How is it different from Jupyter Lab?
# A coding platform that combines differnet tools for programmers. Jupyter lab is web based. 
# 7) What does ~/ mean?
#It is the home directory which everything originates from on your computer. 
# 8) What’s the difference between an absolute path and a relative path?
# Absolute path gives all file steps while relative gives a few steps and shows .. to signify more steps. 
# 9) Imagine you're in your "yourname" repo. Write the absolute and relative paths to "course_assignments/homework2".
# yourname/course_assignments/homework2/homework2.py vs ../../homework2/homework2.py
# 10) What command lets you move from "course_assignments/homework2/" to "course_assignments/"?
# cd ..
# 11) What would rm ./ do in your current directory? (Don’t try it!)
# It would delete it
# 12) What do the following commands do?
# git add It adds a file to the git work tree
# git commit it saves local changes
# git push it sends local changes to the cloud on github 

# 13) What's the difference between "git add ." and "git add <file>"?
# Git add . saves everything and the <file> version only saves the save data in the named file. 
# 14) What do "git status" and "git log -1" do?
# Git status shows worktree status and git  log -1 shows worktree history
# 15) What’s the difference between cloning a repository and pulling from it?
# Cloning makes an full copy of a remote repositorywhile pulling makes changes to a prexisting local repository from a remote one.
# 16) What has been your most frustrating bug or error in this class so far? How did you troubleshoot or fix it?
# having issues with text editors but as I became more familiar it was esier to understand how to use them. 
# 17) What’s a question you still have? What’s something you’re confused about?
# Can all of the actions made by commands in the terminal also be completed in the regular finder window?
# 18) Tell me a fun fact!
# I have a baby yoda stuffy on my desk and its super cute. 
# 19) Print your favorite math expression you've learned in Python so far. 
# (Hint: Use print() and add a comment explaining what it does.)
def drinkingage(a):
    if a>=21:
        print("Is of legal drinking age.")
    else:
        print("Is not of legal drinking age.")
a=21
drinkingage(a)
#This math problem is super cool because it determines if a number (a) is greater than or equal to 21 and that information can be used to determine drinking legality. 
