import random
import string
import pyperclip

print('WELCOME TO THE PASSWORD GENRETOR')

all_chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(8):
    password += random.choice(all_chars)

print(f" YOUR GENRETED PASSWORD IS :- {password}")

print("DO YOU WANT TO COPY THE THE PASSWORD (YES = y NO = n) ")
copy = input("ENTER YOU CHOICE :- ")
if copy.lower() == 'y':
    pyperclip.copy(password)
    print("PASSWORD COPIED TO CLIPBOARD")
elif copy.lower() == 'n':
    print('THANKS FOR USING..........') 
else:
    print("ERROR : INVALID CHOICE")    