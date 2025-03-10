metin = input("Metin giriniz: ")

with open("metin.txt", "w") as dosya:
    dosya.write(metin)

with open("metin.txt", "r") as dosya:
    print(dosya.read())

with open("metin1.txt", "w") as dosya:
    for i in range(5):
        metin = input("Metin giriniz: ")
        dosya.write(metin + "\n")

with open("metin1.txt", "r") as dosya:
    print(dosya.read())