direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text1,shift1):  
    encrypt_text = ""
    for i in text1:
        encrypt_text += chr(ord(i)+shift1)
    print(F"This is the encrypted text: {encrypt_text}")    
def decrypt(text1,shift1):  
    decrypt_text = ""
    for i in text1:
        decrypt_text += chr(ord(i)-shift1)
    print(F"This is the decrypted text: {decrypt_text}")   

if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)
else :
    print("the direction is invalid!!")  

   
 