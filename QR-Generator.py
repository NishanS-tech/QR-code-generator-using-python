import qrcode

data =input("enter the link").strip
# Generate a QR code object from the given data
qr = qrcode.make(data)
filename=input("Enter file name to be saved")
# Save the generated QR code image with the given filename
qr.save(filename)
print("QR Code generated!") 
