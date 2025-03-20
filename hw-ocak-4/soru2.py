inputs = input("İstediğiniz kadar kelime giriniz: ")

kelimeler = inputs.split()

for kelime in kelimeler[::-1]:
    print(kelime, end=" ")