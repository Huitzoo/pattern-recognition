from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views import View
import json
import math
import random
import copy
import nltk
from .funciones import multiClaseOperar,moreThan,updateWeight,biClaseOperar,aprendizajeBiClase1,aprendizajeBiClase2
import operator
import tensorflow as tf
import numpy as np

# Create your views here.
#con base a k se selecciona el peso.

class KNNView(View):
    training = None
    results = None
    k = 0
    w = None
    classes = 0

    def get(self,request):
        return render(request,"knn.html")
    
    def post(self,request):
        jsonAux = ""
        distance = []
        for i in request.FILES['clases']:
            jsonAux = jsonAux + i.decode("utf-8")
        self.training = json.loads(jsonAux)['entrenamiento']
        clasificar = json.loads(jsonAux)['clasificar']
        self.k = json.loads(jsonAux)['k']
        self.classes = json.loads(jsonAux)['classes']

        for j in clasificar:
            self.pattern = j
            self.calcDistance()
            distance.append(self.results[-1])
            classe = self.doKnn()
            self.addClass(classe)
        
        response = {
            "distances":distance,
            "classes": self.classes,
            "classified":len(clasificar),
            "results":self.training,
            "total":len(self.training),
        }
        return JsonResponse(response)
    
    def doKnn(self):
        randoms = 0
        neighbors = []
        votes = [0]*self.classes
        self.w = []
        flag = 0
        classe = 0
        while(randoms<self.k):
            r = random.uniform(0.001,0.799)
            if not randoms in self.w:
                randoms += 1   
                self.w.append(r)
        self.w.sort(reverse=True)
        neighbors = self.results[:self.k]
        for k in neighbors:
            votes[int(k['class'])-1] = votes[int(k['class'])-1] + 1
        
        for k in range(1,len(votes)):
            if votes[k] == votes[k-1]:
                flag = 1
        if flag == 1: #hubo un empate
            votes = [0]*self.classes
            for k in range(0,len(self.w)):
                votes[int(neighbors[k]['class'])-1] = votes[int(neighbors[k]['class'])-1] + self.w[k]
    
        for v in range(1,len(votes)):
            if votes[v] < votes[v-1]:
                classe = v
        return classe

    def calcDistance(self):
        for i in self.training:
            i['distance'] = math.sqrt(math.pow((i['x']-self.pattern['x']),2) + math.pow((self.pattern['y']-i['y']),2))
        self.results = copy.deepcopy(sorted(self.training, key=lambda k: k['distance']))
    
    def addClass(self,classe):
        self.pattern['class'] = classe    
        self.training.append(copy.deepcopy(self.pattern))

class BayesTexto(View):
    def post(self,request):
        text = nltk.Text(nltk.word_tokenize(request.POST.get("frase")))
        lista = [nltk.tag.str2tuple(t) for t in text]
        
        brown_news_tagged = nltk.corpus.brown.tagged_words(categories='news', tagset='universal')

        print(brown_news_tagged)
        
    def get(self,request):
        return render(request,"bayesTexto.html")

class MultiClase(View):
    def post(self,request):
        configure = ""
        if int(request.POST.get("training")) == 1:
            for i in request.FILES['clases']:
                configure = configure + i.decode("utf-8")
            configure = json.loads(configure)
            training = configure['patrones']
            weight = configure['pesos']
            classes = configure['clases']
            bias = configure['bias']
            numeroPatrones = configure['numeroPatrones']
            fd = {}
            errores = 1
            bandera = 0
            while(bandera<2):
                while(errores):
                    errores = 0
                    tam = 0
                    while(tam!=numeroPatrones):
                        for i in training: #recorrer los patrones
                            pattern = training[i][str(tam)]
                            for k in weight:
                                fds = 0
                                for n in weight[k]:
                                    fds = fds+multiClaseOperar(weight[k][n],pattern[n])
                                fd[k] = fds
                            if not moreThan(i,fd,classes):
                                weight = copy.deepcopy(updateWeight(i,weight,classes,pattern,0.5))
                                errores = errores+1
                                bandera = 0
                        tam+=1
                bandera += 1
            response = {
                "weight": weight,
                "patterns":training,
                "classes":len(classes)
            }
            return JsonResponse(response)            
        
        else:
            f = 0
            point = {
                "x":float(request.POST.get("x")),
                "y":float(request.POST.get("y")),
                "u":0
            }
            weightX = request.POST.get("xp")
            weightY = request.POST.get("yp")
            f = f + biClaseOperar(float(weightX),point["x"])
            f = f + biClaseOperar(float(weightY),point["y"])
            if f > 0:
                clase = 1
            else:
                clase = 2
            response = {
                "point":point,
                "clase":clase
            }
            return JsonResponse(response)            

    def get(self,request):
        return render(request,"multiClase.html")


