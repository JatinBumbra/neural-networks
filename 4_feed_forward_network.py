'''
  FEED FORWARD NETWORK:

  This example is demonstration of feed forward network of 2 neuron layers. The ouput of the 1st layer in the network becomes the
  input of the 2nd layer, and the neurons in each layer have their set of weights and biases.

  NOTE: One common mistake that is most often encountered is regarding the shape of the input matrix and weights which are fed to
        the neural network. If we look closely, for the first layer, the 'inputs' and the 'weights' variables are matrices of 3x4 
        each. 
        Now we know that for dot product of two matrices of size PxQ and MxN each, the required condition is that Q = M, i.e. the number
        of rows of 2nd matrix should be equal to number of columns of 1st matrix and vice versa, for dot product to actually occur.

        Since in this example both the inputs and weights are of 3x4 size, the weights matrices are transposed (in line 36 and 37) to meet
        the dot product condition. Not doing so produces a 'shape' error.

  So in a nutshell, one must take care of the shape of data which is being fed in to the neural network.

'''

import numpy as np

inputs = [[1, 2, 3, 2.5],
          [2.0, 5.0, -1.0, 2.0],
          [-1.5, 2.7, 3.3, -0.8]]

# Weights and biases for neurons of layer 1
weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

# Weights and biases for neurons of layer 2
weights2 = [[0.1, -0.14, 0.5],
            [-0.5, 0.12, -0.33],
            [-0.44, 0.73, -0.13]]
biases2 = [-1, 2, -0.5]

# Calculating output from each layer
layer1_output = np.dot(inputs, np.array(weights).T) + biases
layer2_output = np.dot(layer1_output, np.array(weights2).T) + biases2

print(layer2_output)
