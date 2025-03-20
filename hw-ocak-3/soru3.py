num = int(input("Bir sayı giriniz: "))

faktoriyel = 1
temp = num
while(temp > 1):
    faktoriyel = faktoriyel * temp
    temp = temp - 1

print(f"{num} sayısının faktoriyeli: {faktoriyel}")