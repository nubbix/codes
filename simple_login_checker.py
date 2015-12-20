## Very basic login and password checker
## By Tom Knudsen post@tknudsen.com


#variables in plain text
username = 'test'
password = 'lamepassword'

#This takes an input from the user
userName = input(str('Please enter your username: '))
userPassword = input(str('Please enter your password: '))

#statement to check if username and password is set
if (userName == 'test') and (userPassword == 'lamepassword'):
    print('Login successful')
else:
    print('Login failed')
