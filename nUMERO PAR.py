x=int(input("Dame un número: "))
if ((x/2)%2==0):
    print("No es el doble de un número impar")
elif ((x/2)%2==1):
    print(x," Si es el doble de un número impar")
else:
    print("No hay solución")
