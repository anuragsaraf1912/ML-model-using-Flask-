import pickle
import numpy as np

def predict(data):
    X = np.array([[
        float(data['sepal_length']),
        float(data['sepal_width']),
        float(data['petal_length']),
        float(data['petal_width'])
    ]])
    # load the model from disk

    filename = 'pipe.sav'
    loaded_model = pickle.load(open(filename, 'rb'))
    y_pred = loaded_model.predict(X)
    
    names = np.array(['setosa', 'versicolor', 'virginica'])
    
    return names[y_pred[0]]
    