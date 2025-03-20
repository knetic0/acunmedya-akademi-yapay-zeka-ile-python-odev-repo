def is_palindrom(s:str):
    s = s.lower()
    if s == s[::-1]:
        return True
    return False

inp = input("Bir kelime giriniz: ")
if(is_palindrom(inp)):
    print("Bu kelime palindromdur.")
else:
    print("Bu kelime palindrom değildir.")