multiClaseOperar = lambda w,p: w*p
biClaseOperar = lambda w,p:w*p
aprendizajeBiClase1 = lambda w,p,u: w+u*p
aprendizajeBiClase2 = lambda w,p,u: w-u*p

def moreThan(k,fd,classes):
    bandera = 0
    m = 0
    for i in classes:
        if str(i) != k:
            m+=1
            if fd[k] <= fd[str(i)]:
                return False #no es mas grande que fd
    return True

def updateWeight(k,weight,classes,pattern,u):
    
    for i in classes:
        if str(i) != k:    
            weight[str(i)]["x"] = weight[str(i)]["x"]-pattern["x"]*u
            weight[str(i)]["y"] = weight[str(i)]["y"]-pattern["y"]*u
            weight[str(i)]["u"] = weight[str(i)]["u"]-pattern["u"]*u
        else:
            weight[k]["x"] = weight[k]["x"]+pattern["x"]*u
            weight[k]["y"] = weight[k]["y"]+pattern["y"]*u
            weight[k]["u"] = weight[k]["u"]+pattern["u"]*u
    
    return weight