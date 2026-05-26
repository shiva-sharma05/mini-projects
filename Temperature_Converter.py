print('------------WELCOME TO TEMPERATURE CONVERTER-------------')

print('Choose conversion ')

print('press 1 for Celsius → Fahrenheit ')
print('press 2 for Fahrenheit → Celsius ')
print('press 3 for Celsius → Kelvin')

choice = int(input('ENTER YOUR CHOICE :- '))

if choice == 1:
    temp = float(input('ENTER THE TEMPERATURE :- '))
    ans = (temp * 9/5 ) + 32
    print(f"TEMPERATURE IS {ans}°F")

elif choice == 2:
    temp = float(input('ENTER THE TEMPERATURE :- '))
    ans = (temp - 32 ) * 5/9
    print(f"TEMPERATURE IS {ans}°C")

elif choice == 3:
    temp = float(input('ENTER THE TEMPERATURE :- '))
    ans = temp + 273.15
    print(f"TEMPERATURE IS {ans}K")

else:
    print('ERROR : INVALID CHOICE ')    

