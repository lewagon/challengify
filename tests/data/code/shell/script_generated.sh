#!/bin/zsh

cd $GITHUB_WORKSPACE

echo "\nretrieve commits 😊:\n"

# retrieve the list of files impacted by the commits of the pr
files=$(git diff --name-only --diff-filter AM "origin/master")

echo $files

echo "\nlook for first ancestor directory with a Makefile and without a Makefile_ignore 😊:\n"

results=()



if [[ "$results" == "" ]]; then

    echo "\nno tests to run 👌\n"

else

    # YOUR CODE HERE

fi
