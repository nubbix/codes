#This program takes an input from the user and writes it to a file
#Made by Tom Knudsen - post@tknudsen.com

tekst = input('Skriv noe inn her: ')
file = open('C:/test/a.txt', 'w') #For this to work you need to create folder and file C:/test/a.txt
file.write(tekst)
file.close()
