import random
import time
import os
import pyfiglet
from pyfiglet import Figlet


def numberGenerator():
    os.system('cls' if os.name == 'nt' else 'clear')

    print("<<", "=" * 66, ">>")
    f = Figlet(font='slant')
    ascii_art = f.renderText('  NPGenerator')
    print(ascii_art)
    print("<<", "=" * 66, ">>")

    for i in range(2):
        time.sleep(0.1)
    print(" ")
    awalan = input("Masukkan kode nomor telepon(+6289) : ")

    def generate_phone_number():
        rendem1 = ''.join(str(random.choice(range(10))) for _ in range(4))
        rendem2 = ''.join(str(random.choice(range(10))) for _ in range(4))
    
        hasil = awalan + rendem1 + rendem2
    
        return hasil
        
    jumlah = int(input("Masukkan jumlah nomor yang ingin dihasilkan : "))
    nama = input("Masukkan nama file : ")
    filename = nama+".txt"
    print(" ")
    print("<<", "=" * 66, ">>")
    for i in range(2):
        time.sleep(0.1)

    
    with open(filename, "w") as file:
        for _ in range(jumlah):
            nomor = generate_phone_number()
            file.write(nomor + "\n") 
    
    for i in range(3):
        time.sleep(0.1)
    print(" ")
    print(f"Nomor Telepon Berhasil Disimpan Sebagai {filename}")
    print("")
    print("<<", "=" * 66, ">>")
    print("")
    aww = str(input("Ingin Melanjutkan? y/N : "))
    if aww == "y" or aww == "Y":
        numberGenerator()
    elif aww == "n" or aww == "N":
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()

numberGenerator()