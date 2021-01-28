#import retrain
import pickle
import time
import os

#Loading the model
load_success_flag = 0
while not load_success_flag:
    try:
        model = pickle.load(open("model.pkl","rb"))
        print(model)
        load_success_flag = 1
        #time.sleep(0.1)
    except EOFError as e:
        print(e)
        pass