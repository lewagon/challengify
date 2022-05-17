#!/bin/zsh

cd $GITHUB_WORKSPACE

echo "\nretrieve commits 😊:\n"

# retrieve the list of files impacted by the commits of the pr
files=$(git diff --name-only --diff-filter AM "origin/master")

echo $files

echo "\nlook for first ancestor directory with a Makefile and without a Makefile_ignore 😊:\n"

results=()

# $DELETE_BEGIN
# iterate through files line by line
echo $files | while read line; do

  # retrive file parent directory
  file_parent=$line

  # look for the first Makefile in a parent directory without a Makefile_ignore file
  while [[ (! -e "$file_parent/Makefile") || (-e "$file_parent/Makefile_ignore") ]]; do

    # retrieve parent directory
    file_parent=${file_parent%/*}

    # stop looking
    if [[ ("$file_parent" == "" ) || ($file_parent != *"/"*) ]]; then
      break;
    fi

  done

  # add challenge to the list of tests to run
  if [[ (-e "$file_parent/Makefile") && (! -e "$file_parent/Makefile_ignore") ]]; then
    echo "Tests found in '${file_parent}' 🦾 for '${line}' 👍"
    results=( "${results[@]}""${file_parent}\n" )
  else
    echo "No tests found in path '${line}' ❌"
  fi

done
# $DELETE_END

if [[ "$results" == "" ]]; then

    echo "\nno tests to run 👌\n"

else

    # $CHALLENGIFY_BEGIN
    echo "\ndeduplicate challenges 🔎:\n"

    # deduplicate tests
    deduplicated_challenges=$(echo $results |  awk '!a[$0]++')

    echo $deduplicated_challenges

    echo "\nrun tests 🤖:\n"

    # exit on error
    set -eux

    # iterate through challenges
    echo $deduplicated_challenges | while read challenge; do

      # run tests
      make -C "$challenge";

    done
    # $CHALLENGIFY_END

fi
