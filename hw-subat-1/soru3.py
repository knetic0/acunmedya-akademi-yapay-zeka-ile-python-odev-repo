def calc_year(age:int):
    if age >= 100:
        return 0
    return 100 - age

age = int(input("Yaşınızı giriniz: "))

print(f"100 yaşına gelmenize {calc_year(age)} yıl kaldı.")