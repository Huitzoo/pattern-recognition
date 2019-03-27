

class LearnMatrix():
    #autorizacion
    #programa sintetico learning unit id
    
    e=2
    matriz = []
    clases = 0
    def Aprendizaje(self,patrones,c):
        self.clases = c
        for i in range(c):
            aux = []
            for j in range(len(patrones[0].caracteristicas)):
                aux.append(0)
            self.matriz.append(aux)
        for i in patrones:
            n = 0
            for j in i.caracteristicas:
                for k in i.clase:
                    if j == 1 and k == 1:
                        self.matriz[i.numero_clase][n] += self.e
                    elif j == 0 and k == 1:
                        self.matriz[i.numero_clase][n] += -self.e
                    else:
                        self.matriz[i.numero_clase][n] += 0
                n+=1
    
    def Recuperacion(self,patron):
        salida = [0]*self.clases
        n = 0
        for j in self.matriz:
            x = 0
            for k in j:    
                salida[n]+=patron.caracteristicas[x]*k
                x+=1 
            n+=1
        n = 0
        for i in range(1,len(salida)):
            if salida[i-1] > salida[i]:
                patron.numero_clase = i-1

        return patron
        
        