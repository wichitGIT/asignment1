from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
import pickle


#path ของไฟล์ .pkl ที่คุณต้องการอ่าน
file_train = "trainfeaturevector.pkl"
file_test = "testfeaturevector.pkl"

# ทำการอ่านข้อมูลจากไฟล์ .pkl
with open(file_train, "rb") as file:
    featurevector_train = pickle.load(file)
with open(file_test, "rb") as file:
    featurevector_test = pickle.load(file)

#set ข้อมูลให้กับ x_train, y_train, x_test, y_test
def setData(dataset):
    x = []
    y = []
    for index, value in enumerate(dataset):
        x.append( dataset[index][ : len(dataset[index])-1] )
        y.append( dataset[index][len(dataset[index])-1] )
    return x, y

x_train, y_train = setData(featurevector_train)
x_test, y_test = setData(featurevector_test)
print(len(x_train))
print(len(y_train))
print(len(x_test))
print(len(y_test))

model = DecisionTreeClassifier()
model = model.fit(x_train, y_train)
Ypred = model.predict(x_test)
#เก็บค่าความถูกต้อง ความแม่นำ
accuracy = metrics.accuracy_score(y_test, Ypred) * 100
#เก็บผลที่ได้จากการ test ลงในmatrix โดยแนวทแยงจะเป็นค่าที่ถูกต้อง
matrix = metrics.confusion_matrix(y_test, Ypred)

print("\nAccuracy:", accuracy)

print("Confusion matrix:\n", matrix)

rite = 'ClassifierCarModel.pkl'
pickle.dump(model, open(rite, 'wb'))
print("\nClassifierCarModel.pkl file saved.")