#kalkulator

print(20*"_" , )
print(20*" " , )

uinput1 = float(input("Masukan angka : "))
operator = input("Masukan operator : ")
uinput2 = float(input("Masukan angka : "))

if operator == "+" :
        print(uinput1 + uinput2)
elif operator == "-" :
        print(uinput1 - uinput2)
elif operator == "*" :
        print(uinput1 * uinput2)
elif operator == "/" :
        print(uinput1 / uinput2)

print("Akhir")