hora01 = int(input("Digite primeiramente a hora da primeira entrada: "))
minu01 = int(input("Digite primeiramente os minutos da primeira entrada: "))
hora02 = int(input("Digite primeiramente a hora da segunda entrada: "))
minu02 = int(input("Digite primeiramente os minutos da primeira entrada: "))
print("____________________________________________________________________________")

hora = 0
minuto = 0
saida = 0

if hora:
    hora = hora01 + hora02
    hora = hora%12

else:
    if minuto >=60:
        minuto = minu01 + minu02
    else:
        minuto = hora + 1


print(hora, minuto)
#if saida:
    #saida = print(f"{hora}:{minuto}")





