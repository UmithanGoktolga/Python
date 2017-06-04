import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100)

x,y = digits.data[:-1], digits.target[:-1]
clf.fit(x,y)
plt.plot(digits.data[:5],digits.target[:5])
plt.ylabel("targets")
plt.xlabel("data")
plt.show()

print "Prediction is : " , clf.predict(digits.data[12])
plt.imshow(digits.images[12], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()