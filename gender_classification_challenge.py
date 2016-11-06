from sklearn import tree, neighbors, linear_model

# CHALLENGE - create 3 more classifiers...
clfs = (neighbors.KNeighborsClassifier(n_neighbors=3), linear_model.LogisticRegression(), tree.DecisionTreeClassifier())

# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

# test data
testData = [[174, 50, 36], [185, 80, 43], [177, 65, 41]]
correctAnswer = ['female', 'male', 'male']

# CHALLENGE - ...and train them on our data
predictions = []
for method in clfs:
    clf = method
    clf = clf.fit(X, Y)
    predictions.append(clf.predict(testData))

# CHALLENGE compare their results and print the best one!
bestResult = None
precision = 0
for result in predictions:
    correctAnswersCount = 0
    for i in range(len(result)):
        if result[i] == correctAnswer[i]:
            correctAnswersCount += 1
    # uncomment next line to print results for all methods
    # print (result, correctAnswersCount/len(result))
    if correctAnswersCount / len(result) > precision:
        precision = correctAnswersCount / len(result)
        bestResult = result

print("Best result: ", bestResult, "Precision: ", precision)
