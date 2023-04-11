
from tkinter import *
from tkinter import messagebox
import base64
from Crypto.Cipher import AES, DES, DES3
from secrets import token_bytes

def main_screen():
    screen = Tk()
    screen.geometry("800x450")
    screen.title("PCTAPP")

    def reset():
        code.set("")
        text1.delete(1.0, END)
        text2.delete(1.0, END)

    def encrypt_aes():
        key = token_bytes(16)
        message = text1.get(1.0, END).encode()
        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(message)
        text2.delete(1.0, END)
        text2.insert(INSERT, base64.b64encode(ciphertext).decode())

    def decrypt_aes():
        key = token_bytes(16)
        ciphertext = base64.b64decode(text2.get(1.0, END))
        cipher = AES.new(key, AES.MODE_EAX)
        message = cipher.decrypt(ciphertext).decode()
        text1.delete(1.0, END)
        text1.insert(INSERT, message)

    def encrypt_des():
        key = token_bytes(8)
        message = text1.get(1.0, END).encode()
        cipher = DES.new(key, DES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(message)
        text2.delete(1.0, END)
        text2.insert(INSERT, base64.b64encode(ciphertext).decode())

    def decrypt_des():
        key = token_bytes(8)
        ciphertext = base64.b64decode(text2.get(1.0, END))
        cipher = DES.new(key, DES.MODE_EAX)
        message = cipher.decrypt(ciphertext).decode()
        text1.delete(1.0, END)
        text1.insert(INSERT, message)
        
    def encrypt_3des():
        key = token_bytes(32)
        message = text1.get(1.0, END).encode()
        cipher = DES3.new(key, DES3.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(message)
        text2.delete(1.0, END)
        text2.insert(INSERT, base64.b64encode(ciphertext).decode())

    def decrypt_3des():
        key = token_bytes(32)
        ciphertext = base64.b64decode(text2.get(1.0, END))
        cipher = DES3.new(key, DES3.MODE_EAX)
        message = cipher.decrypt(ciphertext).decode()
        text1.delete(1.0, END)
        text1.insert(INSERT, message)


    Label(text="Enter text for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)

    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calbri", 13)).place(x=10, y=170)
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)
    
    Label(text="This is the cipher text of your message", fg="black", font = ("calbri", 13)).place(x=400, y= 10)
    text2 = Text(font = "Robote 20", bg = "white", relief=GROOVE, wrap=WORD, bd=2)
    text2.place(x=400, y=50, width=350, height=180)

    Button(text="ENCRYPT (AES)", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt_aes).place(x=10, y=250)
    Button(text="DECRYPT (AES)", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt_aes).place(x=200, y=250)
    Button(text="ENCRYPT (DES)", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt_des).place(x=390, y=250)
    Button(text="DECRYPT (DES)", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt_des).place(x=580, y=250)
    Button(text="ENCRYPT (3DES)", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt_3des).place(x=200, y=320)
    Button(text="DECRYPT (3DES)", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt_3des).place(x=390, y=320)
    Button(text="RESET", height="2", width=80, bg="#1089ff", fg="white", bd=0, command=reset).place(x=100, y=380)
    
   
    # Label(text="Encrypted/Decrypted Text", fg="black", font=("calbri", 13)).place(x=10, y=350)
    # text2 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    # text2.place(x=10, y=390, width=780, height=100)

    screen.mainloop()


main_screen()

