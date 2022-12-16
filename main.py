##########################################################################
##              Library Management System using python File             ##
#                      By Pralay Mondal                                 ##
##                       MAIN MODULE                                    ##  
##########################################################################
## IMPORT ADMIN MODULE
import admin
import user
def start():
    print('\t\t\t Library Management System')
    print('\t\t\t -------------------------')
    print()
    print('\t\t\t 1: Admin')
    print('\t\t\t 2: User')
    print('\t\t\t 0: To Exit')
    print('\t\t\t -------------------------')
    print()
    try:
        _choice = int(input('\t\t\tEnter Your Choice:'))
        if _choice == 1:
            admin._callAdmin()
        elif _choice == 2:
            user._callUser()  
        else:
            print('\t\t\t THNAK YOU FOR USING OUR LIBRARY MANAGEMET SYSTEM')        
    except ValueError:
        print('\t\t\tPlease Choose a valid options')
    
start()    