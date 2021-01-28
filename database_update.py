import retrain
import random

for i in range(10000):
    f = open("database.txt",'w')
    f.write(str(random.random()))
    f.close()
    retrain.retrain_fun()          #comlplex operation