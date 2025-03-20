inputs = list(int(input(f"{i+1}. sayıyı giriniz: ")) for i in range(10))

founded = []
for num in inputs:
    if num not in founded:
        founded.append(num)

print(founded)