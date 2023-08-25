import pickle
import os
import json

# ใช้ pickle โหลด Model
model = pickle.load(open(os.getcwd()+r'/model/ClassifierCarModel.pkl', 'rb'))
#model = pickle.load(open(r'../model\ClassifierCarModel.pkl','rb'))

# ส่งค่า hog เข้าไป predictใน Method
def predictModel(hog):
    brand = model.predict(hog)
    return brand[0]