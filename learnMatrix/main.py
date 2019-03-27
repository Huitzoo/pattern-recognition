from learnMatrix import LearnMatrix
from patron import Patron
import copy

#Se ingresa un arreglo de patrones
patrones = []
c = 3

patrones.append(Patron([1,1,0,0,1],[1,0,0],0))
patrones.append(Patron([1,0,1,0,1],[0,1,0],1))
patrones.append(Patron([1,0,1,1,0],[0,0,1],2))
patrones.append(Patron([0,1,0,1,1],[1,0,0],0))

matrix = LearnMatrix()
matrix.Aprendizaje(patrones,c)

p = copy.deepcopy(matrix.Recuperacion(Patron([1,0,1,0,1],[0,0,0],None)))

print("Tu patron pertece a la clase: ", p.numero_clase)
