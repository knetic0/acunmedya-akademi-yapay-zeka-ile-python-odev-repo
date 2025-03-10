metin = input("Metin giriniz: ")

with open("metin.txt", "w") as dosya:
    dosya.write(metin)

with open("metin.txt", "r") as dosya:
    print(dosya.read())

with open("metin.txt", "a") as dosya:
    for i in range(5):
        metin = input("Metin giriniz: ")
        dosya.write("\n" + metin)