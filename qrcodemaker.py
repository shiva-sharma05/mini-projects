# to make the qr code of any thing paste the url of that in the terminal

import qrcode # import the qr code library

# to make the qr coed url must important
url = input('ENTER YOUR URL :- ') 

# this function helps to make the qr
url_qr = qrcode.make(url)

# this function show the qr code
url_qr.show()
