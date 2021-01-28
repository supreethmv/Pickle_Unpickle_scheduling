#import retrain
import pickle
import time
import os

miss = 0
#Load the model
for i in range(1000):
    try:
        model = pickle.load(open("model.pkl","rb"))
        print(model)
    except EOFError as e:
        print(e)
        miss+=1
        pass
miss_rate = miss / 1000
print("Miss Rate =",miss_rate)