from sklearn.tree import DecisionTreeClassifier

# 0 -> smooth , 1-> bumpy
features = [[140,0], [130,0], [150,1], [170,1]]

# 0 -> apple, 1 -> orange
labels = [0,0,2,2]

clf = DecisionTreeClassifier()

clf.fit(features, labels)

prediction = clf.predict([[160,1]]) # orange

if prediction == 2:
    print "Orange"
else:
    print "Apple"
