#!/bin/bash

#This is a program to get input and show output
#Made by Tom Knudsen aka nubbix

clear

#This asks the user for a name
echo "Hi there, please enter your first name followed by [Enter]" 

#This reads the users input and stores it in a variable
read name || $name

#This asks the users for a date of birth
echo "Thank you sir, now please enter your date of birth (4 digits) follow by [Enter]"

#This reads the users input and stores it in a variable
read date || $date

#This gives the user an message
echo "Thank you sir, stand by....."

#This inputs a short delay
sleep 10

#This concatinates the two variable and reads it back to the user.
echo "Your name is" $name "and your date of birth is" $date

#Ends the script
exit
fi
