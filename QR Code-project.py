
#-------------------QR CODE PROJECT---------------
#import the qrcode module
import qrcode
qr=qrcode.make("Please send the Money")
qr.save("docpy.png")
qr.show()