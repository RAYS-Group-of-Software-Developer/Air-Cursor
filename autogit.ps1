# get the first line as the commit message
$commitMessage = Read-Host "Enter the commit message"

# make sure that the commit message is not empty
if ($commitMessage -eq "") {
    Write-Host "Commit message cannot be empty"
    exit
}


# add all files to the staging area
# ask user which files to add
$answer = Read-Host "Add all files? (y/n)"
# if the answer is yes, add all files
if ($answer -eq "y") {
    git add .
}
# if the answer is no, ask which files to add
else {
    $files = Read-Host "Enter the files to add (separated by spaces)"
    git add $files
}


# confirm that the files have been added
git status


# ask if the commit message is correct
Write-Host "Commit message is: $commitMessage"
$answer = Read-Host "Is this correct? (y/n)"

# if the answer is not yes, exit the script
if ($answer -ne "y") {
    exit
}

# commit the staged files with the commit message
git commit -m $commitMessage

# confirm that the files have been committed
git status

# ask if the commit should be pushed to the remote repository
$answer = Read-Host "Push to remote repository? (y/n)"

# if the answer is not yes, exit the script
if ($answer -ne "y") {
    exit
}

# push the changes to the remote repository
# provide the list of branches and ask which branch to push to or create a new branch
# allow user to navigate between branches useing the arrow keys
# allow user to create and push a new branch

# get the list of branches
$branches = git branch

# ask the user which branch to push to
$branch = Read-Host "Enter the branch to push to"

# if the branch does not exist, ask if it should be created
if ($branches -notcontains $branch) {
    $answer = Read-Host "Branch $branch does not exist. Create it? (y/n)"
    if ($answer -eq "y") {
        git checkout -b $branch
    }
    else {
        exit
    }
}




git push -u origin main

# confirm that the files have been pushed
git status

# pause the script so that you can see the output
Read-Host -Prompt "Press Enter to exit"
