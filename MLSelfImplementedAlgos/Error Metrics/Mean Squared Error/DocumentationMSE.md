# Mean Squared Error

The mean squared error (MSE) tells you how close a regression line is to a set of points. It does this by taking the distances from the points to the regression line (these distances are the “errors”) and squaring them. The squaring is necessary to remove any negative signs. It also gives more weight to larger differences. It’s called the [mean ](https://www.statisticshowto.com/mean/)squared error as you’re finding the average of a set of errors. The lower the MSE, the better the forecast.

![image](https://user-images.githubusercontent.com/78155475/194711506-423752be-a396-4dd1-90bd-82004d1cc4a4.png)

The calculations for the mean squared error are similar to the variance. To find the MSE, take the observed value, subtract the predicted value, and square that difference. Repeat that for all observations. Then, sum all of those squared values and divide by the number of observations.

For example, in regression the mean squared error represents the average squared residual

![image](https://user-images.githubusercontent.com/78155475/194711594-67ecd6cb-d9f9-42dc-b47f-3b154d4aff2d.png)

As the data points fall closer to the regression line, the model has less error, decreasing the MSE. A model with less error produces more precise predictions.






