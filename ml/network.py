__author__ = 'talmid'
import random
import math

class Network(object):

    """
    Create a neural network
    Parameters:
        layers - a list of the number of neurons for the corresponding layer (example: [2, 1, 3] has two neurons in the
        first layer, one in the second and three in the third)
    """
    def __init__(self, layers):
        self.layers = layers
        self.num_layers = len(layers)
        self.weights = []
        self.biases = []

        # Initialize Weights:
        # Three dimensional list: layers (except for first layer), for each layer neurons, for each neuron
        # connections (previous layer's neurons).
        for layer in xrange(1, self.num_layers):
            self.weights.append([])
            for neuron in xrange(0, self.layers[layer]):
                self.weights[layer-1].append([])
                for connection in xrange(0, self.layers[layer-1]):
                    self.weights[layer-1][neuron].append(random_float(-3, 3))

        # Initialize Biases:
        # Two dimensional list: layers (except for first layer), for each layer neurons
        for layer in xrange(1, self.num_layers):
            self.biases.append([])
            for neuron in xrange(0, self.layers[layer]):
                self.biases[layer-1].append(random_float(-3, 3))

    """
    Make the network learning according to a data set
    Parameters:
        data_set - List of tuples: (input, expected output)
        learning_speed - Changes the learning speed - lower means less change and less possible mistakes,
                         bigger means faster learning but more room for error (has to be positive)
        batch_size - Default 20, control the size of the batches.
    """
    def learn(self, data_set, learning_speed, batch_size=20):
        formatted_batch = ([], [])
        for element in data_set:
            formatted_batch[0].append(element[0])
            formatted_batch[1].append(element[1])
        for x in xrange(0, len(data_set) / batch_size):
            cur_batch = (formatted_batch[0][x*batch_size : x*batch_size+batch_size],
                         formatted_batch[1][x*batch_size : x*batch_size+batch_size])
            self.update_batch(cur_batch, learning_speed)

    """
    Update the network according to a batch and a learning speed (learns)
    Parameters:
        batch - Tuple of lists: (list of inputs, list of corresponding expected outputs)
        learning_speed - Changes the learning speed - lower means less change and less possible mistakes,
                         bigger means faster learning but more room for error (has to be positive)
    """
    def update_batch(self, batch, learning_speed):
        inputs = batch[0]
        expected_outputs = batch[1]
        # These two will be the values of the derivatives and not the derivative function (slopes).
        weight_derivative_sum = self.zeroes_weight_shape()
        bias_derivative_sum = self.zeroes_bias_shape()

        # For each input and its corresponding output, calculate the value of the derivative (slope) for every weight
        # and bias and add it for averaging later.
        for inp, expected in zip(inputs, expected_outputs):
            weighted_inputs, activations = self.feedforward(inp)
            weight_derivatives, bias_derivatives = self.backpropogation(weighted_inputs, activations, expected)
            for layer in xrange(1, self.num_layers):
                list_addition(bias_derivative_sum[layer - 1], bias_derivatives[layer - 1])
                for neuron in xrange(0, self.layers[layer]):
                    list_addition(weight_derivative_sum[layer - 1][neuron], weight_derivatives[layer - 1][neuron])

        # Average the slopes for each bias and weight, multiplied by -1 to decrease the cost function (thanks math)
        for layer in xrange(1, self.num_layers):
            list_scalar_multiplication(bias_derivative_sum[layer - 1], -(1 / float(len(batch[0]))) * learning_speed)
            for neuron in xrange(0, self.layers[layer]):
                list_scalar_multiplication(weight_derivative_sum[layer - 1][neuron],
                                           -(1 / float(len(batch[0]))) * learning_speed)

        # Add the deltas
        self.update_weights(weight_derivative_sum)
        self.update_biases(bias_derivative_sum)

    """
    Calculate the activations and inputs on all the neurons in the network
    Parameters:
        inp - list of input neurons
    Return value:
        Tuple of two lists: neuron weighted and biased inputs and neuron activations. Both are two dimensional lists:
        layers (except the first layer in the inputs list), for each layer neurons.
    """
    def feedforward(self, inp):
        activations = [inp]
        weighted_inputs = []
        # Loop over all neurons in the network
        for layer in xrange(1, self.num_layers):
            activations.append([])
            weighted_inputs.append([])
            for neuron in xrange(0, self.layers[layer]):
                activations[layer].append(0)
                weighted_inputs[layer - 1].append(0)
                weighted_input = 0
                # Multiply each neuron from the last layer by its corresponding connection weight to the current neuron
                # and sum them up
                weighted_sum = 0
                for connection in xrange(0, self.layers[layer-1]):
                    weighted_sum += activations[layer - 1][connection] * self.weights[layer - 1][neuron][connection]
                # Add weighted sum to the weighted input
                weighted_input += weighted_sum
                # Add bias to the weighted input
                weighted_input += self.biases[layer - 1][neuron]
                weighted_inputs[layer-1][neuron] = weighted_input
                # Apply activation function
                activations[layer][neuron] = sigmoid(weighted_input)
        return (weighted_inputs, activations)


    def backpropogation(self, weighted_inputs, activations, expected):
        cost_derivatives = self.zeroes_bias_shape()
        weight_derivatives = self.zeroes_weight_shape()
        bias_derivatives = self.zeroes_bias_shape()

        for neuron in xrange(0, self.layers[-1]):
            cost_derivative = self.cost_derivative(activations[-1][neuron], expected[neuron], weighted_inputs[-1][neuron])
            cost_derivatives[-1][neuron] = cost_derivative
            bias_derivatives[-1][neuron] = cost_derivative
            for connection in xrange(0, self.layers[-2]):
                weight_derivatives[-1][neuron][connection] = cost_derivative * activations[-2][connection]

        for layer in xrange(self.num_layers - 2, 0, -1):
            for neuron in xrange(0, self.layers[layer]):
                cost_derivative = 0
                for neuron_next in xrange(0, self.layers[layer+1]):
                    cost_derivative += cost_derivatives[layer][neuron_next] * self.weights[layer][neuron_next][neuron]
                cost_derivatives[layer-1][neuron] = cost_derivative * sigmoid_derivative(weighted_inputs[layer-1][neuron])
                bias_derivatives[layer-1][neuron] = cost_derivatives[layer-1][neuron]
                for connection in xrange(0, self.layers[layer-1]):
                    weight_derivatives[layer-1][neuron][connection] = cost_derivatives[layer-1][neuron] * activations[layer-1][connection]

        return (weight_derivatives, bias_derivatives)

    def update_weights(self, delta):
        for layer in xrange(1, self.num_layers):
            for neuron in xrange(0, self.layers[layer]):
                list_addition(self.weights[layer-1][neuron], delta[layer-1][neuron])

    def update_biases(self, delta):
        for layer in xrange(1, self.num_layers):
            list_addition(self.biases[layer-1], delta[layer-1])

    def cost_function(self, activation, expected):
        return 0.5 * math.pow(expected - activation, 2)

    def cost_derivative(self, activation, expected, weighted_input):
        return (activation - expected) * sigmoid_derivative(weighted_input)

    def zeroes_bias_shape(self):
        biases = []
        for layer in xrange(1, self.num_layers):
            biases.append([])
            for neuron in xrange(0, self.layers[layer]):
                biases[layer-1].append(0)
        return biases

    def zeroes_weight_shape(self):
        weights = []
        for layer in xrange(1, self.num_layers):
            weights.append([])
            for neuron in xrange(0, self.layers[layer]):
                weights[layer-1].append([])
                for connection in xrange(0, self.layers[layer-1]):
                    weights[layer-1][neuron].append(0)
        return weights


