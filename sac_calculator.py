#SAC Rate Calculator
#This program will calculate your air consumption rate for scuba diving
#Made by Tom Knudsen - post@tknudsen.com
#License is open source


startBar = int(input('Please enter your start pressure: ')) #starting pressure with full cooled tank
endBar = int(input('Please enter your end pressure: ')) #ending pressure with cooled tank
depth = int(input('Please enter your average depth in numbers: ')) #This is your average depth, not your maximum
divetime = int(input('Please enter you dive time in numbers: ')) #This is your total dive time
print('Please wait, doing the calculation now!') 
sacrate = int(startBar - endBar * 10) / depth +10 + divetime #This calculates using a SAC forumula for air consumption in metric use
print("Your air consumption is: ",  sacrate, "bar per minute")
