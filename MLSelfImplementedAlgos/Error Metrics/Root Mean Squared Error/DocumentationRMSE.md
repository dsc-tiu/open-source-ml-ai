# Root Mean Squared Error

The Root mean squared error (RMSE) tells you how close a regression line is to a set of points. It does this by taking the distances from the points to the regression line (these distances are the “errors”) ,squaring them and taking whole root. The squaring is necessary to remove any negative signs. It also gives more weight to larger differences, to keep the final value from reaching very high values, root of it is taken as error metric in RMSE. It’s called the root [mean ](https://www.statisticshowto.com/mean/)squared error as you’re finding the root of the average of a set of errors squred. The lower the RMSE, the better the forecast.

![image](https://www.gstatic.com/education/formulas2/472522532/en/root_mean_square_deviation.svg)

The calculations for the root mean squared error are similar to the standard deviation. To find the RMSE, take the observed value, subtract the predicted value, and square that difference. Repeat that for all observations. Then, sum all of those squared values and divide by the number of observations.And finally take root of the value obtained in the previous step.

For example, in regression the root mean squared error represents the root of average squared residual

![image](https://user-images.githubusercontent.com/78155475/194711594-67ecd6cb-d9f9-42dc-b47f-3b154d4aff2d.png)

As the data points fall closer to the regression line, the model has less error, decreasing the MSE. A model with less error produces more precise predictions.
