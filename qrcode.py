import qrcode
import random
x=random.randint(10000,99999)
im=qrcode.make('OTP IS : '+str(x))
im.show()
