
import numpy as np
from LearningLibrary.Train import train
from LearningLibrary.neuralnet import NeuralNet
from LearningLibrary.layers import Linear, Tanh

inputs = np.array([
    [0,0],
    [1,0],
    [0,1],
    [1,1]
])

targets = np.array([
    [1,0],
    [0,1],
    [0,1],
    [1,0]
])

net = NeuralNet([
    Linear(input_size=2, output_size=2),
    Tanh(),
    Linear(input_size=2, output_size=2)
])

train(net, inputs, targets)

for x, y in zip(inputs, targets):
    predicted = net.forward(x)
    print(x, predicted, y)