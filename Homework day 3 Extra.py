users = {
    'user_name': '0123456',
    'user_name2': '123',
    'Yousioph': '456'
}

if True:
    entered_user_name = input("Please enter the user name:")
    entered_password = input("please enter your password:")
    if entered_user_name in users.keys() and entered_password == users[entered_user_name]:
        print('login Successful,you will be shortly redirected to your account page')
    else:
        print('login fail,please try again\nif you cannot remember you should choose forget password below')
