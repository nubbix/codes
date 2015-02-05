#!/bin/bash

#Script to verify and remove files based on permission value
#by Tom Knudsen aka nubbix

#This clears the screen
clear
#This sets the folder
folder=/tmp

#This is a fore lopp to check the folder and see if the file has #the right permission, one by one and delete those that are #fales.

for file in ${folder}/*
do
perm=$(ls -l "$file" | cut -d ' ' -f 1)


if [ "$perm" = "-rwxr-xr-x" ]
then echo "The file $file has the correct permissions"
else rm -v "$file"

fi
#This endes the loop
done

sleep 1

clear

exit 0
