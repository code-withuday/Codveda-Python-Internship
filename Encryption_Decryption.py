message = input("enter name: ")

shift = 3

encrypted = ""

for i in message:
    encrypted += chr(ord(i) + (shift))

print("encrypted message: ", encrypted)