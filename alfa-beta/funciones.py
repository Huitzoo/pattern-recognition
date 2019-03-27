def Beta(fila,patron):
    val = -1 
    if fila == 0 and patron == 0:
        val = 0
    if fila == 0 and patron == 1:
        val = 0
    if fila == 1 and patron == 0:
        val = 0
    if fila == 1 and patron == 1:
        val = 1
    if fila == 2 and patron == 0:
        val = 1
    if fila == 2 and patron == 1:
        val = 1
    return val
    
def Alfa(fila,patron):
    val = -1
    if fila == 0 and patron == 0:
        val = 1
    if fila == 2 and patron == 1:
        val = 0
    if fila == 1 and patron == 0:
        val = 2
    if fila == 1 and patron == 1:
        val = 1
    return val

def Mini(v):
    v.sort()
    return v[0]
    
def Maxi(v):
    v.sort()
    return v[-1]