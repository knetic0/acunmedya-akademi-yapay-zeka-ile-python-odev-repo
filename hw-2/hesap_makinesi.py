def hesap_makinesi(num1:int, num2:int, operator:str):
    if operator not in ["+","-","*","/"]:
        return "Geçersiz işlem."
    
    if operator == "/" and num2 == 0:
        return "Bir sayı sıfıra bölünemez."
    
    result_str = f"{num1} {operator} {num2} = "
    
    if operator == "+":
        return result_str + str(num1 + num2)
    elif operator == "-":
        return result_str + str(num1 - num2)
    elif operator == "*":
        return result_str + str(num1 * num2)
    else:
        return result_str + str(num1 / num2)

num1 = int(input("Birinci sayıyı giriniz: "))
num2 = int(input("İkinci sayıyı giriniz: "))
operator = input("Yapılacak Olan İşlemi giriniz: ")

result = hesap_makinesi(num1,num2,operator)

print(result)