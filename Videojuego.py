class Videojuego:
    def __init__(self, titulo="", horasEstimadas=10, entregado=False, genero="", company=""):
        self.titulo = titulo
        self.horasEstimadas = horasEstimadas
        self.entregado = entregado
        self.genero = genero
        self.company = company

    def __str__(self):
        return str(self.titulo + " " + repr(self.horasEstimadas) + " " +  repr(self.entregado) + " " + self.genero + " " + self.company)