def list_addition(add_to, add_what):
    for x in xrange(0, len(add_to)):
        add_to[x] += add_what[x]

def list_scalar_multiplication(multiply_what, multiply_by):
    for x in xrange(0, len(multiply_what)):
        multiply_what[x] *= multiply_by

def list_multiplication(multiply_what, multiply_by):
    for x in xrange(0, len(multiply_what)):
        multiply_what[x] *= multiply_by[x]

def sigmoid(x):
    return 1/(1+math.exp(-x))


def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))


def random_float(mini, maxi):
    return (random.random() * (maxi-mini)) + mini


def main():
    batch1 = ([], [])
    for x in xrange(0, 2):
        for y in xrange(0, 20):
            batch1[0].append([random_float(-50, 50), random_float(-50, 50), random_float(-50, 50)])
            batch1[1].append([0.5, 0.5])
    net = Network([3, 3, 2])
    print net.feedforward(batch1[0][0])[1][-1]
    set = []
    for x in xrange(0, 100000):
        set.append(([random_float(-50, 50), random_float(-50, 50), random_float(-50, 50)],
                    [0.5, 0.5]))
    net.learn(set, 1)
    print net.biases[-1]
    print net.weights[-1]
    print net.feedforward(batch1[0][0])[1][-1]

if __name__ == '__main__':
    main()
