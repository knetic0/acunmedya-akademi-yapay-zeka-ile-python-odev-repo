def asal_mi(num:int):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

inp = int(input("Sayı giriniz: "))

result = asal_mi(inp)

if result:
    print(f"{inp} bir asal sayıdır.")
else:
    print(f"{inp} bir asal sayı değildir.")