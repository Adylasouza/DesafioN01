h1 = int(input("Hora 1"))
m1 = int(input("Minuto 1"))
h2 = int(input("Hora 2"))
m2 = int(input("Minuto 2"))

somaH = h1 + h2
somaM = m1 + m2
if somaM > 59:
    #somaH=somaH+1
    somaH+=1
    #somaM=somaM-60
    somaM=somaM % 60
if somaH >=36:
    somaH = somaH - 36
elif somaH >24:
    somaH = somaH - 24
elif somaH >= 12:
    somaH = somaH - 12
print(f"{somaH} hora")