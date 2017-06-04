import matplotlib.pyplot as plt
from sklearn import tree
from sklearn import datasets

iris = datasets.load_iris()


print "Targets are: ", iris.target
print "Data are: ", iris.data


clf = tree.DecisionTreeClassifier()
x,y = iris.data, iris.target

print x.shape 
clf.fit(x,y)

print "Prediction is : ", clf.predict(iris.data[5])
print "Real data is: ", iris.data[5]



