storeage = {
    "rishi" : 1234567890 ,
    "papa" : 9876543210,

}

def add_contact():
    name = input('enetr name of the contect :- ')
    if name in storeage:
        print('contect all ready exist')
    else:
        number = int(input('enter the number :- '))
        storeage.update({name : number})
    print(storeage)

def search_contact():
    name = input('enetr name of the contect :- ') 
    if name in storeage:
        print(storeage.get(name))
    else:
        print('contect is not present')

def delete_contact():
    name = input('enetr name of the contect :- ')
    if name in storeage:
        storeage.pop(name)
        print(storeage)
    else:    
        print('contect is not present')

def show_all():
    print(storeage)

while True:
    print('press 1 for add contect')
    print('press 2 for search contect')    
    print('press 3 for delete contect')    
    print('press 4 for show all contect')    
    print('press 5 exit')       
    option = int(input('enter you option :- ')) 

    if option == 1:
        add_contact()
    elif option == 2:
        search_contact()  
    elif option == 3:
        delete_contact()
    elif option == 4:
        show_all()
    elif option == 5:
        break    
    else:
        print('ERROR : INVALID CHOICE')