from pathlib import Path

print('--------WELCOME TO TASK MANAGER APP--------')

def add_task():
    add_task = input('ENTER YOUR TASK YOU WANT TO ADD :- ')
    p = Path('task.txt')
    with open ('task.txt' , 'a') as f:
        f.write(add_task + '\n')
        print('TASK ADDED SUCCESSFULLY......')

def view_task():
    with open ('task.txt' , 'r') as f:
        print(f.read())

def delete_task():
    task = input('ENTER THE TASK YOU WANT TO DELETE :- ')
    with open ('task.txt' , 'r') as f:
        lines = f.readlines()

    with open ('task.txt' , 'w')  as f:
        for i in lines:
            if i.strip().lower() != task.lower():
                f.write(i)  
                
def update_task():
    task = input('ENTER THE TASK YOU WANT TO UPDATE :- ')

    with open ('task.txt' , 'r') as f :
        lines = f.readlines()

    with open ('task.txt' , 'w') as f:
        for i in lines:
            if i.strip().lower() == task.lower():
                contant = input('ENTER YOUR CONTANT :- ')
                f.write(contant + '\n')
                print('TASK UPDATED SUCCESSFULLY.......')
            else:
                f.write(i)    
                
while True:
    print('PRESS 1 FOR ADD TASK')
    print('PRESS 2 FOR DELETE TASK')
    print('PRESS 3 FOR UPDATE TASK')
    print('PRESS 4 FOR VIEW TASK')
    print('PRESS 0 FOR EXIT APP')
    option = int(input('ENTER YOUR OPTION :- '))   

    if option == 1:
        add_task()
    elif option == 2:
        delete_task()
    elif option == 3:
        update_task()
    elif option == 4:
        view_task()
    elif option == 0:
        break
    else:
        print('ERROR : INVALID CHOICE')                         
                