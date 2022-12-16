############################################################
##           Code Written By Pralay Mondal                ##
##                     ADMIN MODULE                       ##
############################################################
    
def _callAdmin():
    print('\t\t\t Library Management System')
    print('\t\t\t Welcome Admin')
    print('\t\t\t -------------')
    print('\t\t\t 1: ADD NEW BOOK')
    print('\t\t\t 2: SHOW ALL BOOK')
    print('\t\t\t 3: SHOW BRROWED BOOK INFORMATION')
    print('\t\t\t 0: TO EXIT')
    print()
    try:
        _choice = int(input('Enter your choice:'))
        if _choice == 1:
            _addNewBook()
        elif _choice == 2:
            _showAllBook()
        elif _choice == 3:
            _showBorrowInfo()
        else:          
            print('\t\t\t THANKS FOR USING OUR LIBRARY MANAGEMENT SYSTEM') 
    except ValueError:
        print('\t\t\t Please enter a valid choice')        

## function for adding new book information 
def _addNewBook():
    ## book.txt is the book file which store book details
    _filename = 'book.txt'
    _add = 'Y'
    try:
        with open(_filename, "a") as _fname:
            while _add == 'Y':
                _bookId = int(input('Enter Book Id :'))        
                _bookName = input('Enter Book Name :')
                _fname.write("%d \t %s \n" %(_bookId, _bookName))
                _add = input('\t\t\tAdd Another Records :').upper()       
        _callAdmin()         
    except FileNotFoundError:
        print("\t\t\tSorry, The File "+ _filename +"does not exits")
        
## function for showing all book available in book.txt file
def _showAllBook():
    _filename = 'book.txt'
    try:
        with open(_filename, "r") as _fName:
            _data = _fName.readlines()
            for _ln in _data:
                print('\t\t\t'+_ln)
                print('\t\t\t-------------------------------')
        print('\t\t\t---------------------------------------') 
        _callAdmin()       
    except FileNotFoundError:
        print('\t\t\tFile Name ' +_filename + ' Does not exits')
         
            
##function for showing borrowed book information 
def _showBorrowInfo():
    _fileName = 'borrwed.txt'
    try:
        print('---------------------------------------')
        with open(_fileName, "r") as _fName:
            _data = _fName.readlines()
            for _ln in _data:
                print('\t\t\t' + _ln)
                print('\t\t\t-------------------------------')
        _callAdmin()       
    except FileNotFoundError:
        print('\t\t\tFile Name ' +_fileName + ' Does not exits')               