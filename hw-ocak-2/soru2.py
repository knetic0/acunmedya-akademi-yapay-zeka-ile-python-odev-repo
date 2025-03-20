puan = int(input("Notunuzu giriniz: "))

if puan <= 100 and puan >= 90:
    print("A")
elif puan < 90 and puan >= 80:
    print("B")
elif puan < 80 and puan >= 70:
    print("C")
elif puan < 70 and puan >= 60:
    print("D")
else:
    print("F")