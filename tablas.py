from prettytable import PrettyTable

# Definir los datos
frecuencias = ["12.5 GHz", "25 GHz", "50 GHz", "12.5 GHz and above",
               "Approximate nominal central wavelengths(nm)"]
f12 = []
cluz = 2.99792458 * (10**-7)
finicio = 195.9
ft1 = 920
ft2 = int(ft1/2)
ft3 = int(ft1/4)
ft4 = int(ft1/8)

for i in range(ft1):
    f12.append(round(finicio - i * 0.0125, 4))

f25 = []
for i in range(ft2):
    f25.append(round(finicio - i * 0.025, 4))
    f25.append("-")

f50 = []
for i in range(ft3):
    f50.append(round(finicio - i * 0.05, 4))
    for j in range(3):
        f50.append("-")

f100 = []
for i in range(ft4):
    f100.append(round(finicio - i * 0.1, 4))
    for j in range(7):
        f100.append("-")

lnm = []
for i in f12:
    lnm.append(round((cluz/i)*10**12, 4))


# Crear una instancia de PrettyTable
tabla = PrettyTable()

# Añadir encabezados y columnas al PrettyTable
# tabla.field_names = ["F12", "F25", "F50", "F100", "Lambda (nm)"]
print("")
tabla.add_column("12.5 GHz", f12)
tabla.add_column("25 GHz", f25)
tabla.add_column("50 GHz", f50)
tabla.add_column("100 GHz and above", f100)
tabla.add_column("Approximate nominal central wavelengths", lnm)

# Imprimir la tabla
print(tabla)
