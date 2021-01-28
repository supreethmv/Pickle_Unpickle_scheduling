#import retrain
import pickle
import time
import os

#Load the model
for i in range(1000):
    while not os.path.getsize("model.pkl"):
        pass
    model = pickle.load(open("model.pkl","rb"))
    print(model)
    time.sleep(0.1)