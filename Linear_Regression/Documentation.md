# **Linear Regression**
Linear regression is a *supervised* machine learning model which tries to best fit the linear expression on the training dataset to best predict for the future x input values.

</br>

<img src="https://files.realpython.com/media/fig-lin-reg.a506035b654a.png" width=700>

</br>

## Hypothesis



In the above image the slope is called the *hypothesis*
and the y-intercept is called the *bias*. Linear regression model tries to optimize the slope by using the cost function.

hypothesis function is given by :-

<img src="https://miro.medium.com/max/3952/1*4RTaC3lmtnYSlO6d1G1fow.png" width=500>

</br>

here, parameters (theta) are the weights of the respective features(x).

</br>

## Cost Function
This function gives the loss of data against the predicted values. The cost function of regression model is given by :-

</br>

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTn76tumn9T1b0cSPtU-4OXDToIyS93IdtNLfbKyq7gI2iJ2sWbrRk6Dnk6euzQ-EjY_w&usqp=CAU " width=300>

</br>

## Gradient Descent

</br>

<img src="https://aiaspirant.com/wp-content/uploads/2019/07/gradient-descent.png" width=500>

</br>

The weights and bias are optimized by using *Gradient descent* which attempts to find a global/local minima of the cost function plotted against the weights.

</br>

<img src="https://miro.medium.com/max/450/1*8Omixzi4P2mnqdsPwIR1GQ.png" width=400>

</br>

* Here, alpha is the learning rate which determines the size of steps taken to reach the required minima. If its value is too large, the counter will bounce back and forth and will never reach the minima. Also if its value is too low then the will surely reach the minima but will a lot of time. So, there is a sweet spot in between in which the learning rate must reside to make optimum calculations.

</br>

<img src="https://www.jeremyjordan.me/content/images/2018/02/Screen-Shot-2018-02-24-at-11.47.09-AM.png" width=600>

</br>

* After alpha is the derivative of cost function with respect to feature(x) weights for theta_1 and derivative of cost function with respect to bias for theta_0.

</br>

## Implementation
___

Linear Regression code consists of three main following functions:
* Fit 
* Predict 
* Score 
### Fit Function
Fit function is used to train our regression model and return the weights and bias.Weights ang bias are first initialised as zero and then passes through the *gradient descent* funtion multiple times to optimize the weights and bias.

### Predict & Score Function
Predict Function - This function returns the predicted y value based on the trained model.

Score Function - This function evaluates the model and return a value between 0-1. Higher the score, more accurate will be the predictions made by the regression model.
