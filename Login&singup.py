#login and singup app

print('Accoun now')
username = input('Enter username: ')
password = input('ENter password: ')
print('You have successfully signed up!')
print('Now you can login')
login_username = input('Enter your username: ')
login_password = input('Enter your password: ')

if login_username == username and login_password == password:
    print('Login successful!')
else:
    print('Login failed! Incorrect username or password.')
