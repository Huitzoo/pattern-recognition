from funciones import Beta,Alfa,Mini,Maxi

class AlfaBeta():
    #vector s se suman los 1 que existan en la matriz
    
    matriz = []
    matriz_max = []
    matriz_min = []
    clases = 0
    letras = ["A","B","C"]
    def Aprendizaje(self,patrones,c):
        self.clases = c
        for i in range(c):
            aux = []
            for j in range(len(patrones[0].caracteristicas)):
                aux.append(0)
            self.matriz.append(aux)

        for i in patrones:
            for j in i.caracteristicas:
                for k in i.clase:
                    self.matriz[k][j] = Alfa(k,j)

        self.matrizMinima()
        self.matrizMaxima()

    def matrizMinima(self):
        m_min = []
        for i in self.matriz:
            aux = []
            for j in i:
                aux.append(j)
            m_min.append(Mini(aux))
        self.matriz_min = m_min

    def matrizMaxima(self):
        m_max = []
        for i in self.matriz:
            aux = []
            for j in i:
                aux.append(j)
            m_max.append(Maxi(aux))
        self.matriz_max=m_max

    def RecuperacionMin(self,patron):
        recoverA = []
        for i in self.matriz_min:
            aux = []
            for j in range(len(i)):
                aux.append(Beta(i[j],patron[j]))
            recoverA.append(aux)
        recover = []

        for i in recoverA:
            recover.append(Mini(i))
        
        return self.letras[2]
        
    
    def RecuperacionMax(self,patron):
        recoverA = []

        for i in self.matriz_max:
            aux = []
            for j in range(len(i)):
                aux.append(Beta(i[j],patron[j]))
            recoverA.append(aux)
        recover = []

        for i in recoverA:
            recover.append(Maxi(i))
        
        return self.letras[0]
                