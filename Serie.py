class Serie:
    def __init__(self,titulo="",numTemporadas=3,entregado=False,genero="",creador=""):
        self.titulo = titulo
        self.numTemporadas = numTemporadas
        self.entregado = entregado
        self.genero = genero
        self.creador = creador

    def __str__(self):
        return str(self.titulo + " " + repr(self.numTemporadas) + " " + repr(self.entregado) + " " + self.genero + " " + self.creador)