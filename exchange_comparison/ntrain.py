import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_inputs = np.array([[2, 2, 1],
                            [1, 1, 1],
                            [1, 2, 1],
                            [2, 1, 1],
                            [2, 2, 2]])

training_outputs = np.array([[0, 1, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weight = 2 * np.random.random((3, 1)) - 1

print('Случайные инициализирующие веса:')
print(synaptic_weight)

# Метод обратного распространения
for i in range(6000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weight))

    err = training_outputs - outputs
    abjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_weight += abjustments

print('Вкса после обучения:')
print(synaptic_weight)

print('Рузультат после обучения:')
print(outputs)

# Test
new_inputs = np.array([1, 2, 2])
outputs = sigmoid(np.dot(new_inputs, synaptic_weight))

print('Тестовые данные:')
print(outputs)
