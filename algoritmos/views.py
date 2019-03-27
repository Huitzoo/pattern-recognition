from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
import math
import random
# Create your views here.


def estadistico(request):
    if request.method == 'POST':
        jsonAux = ""
        for i in request.FILES['clases']:
            jsonAux = jsonAux + i.decode("utf-8")
        clases = json.loads(jsonAux)
        totalClases = len(clases['clases'])
        total = clases['total']
        anterior = -1
        mayorP = 0
        probabilidad = []
        for c in clases['clases']:
            proba = str(round((c['total']/total*100),2))
            probabilidad.append(proba)
            if c['total'] > anterior:
                mayor = c['id']
                mayorP = proba
                anterior = c['total']

        response = {
            "totalClases" : totalClases,
            "total" : total,
            "mayor" : mayor,
            "mayorP":mayorP,
            "mayor" : mayor,
            "probabilidades":probabilidad
        } 
        return JsonResponse(response)

    else: 
        return render(request,"estadistico.html")


def bayesSimple(request):
    if request.method == 'POST':
        jsonAux = ""
        for i in request.FILES['clases']:
            jsonAux = jsonAux + i.decode("utf-8")
        clases = json.loads(jsonAux)
        totalClases = len(clases['clases'])
        tablaF = []
        tablaP = []
        anterior = -1
        tamano = 0
        muestra = clases['muestra']
        nombre_clases = list(clases['clases'].keys())
        nombre_patrones = list(clases['patrones'].keys()) 
        rasgo = clases['rasgo']
        probabilidades = []
        d = [0,0]
        for k,v in clases['clases'].items():
            tablaAux = []      
            tablaF.append(v['tamanos'])
            total = v['total']
            probabilidades.append(str(round(total/muestra,4)))
            for t in v['tamanos']:
                tablaAux.append(str(round(t/total, 4)))
            tablaP.append(tablaAux)
        for k,p in clases['patrones'].items():
            aleatoria = p['aleatoria']-1 #Esto es a probabilidad de la tabla
            aux = []
            i = 0
            for c in tablaP:
                if i > 0:
                    d[1] = math.log(float(probabilidades[i])) +  math.log(float(c[aleatoria]))
                    if d[1] > d[0]:
                        d[0] = d[1]
                        pertenencia = d[0]
                        claseP = nombre_clases[i]
                else:
                    d[0] = math.log(float(probabilidades[i])) +  math.log(float(c[aleatoria]))       
                i+=1
        response = {
            "num_clases" : len(nombre_clases),
            "nombre_clases":nombre_clases,
            "nombre_patrones":nombre_patrones,
            "rasgo" : rasgo,
            "tablaF" : tablaF,
            "tablaP" : tablaP,
            "claseP":claseP,
            "pertenencia":pertenencia,
        }
        return JsonResponse(response)
    return render(request,"bayesSimple.html")


def metricas(request):
    
    if request.method == 'POST':
        jsonAux = ""
        for i in request.FILES['clases']:
            jsonAux = jsonAux + i.decode("utf-8")
        clases = json.loads(jsonAux)['clases']
        clasificar = json.loads(jsonAux)['clasificar']
        pertenece_b = []
        pertenece_i = []
        pertenece_e = []
        numero_patrones = json.loads(jsonAux)['numero_patrones']
        euclideo = 0
        valor = 0
        city_block_response = []
        euclidea_response = []
        representantes = []
        city_block = []
        euclidea = []
        puntos = []
        clase = []
        patrones = []
        for i in clases:
            descripcion = clases[i]
            vector = descripcion["vectores"][str(random.randint(1,len(descripcion["vectores"])))]
            puntos.append(descripcion["vectores"])
            representantes.append(vector)
            clase.append(descripcion["nombre"])
        longitud = len(representantes[0])
        for i in clasificar:
            menor_euclideano = 9999999999999
            menor_block = 99999999999999999
            mayor = -9999999999999999
            for j in range(0,len(representantes)):
                for k in range(0,longitud):
                    valor = valor + math.pow(clasificar[i]["vector"][k]-representantes[j][k],2)
                euclideo = math.sqrt(valor)
                city_block.append(valor)
                city_block.append(j+1)
                euclidea.append(euclideo)
                euclidea.append(j+1)
                if valor < menor_block:
                    menor_block = valor
                    clase_city = clase[j]
                if euclideo < menor_euclideano:
                    menor_euclideano = euclideo
                    clase_euclidea = clase[j]
                if valor > mayor:
                    mayor = valor
                    clase_mayor = clase[j]
                city_block_response.append(city_block)
                euclidea_response.append(euclidea)
                city_block = []
                euclidea = []
                valor = 0
            patrones.append(clasificar[i]["vector"])
            pertenece = []
            pertenece.append(menor_block)
            pertenece.append(clase_city)
            pertenece_b.append(pertenece)
            pertenece = []
            pertenece.append(mayor)
            pertenece.append(clase_mayor)
            pertenece_i.append(pertenece)
            pertenece = []
            pertenece.append(menor_euclideano)
            pertenece.append(clase_euclidea)
            pertenece_e.append(pertenece)
        response = {
            "pertenece_b":pertenece_b,
            "pertenece_i":pertenece_i,
            "pertenece_e":pertenece_e,
            "representantes":representantes,
            "city_response":city_block_response,
            "euclidea_response":euclidea_response,
            "puntos":puntos,
            "nombre_patrones":clase,
            "patrones":patrones
        }
        return JsonResponse(response)
    return render(request,"metricas.html")


def euclideano(request):
    
    return render(request,"euclideano.html")
