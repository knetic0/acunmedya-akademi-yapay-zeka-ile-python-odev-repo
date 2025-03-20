age = int(input("Yaşınızı giriniz: "))

if age >= 0 and age <= 12:
    print("Çocuk")
elif age >= 13 and age <= 19:
    print("Genç")
elif age >= 20 and age <= 59:
    print("Yetişkin")
else:
    print("Yaşlı")