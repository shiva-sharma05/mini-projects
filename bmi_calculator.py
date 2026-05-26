print('-----------WELCOME TO BMI CALCULATOR--------------')

weight =float(input('ENTER YOUR WEIGHT (IN kg) :- '))
height = float(input('ENTER YOUR HEIGHT (IN meters):- '))

BMI = weight / (height*height)

print(f'YOUR BMI IS :- {BMI}')

print('YOUR BMI CATEGORY IS :- ')

if BMI < 18.5:
    print('Underweight')
elif BMI >= 18.5 and BMI <= 24.9:
    print('normal')    
elif BMI >= 25 and BMI <= 29.9:
    print('overweight')
else :
    print('Obese')    

