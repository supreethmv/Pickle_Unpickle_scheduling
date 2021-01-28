import time
import pickle

def retrain_fun():
    f = open("database.txt",'r')
    #time.sleep(1)           #comlplex operation
    model = f.read()
    pickle.dump(model,open("model.pkl","wb"))
    f.close()
    print(model)