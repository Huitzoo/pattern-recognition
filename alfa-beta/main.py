from PIL import Image,ImagePalette
import numpy as np
import os
from PIL import Image,ImagePalette
import numpy as np
import os
from patron import Patron
import copy
from alfaBeta import AlfaBeta

archivos = os.listdir("letras/entrenamiento/")
path = os.getcwd()+"/letras/entrenamiento/"
patrones = []
clases = [[0,1,0],[1,0,0],[0,0,1]]
p = 0
bandera = 0
for a in archivos:
    rasgo = []
    img = Image.open(path+a)
    pixeles = np.array(img)
    for i in pixeles:
        for j in i:
            if j[0] == 255:
                rasgo.append(1)
            else:
                rasgo.append(0)
    patrones.append(Patron(rasgo,clases[p],p,a))
    p += 1

alfaBeta = AlfaBeta()
alfaBeta.Aprendizaje(patrones,p)

rasgo = []
path = os.getcwd()+"/letras/"
img = Image.open(path+"c_bis.bmp")
bandera = 1
pixeles = np.array(img)
for i in pixeles:
    for j in i:
        if j[0] == 255:
            rasgo.append(1)
        else:
            rasgo.append(0)
p = copy.deepcopy(alfaBeta.RecuperacionMin(rasgo))

print("Tu clase es: ",p)
