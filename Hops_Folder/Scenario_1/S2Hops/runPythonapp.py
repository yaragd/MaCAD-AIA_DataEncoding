import tensorflow as tf
#import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import joblib
import sklearn
import dill
#from sklearn.preprocessing import MaxAbsScaler

#Load saved model
def predictions(h, w, l, s):
    model = tf.keras.models.load_model('DirectSun03twisted.h5')
    model.summary()

    from sklearn.preprocessing import StandardScaler
    scalerX = joblib.load("scalerX.pkl")
    scalerY = joblib.load("scalerY.pkl")

    inputData = np.array([h,w,l,s])
    inputReshape = inputData.reshape(1,-1)
    x_scaled = scalerX.transform(inputReshape)
    x_reshape = x_scaled.reshape(1,4)

    predictions = model.predict(x_reshape)

    final_predictions = scalerY.inverse_transform(predictions)
    fakelist = final_predictions.tolist()

    list1 = predictions.tolist()
    flat_list = []

    for item in fakelist:
        flat_list += item
    
    print(flat_list)
    return flat_list





#######################################
#BONUS HINT

#if you had a scaler in your training you should have had this
##Normalize data using standard scaling
#scalerY = StandardScaler().fit(outputArr)
#y_scaled = scalerY.transform(outputArr)
#print("y_scaled", np.amin(y_scaled), np.amax(y_scaled))

##Save scaler model for later use
#joblib.dump(scalerY, 'scalerY.pkl')

#SO YOU NEED TO
#Load scaler for inverse transformation
#scalerY = joblib.load("scalerY.pkl")
#And apply it to either input or output

#########################################
