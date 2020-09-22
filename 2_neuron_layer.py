'''
    SIMPLE NEURON LAYER:

    This example is a demonstration of a single neuron layer composed of 3 neurons. Each neuron has it's own weights that it
    assigns to its inputs, and the neuron itself has a bias. Based on these values, each neuron operates on the input vector
    and produces the output.

    The below program demonstrates the ouput of a layer.

    NOTE: This example does not combine the result into a single value, like the final output layer which has one 
          output(in simplest case)
'''

inputs = [1, 2, 3, 2.5]

weights1 = [0.2, 0.8, -0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [inputs[0]*weights1[0] + inputs[1] * weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
          inputs[0]*weights2[0] + inputs[1] * weights2[1] +
          inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
          inputs[0]*weights3[0] + inputs[1] * weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3, ]
print(output)