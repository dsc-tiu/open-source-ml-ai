# Mean Absolute Error

The mean absolute error (MSE) tells you how close a regression line is to a set of points. It does this by taking the distances from the points to the regression line (these distances are the “errors”) and only taking the positive ditance(i.e absolute values). Then the mean is taken to average out the error over all cases.The lower the MAE better the model training.

![image](https://www.gstatic.com/education/formulas2/472522532/en/mean_absolute_error.svg)

To find the MAE, take the observed value, subtract the predicted value, and take absolute value of the difference. Repeat that for all observations. Then, sum all of those positive/absolute values and divide by the number of observations.

For example, in regression the mean absolute error represents the average gap from the mean

![image](https://user-images.githubusercontent.com/78155475/194711594-67ecd6cb-d9f9-42dc-b47f-3b154d4aff2d.png)

As the data points fall closer to the regression line, the model has less error, decreasing the MAE. A model with less error produces more precise predictions.
