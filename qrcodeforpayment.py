import qrcode

# taking input from the user 
upi_id = input('PLEASE ENTER YOUR UPI ID :- ')
amount = int(input('ENTER THE AMMOUT YOU WANT TO RECEIVE :-  '))

# define the payment url based on the upi id and the payment app
# you can modify this url based on the payment app you want to support

phonepay_url = f'upi://pay?pa={upi_id}&pn=recipent&cu=INR&am={amount}'

# to make the qr code for each payment app
phonepe_qr = qrcode.make(phonepay_url)

# for display the qr code 
phonepe_qr.show()
