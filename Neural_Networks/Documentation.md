# Neural Networks
Neural network is a machine learning model which tries to mimic the neurons present in our body, where information in comming from every direction rather than just one in case of conventional models like linear regession, logistic regression, Natural Language Processing,etc. This information is processed by the current perceptron and passed on to next perceptron. This process goes on and on until the output/final layer is reached.

With Neural Networks there is a possibility of complex decision boundaries making it a more efficient non-linear model.

</br>

<img src="https://www.nomidl.com/wp-content/uploads/2022/04/image-6.png" width=400>

</br>

## Perceptron 

A perceptron is like a neuron which collects information from other neurons processes it and then further pass the precocessed information. There can be as many perceptron in each hidden layer and each layer can further have different activation functions. Some can have sigmoid, relu function while others can have any tangential function etc, it is totally up to our choice. But generally we use sigmoid and relu as our activation function.

</br>

<img src="https://media-exp1.licdn.com/dms/image/C5612AQF1JgTTKIHVMw/article-cover_image-shrink_600_2000/0/1520136698297?e=2147483647&v=beta&t=sDN_IxQlI9xMBcywNKtm2wGwd7vbIygye7vgGKAyWV4" width=300>

</br>
The two main operations while implementing neural networks are:
* Forward Propagation - Forward propagation is used to evaluate the result of our model / to make predictions. As the name suggests we move from our input layer to the farthest output layer.
* Backward Propagation - Backward propagation is used to optimize the weights and bias to increase the accuracy of our model. In other terms it is simply implemented to train our neural network.
In contrast to forward propagation we move backwards by pushing the error back to the previous layer and updating the weights along the way.

## Backward Propagation
As told earlier it is used to optimize the weights and bias by pushing the error backwards.The cost function used here can be same as the one used in linear regression.

Generally the cost function used is the mean square error.

</br>
<img src="https://miro.medium.com/max/730/0*MdRLxfy4GbQlv97V." width=300>
</br>
The weights and bias can be optimized using gradient descent by taking the derivative of cost function wrt weights and bias.

</br>

Let the current position of current perceptron be i and the position of next perceptron be j. The derivative of cost function *E* wrt to the weight wij can be broken down using total derivatives.

</br>
<img src="https://i.ibb.co/mSnMZFp/Derivative-of-cost-function.jpg" alt="Derivative-of-cost-function" width=400>

</br>

Here O<sub>j</sub> is the output of the j<sup>th</sup> perceptron and similarly input<sub>j</sub> is the input to the j<sup>th</sup> perceptron.

* Note: input to the j<sup>th</sup> perceptron contains input from all the perceptrons from the previous hidden layer. Let the number of perceptrons in the previous layer be *l*.

    input<sub>j</sub> can be described as :- $$\sum_{k=1}^l  w_{kj} * O_k$$
derivative of input<sub>j</sub> wrt w<sub>ij</sub> gives the following and can be further reduced as:


</br>

<img src="https://i.ibb.co/cytpMKr/derivative-input-by-weight-2.jpg" alt="derivative-input-by-weight-2" width=400> &nbsp; &nbsp; <img src="https://i.ibb.co/W3dFqFZ/derivative-input-by-weight-j.jpg" alt="derivative-input-by-weight-j" width=200>

</br>

The derivative of O<sub>j</sub> wrt to input is equal to the derivative of activation function, which is sigmoid in our case.

The derivative of sigmod is sigmoid(z)(1-sigmoid(z))

</br>

<img src="https://i.ibb.co/gPP4hPD/derivative-output-j-to-input-j.jpg" alt="derivative-output-j-to-input-j" width=400>

</br>

### Now only the derivation of cost function *E* wrt O<sub>j</sub> is left. On solving this two situation arises:

* When j is the output layer perceptrons

    </br>
    <img src="https://i.ibb.co/tLbTQKT/2022-10-03-11-05-pm-Office-Lens.jpg" alt="2022-10-03-11-05-pm-Office-Lens" width=400>

    </br>
    In this case output O<sub>j</sub> becomes equal to y<sub>predicted</sub>.
    
    ,thus the final derivate in case of j as output layer becomes:
    
    </br>

    <img src="https://i.ibb.co/0BrPWPz/2022-10-03-11-06-pm-Office-Lens.jpg" alt="2022-10-03-11-06-pm-Office-Lens" width =400>

</br>

* When j is not the output layer-In this case the output O<sub>j</sub> from the j<sup>th</sup> perceptron does not directly effect the cost function *E*. It first affects the input going to the next hidden layer which again affect the inputs of the next hidden layer and this goes on and on. 

    </br>

    <img src="https://i.ibb.co/TMqwspR/2022-10-03-11-09-pm-Office-Lens.jpg" alt="2022-10-03-11-09-pm-Office-Lens" width=400>
    
    Thus, the derivative of cost *E* wrt to O<sub>j</sub> depending on the incomming inputs to the nxt hidden layer containing *k* perceptrons can be written as-
    
    </br>

    <img src="https://i.ibb.co/wdyPWcp/2022-10-03-11-07-pm-Office-Lens.jpg" alt="2022-10-03-11-07-pm-Office-Lens" width =400> &nbsp; &nbsp; &nbsp; <img src="https://i.ibb.co/r43cn7N/2022-10-03-11-09-pm-Office-Lens-1.jpg" alt="2022-10-03-11-09-pm-Office-Lens-1" width=400>

    here, derivative of *E* wrt input is equal to first two derivative terms in the derivative of *E* wrt O<sub>j+1</sub>. 
    
Thus, if we know the first two derivative terms then we can find the derivatives of the previous layer. Since we can easily find out the first two derivative terms for the farthest layer i.e output layer ,we can pass this error backwards to the previous hidden and find their derivative and again send their error backward and continue this process till the first layer.

This is know as backward propagation as we our propagating backwards to optimize the weights.

</br>

<img src="https://www.i2tutorials.com/wp-content/media/2019/09/Deep-learning-31-i2tutorials.png" width =400>

</br>

## Understanding Code

We have implemented two gates -AND & XOR.
Neural network for AND gate contains a single hidden layer while for XOR we have two hidden layers. Each hidden layer contains two perceptrons in addition to a bias.

* **Fit function** is used to first generate random weights and bias and then by backpropagation optimizing them to increase the accuracy.
This function takes four argumenst-
    * X-inputs
    * Y-y<sub>actual</sub>
    * lr-Learning rate
    * itr-No of iteration to perform backpropagation.

    After optimizing the weights and bias it returns the optimized weights and bias.
*  **Predict function** is used to predict the output by performing forward propagation. It takes the xinputs along with optimized weights and bias generated by fit function as arguments

