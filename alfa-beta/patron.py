
class Patron():
    caracteristicas = []
    clase = []
    claseResultado = []
    archivo = 0
    numero_clase = 0

    def __init__(self,caracteristicas,clase,c,archivo):
        self.caracteristicas = caracteristicas
        self.clase = clase
        self.claseResultado = [0]*len(clase)
        self.archivo = archivo
        self.numero_clase = c

