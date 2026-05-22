print('------------python calculator-----------')

num1 = int(input('ENTER THE NUMBER :- '))
print('EX : + , - , * , / , % ')
oprator = input("ENTER THE OPRETOR YOU WANT TO PERFORM :- ")
num2 = int(input('ENTER THE NUMBER :- '))

if oprator == '+' :
    print(num1+num2)
elif oprator == '-' :
    print(num1-num2) 
elif oprator == '*' :
    print(num1*num2)
elif oprator == '/' :
    if num2 == 0:
        print('ERROR : CANNOT DIVIDE BY 0')
    else:    
        print(num1/num2)   
elif oprator == '%' :
    print(num1%num2)      
else:
    print('ERROR : INVALID OPPRETOR')            


