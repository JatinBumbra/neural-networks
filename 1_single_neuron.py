'''
    A SIMPLE NEURON:

    Simply put, a neuron basically takes 'inputs' which have 'weights' assigned to them, and each weight determines
    how much effect will that input have on the output of the nueron.

    Now each neuron has a bias associated with itself, which determines the value at which the neuron will come into play.

    You can basically imagine bias as the threshold of the neuron. Only after an input*weight reaches a certain threshold
    (determined by the bias) will the neuron will actually come into play. Rest of the time, for values below threshold,
    the neuron will remain dormant and will not contribute to the final output.

    FOR PEOPLE FAMILIAR WITH THE PHOTOELECTRIC EFFECT, we know that an electron is ejected only when that electron acquires 
    enough energy(imparted to it by the photons) to overcome the threshold frequency. Similar is the concept of neurons we can say.

    This concept of bias becomes more clear when we actually encounter an activation function.
    For now, just simply know what a bias is.
'''

inputs = [1, 2, 3]

weights = [0.2, 0.8, -0.5]
bias = 2

output = inputs[0]*weights[0] + inputs[1] * \
    weights[1] + inputs[2]*weights[2] + bias
print(output)