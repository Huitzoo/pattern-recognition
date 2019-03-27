import random
import json

patrones = "{"

patrones = patrones +'"1":{'

for i in range(0,10):
    if i == 9:
        patrones = patrones+'"'+str(i)+'":{"x":'+str(round(random.uniform(1.0, 2.0), 2))+',"y":'+str(round(random.uniform(1.0, 2.0), 2))+',"u":'+str(round(random.uniform(1.0, 2.0), 2))+',"clase":1}'
    else:
        patrones = patrones+'"'+str(i)+'":{"x":'+str(round(random.uniform(1.0, 2.0), 2))+',"y":'+str(round(random.uniform(1.0, 2.0), 2))+',"u":'+str(round(random.uniform(1.0, 2.0), 2))+',"clase":1},'    

patrones = patrones + '},'

patrones = patrones + '"2":{'

for i in range(0,10):
    if i == 9:
        patrones = patrones+'"'+str(i)+'":{"x":'+str(round(random.uniform(-1.0, -2.0), 2))+',"y":'+str(round(random.uniform(1.0, 2.0), 2))+',"u":'+str(round(random.uniform(1.0, 2.0), 2))+',"clase":2}'
    else:
        patrones = patrones+'"'+str(i)+'":{"x":'+str(round(random.uniform(-1.0, -2.0), 2))+',"y":'+str(round(random.uniform(1.0, 2.0), 2))+',"u":'+str(round(random.uniform(1.0, 2.0), 2))+',"clase":2},'    

patrones = patrones + '},'

patrones = patrones + '"3":{'

for i in range(0,10):
    if i == 9:
        patrones = patrones+'"'+str(i)+'":{"x":'+str(round(random.uniform(-1.0,-2.0), 2))+',"y":'+str(round(random.uniform(-1.0, -2.0), 2))+',"u":'+str(round(random.uniform(1.0, 2.0), 2))+',"clase":3}'
    else:
        patrones = patrones+'"'+str(i)+'":{"x":'+str(round(random.uniform(-1.0,-2.0), 2))+',"y":'+str(round(random.uniform(-1.0, -2.0), 2))+',"u":'+str(round(random.uniform(1.0, 2.0), 2))+',"clase":3},'    


patrones = patrones + '}'
patrones = patrones + '}'
print(patrones)