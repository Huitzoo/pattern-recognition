
class Patron():
    caracteristicas = []
    clase = []
    claseResultado = []
    numero_clase = 0
    
    def __init__(self,caracteristicas,clase,numero_clase):
        self.caracteristicas = caracteristicas
        self.clase = clase
        self.claseResultado = [0]*len(clase)
        self.numero_clase = numero_clase

