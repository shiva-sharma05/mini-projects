from datetime import date

today = date.today()

print('-----------WELCOME TO AGE CALCULATOR------------')

birth_year  = int(input('ENTER YOUR YEAR OF BIRTH :- '))
if birth_year > today.year:
    print("ERROR : INVALID YEAR")
    exit()

birth_month = int(input('ENTER YOUR MONTH OF BIRTH :- '))
if birth_month < 1 or birth_month > 12:
    print("ERROR : YOU GIVE INVALID MONTH")
    exit()

birth_date = int(input('ENTER YOUR DATE OF BIRTH :- '))
if birth_date < 1 or birth_date > 31:
    print('ERROR : YOU GIVE INVALID DATE') 
    exit()


today = date.today()


cal_year = today.year - birth_year
if (today.month, today.day) < (birth_month , birth_date):
    cal_year -= 1

print(f'YOUR AGE IS :- {cal_year}')    




 