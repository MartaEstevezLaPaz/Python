class Electrodomestico(object):

	def __init__(self):
		self._COLOR_DEF = "blanco"
		self._CONSUMO_ENERGETICO_DEF = 'F'
		self._PRECIO_BASE_DEF = 100
		self._PESO_DEF = 5

        def comprobarColor(self, color):
            colores = ["blanco", "negro", "rojo", "azul", "gris"]
            encontrado = False
            for i in range(4):
                print(colores[i])


            if colores[i] == color:
                encontrado = True

            if encontrado:
                color = color
            else:
                color = self._COLOR_DEF


        def comprobarConsumo(self, consumo):
            if consumo >= 65 and consumo<=70:
                consumo = consumo
            else:
                consumo = self._CONSUMO_ENERGETICO_DEF


        def getPrecioBase(self):
            return self._PRECIO_BASE_DEF


        def getColor(self):
            return self._COLOR_DEF


        def getConsumoEnergetico(self):
            return self._CONSUMO_ENERGETICO_DEF


        def getPeso(self):
            return self._PESO_DEF

