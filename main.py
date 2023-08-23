import math

class Secuencial:
    def __init__(self, matriz):
        self.matriz = matriz
    def busqueda(self, valor):
        for i in self.matriz:
            if i == valor:
                return print(f"(Secuencial) el valor {valor} se encontró")
        return print(f"(Secuencial) el valor {valor} no se encontró")

class Binario:
    def __init__(self, matriz):
        self.matriz = matriz
    def busqueda(self, valor):
        tamaño = len(self.matriz)
        copia = self.matriz
        while True:
            central = math.trunc(tamaño / 2)
            if(tamaño % 2 == 0):
                central -= 1
            # print(central, copia, valor, copia[central], tamaño)
            if valor == copia[central]:
                return print(f"(Binario) el valor {valor} se encontró")
            elif valor < copia[central] and tamaño > 1:
                copia = copia[:central]
            elif valor > copia[central] and  tamaño > 1:
                copia = copia[central + 1:]
            elif tamaño <= 1:
                return print(f"(Binario) el valor {valor} no se encontró")

            tamaño = len(copia)

class TransfClaves():
    def __init__(self, matriz, funcion, tamaño):
        self.matriz = matriz
        self.tamaño = tamaño
        self.estructura = {}
        self.fn = funcion
        self.crearDiccionario()

    def crearDiccionario(self):
        for value in self.matriz:
            clave = self.obtenerClave(value)
            if (len(self.estructura) < self.tamaño):
                if (clave in self.estructura):
                    print("\033[0;31m El elemento " + str(value) + " presenta una colision con " + str(
                        self.estructura.get(clave)) + " al intentar guardarlo con la clave " + str(
                        clave) + "\033[0;37m")
                else:
                    self.estructura[clave] = value
                    print("se ha guardado exitosamente a " + str(value) + " | clave: " + str(clave))
            else:
                print("\033[0;31m" + "La estructura ya está llena, no se ha introducido " +
                      str(value) + "\033[0;37m")
                break
        print("\033[0;32mse ha creado la estructura con la funcion " + self.fn + "\033[0;37m")
        print("")
    def obtenerClave(self, value):
        if (self.fn == "Mod"):
            clave = (value % self.tamaño) + 1
        elif (self.fn == "Cuadrada"):
            potencia = value ** 2
            init = (len(str(potencia)) - 1) // 2 if len(str(potencia)) % 2 == 0 else len(str(potencia)) // 2
            claveTemp = str(potencia)[init:init + len(str(self.tamaño - 1))]
            clave = 1 if claveTemp == "" else int(claveTemp) + 1
        elif (self.fn == "Truncamiento"):
            init = len(str(self.tamaño)) - 1
            if init == 0:
                init += 1
            value_str = str(value)
            sub_strings = [
                int(digit) for i, digit in enumerate(value_str) if i % 2 == 0
            ]
            clave = int(''.join(str(num) for num in sub_strings)) + 1
        elif (self.fn == "Plegamiento"):
            init = len(str(self.tamaño)) - 1
            if init == 0:
                init += 1
            value_str = str(value)
            sub_strings = [
                value_str[i:i + init] for i in range(0, len(value_str), init)
            ]
            clave = sum(int(sub) for sub in sub_strings) + 1
            if clave > self.tamaño:
                clave = clave % (10 ** init)
        else:
            raise Exception("La función dada no es válida")
        return clave
    def buscarElemento(self, elemento):
        clave = self.obtenerClave(elemento)
        print("la clave de " + str(elemento) + " es " + str(clave))
        if (clave in self.estructura):
            if (self.estructura.get(clave) == elemento):
                print("\033[0;32m" + str(elemento) + " se encuentra en la estructura con la clave " + str(
                    clave) + "\033[0;37m")
            else:
                print("\033[0;31m" + str(elemento) + " No está en la estructura. La clave " +
                      str(clave) + " contiene a " + str(self.estructura.get(clave)) + "\033[0;37m")
        else:
            print("\033[0;31m" + "La estructura no contiene la clave " +
                  str(clave) + "\033[0;37m")

# Datos definidos
lista1 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
lista2 = [53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
lista3 = [1234, 3231, 5435, 5322, 1240]

print("- - - - - - - - - - -")
secuencial = Secuencial(lista1)
print("Búsqueda secuencial en lista 1: buscar número 29")
secuencial.busqueda(29)

print("Búsqueda secuencial en lista 1: buscar número 4")
secuencial.busqueda(4)

print("- - - - - - - - - - -")
binario = Binario(lista2)
print("Búsqueda binaria en lista 2: buscar número 83")
binario.busqueda(83)
print("Búsqueda binaria en lista 2: buscar número 13")
binario.busqueda(13)

print("- - - - - - - - - - -")
print("Prueba de hash cuadrado")
hashCuadrado = TransfClaves(lista3, "Cuadrada", 100)
print("Búsqueda hash mod en lista 3: buscar número 1240")
hashCuadrado.buscarElemento(1240)
print("Búsqueda hash mod en lista 3: buscar número 41")
hashCuadrado.buscarElemento(41)

print("- - - - - - - - - - -")
print("Prueba de hash plegamiento")
hashPlegamiento = TransfClaves(lista3, "Plegamiento", 10)
print("Búsqueda hash plegamiento en lista 3: buscar número 1240")
hashPlegamiento.buscarElemento(1240)
print("Búsqueda hash plegamiento en lista 3: buscar número 41")
hashPlegamiento.buscarElemento(41)

print("- - - - - - - - - - -")
print("Prueba de hash truncamiento")
hashTruncamiento = TransfClaves(lista3, "Truncamiento", 5)
print("Búsqueda hash truncamiento en lista 3: buscar número 1240")
hashTruncamiento.buscarElemento(1240)
print("Búsqueda hash truncamiento en lista 3: buscar número 41")
hashTruncamiento.buscarElemento(41)

print("- - - - - - - - - - -")
print("Prueba de hash mod")
hashMod = TransfClaves(lista3, "Mod", 10)
print("Búsqueda hash mod en lista 3: buscar número 1240")
hashMod.buscarElemento(1240)
print("Búsqueda hash mod en lista 3: buscar número 43")
hashMod.buscarElemento(43)
