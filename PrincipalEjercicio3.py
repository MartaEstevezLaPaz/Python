from Videojuego import Videojuego
from Serie import Serie

series = list()
juegos = list()

# def __init__(self,titulo="",numTemporadas=3,entregado=False,genero="",creador=""):

series.insert(-1, Serie(titulo="Serie1",numTemporadas=2,entregado=True))
series.insert(-1, Serie(titulo="Serie2",numTemporadas=2,entregado=False))
series.insert(-1, Serie(titulo="Serie3",numTemporadas=2,entregado=True))
series.insert(-1, Serie(titulo="Serie4",numTemporadas=2,entregado=False))
series.insert(-1, Serie(titulo="Serie5",numTemporadas=2,entregado=True))

juegos.insert(-1, Videojuego(titulo="Juego1", horasEstimadas=10,entregado=False))
juegos.insert(-1, Videojuego(titulo="Juego2", horasEstimadas=10,entregado=True))
juegos.insert(-1, Videojuego(titulo="Juego3", horasEstimadas=10,entregado=False))
juegos.insert(-1, Videojuego(titulo="Juego4", horasEstimadas=10,entregado=True))
juegos.insert(-1, Videojuego(titulo="Juego5", horasEstimadas=10,entregado=False))

serieMax = Serie()
juegoMax = Videojuego()

for i in series:
    if i.entregado:
        print(i)
        if i.numTemporadas > serieMax.numTemporadas:
            serieMax = i

for i in juegos:
    if i.entregado:
        print(i)
        if i.horasEstimadas > juegoMax.horasEstimadas:
            juegoMax=i

print("\nMayor: " + str(serieMax))
print("Mayor: " + str(juegoMax))