class BiClase(View):
    def post(self,request):
        if request.POST.get("training") == "1":
            configure = ""
            for i in request.FILES['clases']:
                configure = configure + i.decode("utf-8")
            configure = json.loads(configure)
            training = configure['patrones']
            weight = configure['pesos']
            classes = configure['clases']
            u = configure['u']
            errores = 1
            while(errores):
                errores = 0
                for i in training:
                    pattern = training[i]
                    for j in pattern:
                        f = 0
                        for k in weight:
                            f = f + biClaseOperar(weight[k],pattern[j][k])
                        if i == '1':
                            if f > 0:
                                pass
                            else:
                                errores = errores+1
                                for k in weight:
                                    weight[k] = aprendizajeBiClase1(weight[k],pattern[j][k],u)
                        else:
                            if f < 0:
                                pass
                            else:
                                errores = errores+1
                                for k in weight:
                                    weight[k] = aprendizajeBiClase2(weight[k],pattern[j][k],u)    
                    
            response = {
                "classes":len(classes),
                "weight":weight,
                "patterns":training
            }
        else:
            f = 0
            point = {
                "x":float(request.POST.get("x")),
                "y":float(request.POST.get("y")),
                "u":0
            }
            weightX = request.POST.get("xp")
            weightY = request.POST.get("yp")
            f = f + biClaseOperar(float(weightX),point["x"])
            f = f + biClaseOperar(float(weightY),point["y"])
            if f > 0:
                clase = 1
            else:
                clase = 2
            response = {
                "point":point,
                "clase":clase
            }
    
        return JsonResponse(response)            

    def get(self,request):
        return render(request,"biClase.html")

class PerceptronNAND(View):
    def get(self,request):
        NUM_FEATURES = 2
        NUM_ITER = 2000
        learning_rate = 0.01
        x = np.array([[0, 0], [1, 0], [1, 1], [0, 1]], np.float32) # 4x2, input
        y = np.array([1, 1, 0, 1], np.float32) # 4, correct output, AND operation
        #y = np.array([0, 1, 1, 1], np.float32) # OR operation

        W = np.zeros(NUM_FEATURES, np.float32) # 2x1, weight
        b = np.zeros(1, np.float32) # 1x1

        N, d = np.shape(x) # number of samples and number of features

        # process each sample separately
        for k in range(NUM_ITER):
            for j in range(N):
                yHat_j = x[j, :].dot(W) + b # 1x2, 2x1
                yHat_j = 1.0 / (1.0 + np.exp(-yHat_j))

                err = y[j] - yHat_j # error term
                deltaW = err * x[j, :]
                deltaB = err
                W = W + learning_rate * deltaW # if err = y - yHat, then W = W + lRate * deltW
                b = b + learning_rate * deltaB

        # Now plot the fitted line. We need only two points to plot the line
        plot_x = np.array([np.min(x[:, 0] - 0.2), np.max(x[:, 1]+0.2)])
        plot_y = - 1 / W[1] * (W[0] * plot_x + b) # comes from, w0*x + w1*y + b = 0 then y = (-1/w1) (w0*x + b)
        print("w: ",W)
        context = {
            "compuerta":{
                "0":{"x":0,"y":0},
                "1":{"x":0,"y":1},
                "2":{"x":1,"y":0},
                "3":{"x":1,"y":1},
            },

            "x1":plot_x[0],
            "x2":plot_x[1],
            "y":plot_y,
            "pesos1":W[0],
            "pesos2":W[1],
            "bias":b
        }
        return render(request,"perceptronNAND.html",context)

    def step(x):
        is_greater = tf.greater(x, 0)
        as_float = tf.to_float(is_greater)
        doubled = tf.mul(as_float, 2)
        return tf.sub(doubled, 1)