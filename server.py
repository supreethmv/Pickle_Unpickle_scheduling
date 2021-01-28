from flask import Flask
import retrain

app = Flask(__name__)

if __name__ == '__main__':
    retrain.retrain_fun()
    app.run()