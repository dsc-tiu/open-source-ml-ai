# K Nearest Neighbours(KNN)
The intuition behind KNN is that for a perticular datapoint we'll look for its nearest neighbours and predict it to be belonging to the most commomly occuring neighbouring class.

</br>

<img src="https://miro.medium.com/max/587/1*hncgU7vWLBsRvc8WJhxlkQ.png" width =400>

</br>

### Distance between two datapoints
The distance metric will define the relationship between two datapoints. More related the two datasets smaller will be the distance between them. It is an important criteria in predicting our results. 

</br>

<img src="https://miro.medium.com/max/1220/0*WrVc0CpxoStXpACy.png" width=300>

Distance metric of our model could be anything we want to, it can be euclidean distance or it could be manhattan distance or minkowski.

* Euclidean distance formula :

    <img src="https://miro.medium.com/max/1400/1*9LeaMTcOXxeTPN-VCbKloQ.png" width=200>

</br>

* Manhattan diastance formula :

    <img src="https://miro.medium.com/max/1018/1*KDgfdK6SooXtaUvlnXdpaA.png" width=210>

### Feature Scaling

Before applying KNN it is very important to apply feature scaling which involves transforming the data into a single range [0,1].

</br>

<img src="https://media-exp1.licdn.com/dms/image/C4E12AQFPqF6qfXYOvQ/article-cover_image-shrink_600_2000/0/1624324925880?e=2147483647&v=beta&t=C5ghUcvwlIFvEqyfLrB5bb4cL5z4mFYwQxzZscULq8c" width=400>

</br>

<img src="https://qph.cf2.quoracdn.net/main-qimg-63a05d8898505f9c84ba2c6427c9c78c" width=400>

</br>

### Value of K
K will give the number of nearest neighbours to look for while implementing KNN.In sklearn it is 5 by default though you can change it according to your need.

**Finding Optimal K**
* Large value of k leads to undefitting. 
* Small value of k leads to overfitting.

</br>

<img src="https://media.geeksforgeeks.org/wp-content/cdn-uploads/20190523171258/overfitting_2.png" width=600>

There is a sweet spot in between where there our optimal value of k resides which will lead to good performance on testing data.

### Code Description
 Our code contains a predict function which takes x_train,y_train and x_test values as argument along with K then for each dataset it returns the most common class of the K nearest neighbour to the dataset.

 After getting y_prediction we have evaluated our model using sklearn classification report and confusion matrix, and we can see that our model is doing well with high accuracy in testing data.