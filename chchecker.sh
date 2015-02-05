#!/bin/bash
#Script to set permission to a specific folder
#Made by Tom Knudsen aka nubbix

#Clears the screen 
clear

#Ask the user to input a PATH to a specific folder
read -p "Enter folder permission path : " DIRECTORY

#Ask the user to input a new chmod number
read -p "Enter new permission number : " PERMISSION

#Changes the specific folders permission based on the previous input
chmod -R "$PERMISSION" "$DIRECTORY"

#Ends the scipt
exit 0
