#!/usr/bin/env python3.6
from user import User
from credetials import Credentials


def main():
    while True:
        print('Welcome to password locker \n Default username: Brian, \n Default Password: 1234')
        print('Short code : nu = new user, lg = login, ex = exit')
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('Create new username:..')
            created_user_name = input()

            print('Create new password')
            created_password = input()

            print('Confirm password')
            confirm_password = input()

            while confirm_password != created_password:
                print('Password didnot match!!')
                print('Enter password')
                created_password = input()
                print('Confirm password')
                confirm_password = input()

            else:
                print('------------------------------------')
                print(f'Congratulations {created_user_name}, account created Successful.\n')
                print('Procceed to login')
                print('Username')
                entered_user_name = input()
                print('Your password')
                enterd_password = input()

            while entered_user_name != created_user_name or enterd_password != created_password:
                print('Invalid username or password!!')
                print('Username')
                entered_user_name = input()
                print('Your password')
                enterd_password = input()
            
            else:
                print(f'welcome : {entered_user_name} to your account \n')
                print('**********************************************')
                print('login successful. \n')
                print('Do you want to view or add new Data? (vw / ad) \n')
                
                key_word = input().lower()
                if key_word == 'ad':
                    print('Add in your credentials to save them.\n Your inputs will be saved on the last line..')
                    f = open("user.txt", "a")
                    f.write(input('\n Your account name : \n') + ', ' + input('Your username: \n')+ ', ' + input('Your account password: \n') + '\n')
                    f.close()
                    
                    print('*****-----------------******* \n YOUR CREDENTIALS.')
                    f = open("user.txt", "r")
                    print(f.read())
                    print('*************************')
                    break
                else:
                    print('*****-----------------******* \n YOUR CREDENTIALS.')
                    f = open("user.txt", "r")
                    print(f.read())
                    print('*************************')
                    break

        elif short_code == 'lg':
            print('Welcome \n Enter username: ')
            default_user_name = input()

            print('password: ')
            default_user_password = input()
            print('\n')

            while default_user_name != 'Brian' or default_user_password !='1234':
                print('Invalid username or password')
                print('Enter username: ')
                default_user_name = input()

                print('password: ')
                default_user_password = input()
                print('\n')

            else:
                print('login successful. \n -------------------------')
                print('Do you want to view or add new Data? (vw / ad) \n')
                
                key_word = input().lower()
                if key_word == 'ad':
                    print('Add in your credentials to save them.\n Your inputs will be saved on the last line..')
                    f = open("user.txt", "a")
                    f.write(input('\n Your account name : \n') + ', ' + input('Your username: \n')+ ', ' + input('Your account password: \n') + '\n')
                    f.close()
                    
                    print('*****-----------------******* \n YOUR CREDENTIALS.')
                    f = open("user.txt", "r")
                    print(f.read())
                    print('*************************')
                    break
                else:
                    print('*****-----------------******* \n YOUR CREDENTIALS.')
                    f = open("user.txt", "r")
                    print(f.read())
                    print('*************************')
                    break
        
        elif short_code == 'ex':
            print('Cancelled. Bye..')
            print('******************************************')
            break

        else:
            print('---------------------------------------------')
            print('Enter valid short code to continue.')
            print('---------------------------------------------')
if __name__ == '__main__':
    main()