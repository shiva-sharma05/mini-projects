import random

print('WELCOME TO OTP GENRATOR')
length = int(input('WHAT THE LENGTH YOU WANT FOR OTP :- '))
otp = ""

for i in range(length):
    otp += str(random.randint(1,9))

print(f'YOUR OTP IS :- {otp}')    

