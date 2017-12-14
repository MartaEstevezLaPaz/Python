
import random;


class Persona(object):

    def __init__(self, nombre, edad, sexo, peso, altura):
        self._nombre = nombre
        self._edad = edad
        self._SEXO_DEF = sexo
        self._peso = peso
        self._altura = altura
        self.generarIMC()

    def generarDni(self):
        divisor = 23
        _numDNI = (random.randint (10000000, 99999999))
        _res = _numDNI - (_numDNI / divisor * divisor)
        _letraDNI = self.generarLetraDNI(random.randint(0, 22))
        self._DNI = str(_numDNI) + _letraDNI
        return self._DNI

    def generarLetraDNI(self, _res):
        letra = ['T', 'R', 'W', 'A', 'G', 'M', 'Y','F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z','S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
        l = letra[_res]
        return l

    def generarIMC(self):

        self._pes = int(self._peso)
        self._alt = float(self._altura)/100

        imc = self._pes / (self._alt*self._alt)

        return imc

    def esMayoroNo(self):
        if self._edad < 18:
            frase = str("Es usted menor de edad")
        else:
            frase = str("Es usted mayor de edad")
        return frase

a = Persona("Marta", 18, "M", 52, 160)


a._nombre = raw_input("Nombre: ")
a._edad = raw_input("Edad: ")
a._sexo = raw_input("Sexo: ")
a._peso = raw_input("Peso: ")
a._altura = raw_input("Altura: ")

print "Su nombre: " + a._nombre
print "Su edad: " + a._edad
print a.esMayoroNo()
print "Su sexo: " + a._sexo 
print "Su DNI" +  a.generarDni()
print "Peso: " + a._peso + " kg "
print "Su altura: " +a._altura + "cm"
print "Indice de masa corporal: " + str(a.generarIMC())




