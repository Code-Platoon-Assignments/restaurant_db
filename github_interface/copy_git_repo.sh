#!/bin/bash
# copyrepos
# ---------------
# Clone a repo from one gh organization into another organization --
# the new repo will have the same name.
# Git commit history is preserved.
# Intended to help us easily copy assignment repos from one org to another,
# as we currently create a new gh org for each platoon/cohort.
#
# See source of this code - https://github.com/eleniums/copy-git-repo - for README with details

# Requirements
# --------------
# - github cli tool.
#	- See https://cli.github.com/ for docs & install instructions.
#	- You must have this installed.
#	- You must then run `gh authenticate login` have the gh cli tool authenticate against and log
#	  into your github account so it has the necessary permission to do stuff.
# - git, obviously.

# Examples
# -------------
# Copy the guessing-game repo from romeoplatoon org to sierraplatoon org:
# ./copyrepos.sh romeoplatoon sierraplatoon oop-guessing-game

# See https://stackoverflow.com/questions/36273665/what-does-set-x-do
[ "$DEBUG" == 'true' ] && set -x

# See https://towardsdev.com/what-does-set-u-mean-in-a-bash-script-52b048271741
set -u

source_org=$1
target_org=$2
repo_name=$3

source_url="https://github.com/$source_org/$repo_name"
target_url="https://github.com/$target_org/$repo_name"

# TODO: Allow public/private/internal to be set as a command line flag

# Create empty repo in target org
gh repo create $target_org/$repo_name --private

# this is the name of the temporary directory to use
temp_dir=copyrepo-temp

# create a copy of the source repository
git clone --bare $source_url $temp_dir

# push the copy to the destination repository
cd $temp_dir
git push --mirror $target_url

# remove the temporary directory
cd ..
rm -rf $temp_dir