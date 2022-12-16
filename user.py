##########################################################################
##              Library Management System using python File             ##
#                      By Pralay Mondal                                 ##
##                       USER MODULE                                    ##  
##########################################################################
import os
from datetime import date
def _callUser():
    print()
    print('\t\t\t Library Management System')
    print('\t\t\t Welcome User')
    print('\t\t\t -----------------------------------')
    print('\t\t\t 1: SHOW BOOKS')
    print('\t\t\t 2: BORROW BOOK')
    print('\t\t\t 3: RETURN BOOK')
    print('\t\t\t 0: TO EXIT')
    print('\t\t\t -----------------------------------')
    print()
    try:
        _choice = int(input('\t\t\tEnter your choice:'))
        if _choice == 1:
            _showBooks()
        elif _choice == 2:
            _borrowBook()
        elif _choice == 3:
            _returnBook()
        else:          
            print('\t\t\t THANKS FOR USING OUR LIBRARY MANAGEMENT SYSTEM') 
    except ValueError:
        print('\t\t\tPlease enter a valid choice')
        
        

##function for showing all book available in book.txt file
def _showBooks():
    _filename = 'book.txt'
    try:
        with open(_filename, "r") as _fName:
            _data = _fName.readlines()
            for _ln in _data:
                print('\t\t\t'+_ln)
                print('\t\t\t-------------------------------')
        print('\t\t\t---------------------------------------')        
        _callUser()
    except FileNotFoundError:
        print('\t\t\t File Name ' +_filename + ' Does not exits')

## function for borrowed Book        
def _borrowBook():
    _fileBook = 'book.txt'
    _fileBorrow = 'borrwed.txt'
    _flag = 0
    _bookId = input('\t\t\tEnter the Book Id To Borrow')
    _datalist = [] 
    try:
        with open(_fileBorrow, 'r') as _fborrow:
            for i in _fborrow:
                _dataBorr = i.split('\t')
                if _bookId in _dataBorr[0]:
                    print('\t\t\t Book Id ' + _bookId + ' Is already borrowed')
                    _flag = 1
                    break 
        if _flag == 0:
            try:
                print('\t\t\t Book Details')
                with open(_fileBook) as _fbook:
                    for _fb in _fbook:
                        print('\t\t\t ' +_fb)
                print('\t\t\t --------------------------------')    
                try:
                    with open(_fileBorrow, 'a') as _fbow:
                        _name = input('\t\t\t Enter Name:')
                        _date = date.today()
                        _dateStr = date.isoformat(_date)
                        _fbow.write('%s \t %s \t %s\n' %(_bookId,_name,_dateStr))
                    _callUser()    
                except FileNotFoundError:
                    print('File Name '+ _fileBorrow +' is not found')            
            except FileNotFoundError:
                print('\t\t\t file Name '+ _fileBook + ' is not found')
        else:
            _callUser()                    
    except FileNotFoundError:
        print('File name ' + _fileBorrow + ' is not found')                

## function for return Book 
def _returnBook():
    _fileTemp = 'temp.txt'
    _fileBorrow = 'borrwed.txt'
    _bookId = input('\t\t\t Enter Book Id:')
    _name = input('\t\t\t Enter Your Name:')
    _dataList = []
    try:
        with open(_fileBorrow, 'r') as _fborrow:
            for _fbInfo in _fborrow:
                _idList = _fbInfo.split('\t') 
                if _bookId not in _idList[0]:
                    _dataList.append(_fbInfo)
        ##print(_dataList)
        n_names = ["{}\t".format(i) for i in _dataList]
        try:
            with open(_fileTemp, 'a') as _ftmp:
                _ftmp.writelines(n_names)
            print('\t\t\t Thank You ' + _name + ' Have A Nice Day !!!')    
            os.replace(_fileTemp,_fileBorrow)    
            _callUser()
        except FileNotFoundError:
            print('File Name ' + _fileTemp + ' is not found')        
    except FileNotFoundError:
        print('File Name ' + _fileBorrow + ' is not found')            