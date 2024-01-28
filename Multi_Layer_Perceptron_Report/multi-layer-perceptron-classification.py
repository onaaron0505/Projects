import torchvision.transforms as transforms
import torch
import torch.nn as nn
import pandas as pd
from torch.utils.data import TensorDataset, DataLoader
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Define the multi-layer perceptron model
class Perceptron(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(Perceptron, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

def preprocess(data):
    labels = data.iloc[:, 0].values
    features = data.iloc[:, 1:].values / 255.0  # Normalize pixel values
    # threshold = np.where(features >=0.4, 1, 0)
    return torch.tensor(features, dtype=torch.float32), torch.tensor(labels, dtype=torch.int64)

print("Loading data...")
train_data = pd.read_csv('classification_data/mnist_train.csv')
test_data = pd.read_csv('classification_data/mnist_test.csv')

print("Preprocessing data...")
train_images, train_labels = preprocess(train_data)
test_images, test_labels = preprocess(test_data)

print("Creating data loaders...")
train_loader = DataLoader(TensorDataset(train_images, train_labels), batch_size=100, shuffle=True)
test_loader = DataLoader(TensorDataset(test_images, test_labels), batch_size=100, shuffle=False)




input_size = 784
hidden_size = 256
output_size = 10

accuracies = np.array([])
errors = np.array([])
i = 51

print("Initializing model...")
model = Perceptron(input_size, hidden_size, output_size)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01, momentum=0.5)


print("Training model...")

num_epochs = i

for epoch in range(1, num_epochs):
    model.train()
    for images, labels in train_loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')
    errors = np.append(errors, loss.item())

    print("Evaluating model...")
    model.eval()

    actuals = []
    predictions = []

    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            _, predicted = torch.max(outputs, 1)
            actuals.extend(labels.view_as(predicted)) 
            predictions.extend(predicted)  

    actuals = torch.tensor(actuals)
    predictions = torch.tensor(predictions)

    conf_matrix = confusion_matrix(actuals.numpy(), predictions.numpy())
    print(conf_matrix)
    accuracy = np.trace(conf_matrix) / np.sum(conf_matrix)
    print(f"Accuracy: {accuracy:.4f}")
    accuracies = np.append(accuracies, accuracy)
    print(accuracies)


epochs = np.array(range(1, num_epochs))
plt.figure(figsize=(10, 6))
plt.plot(epochs, accuracies, marker='o', color='b', linestyle='-', linewidth=2, markersize=6, label='Accuracy')
plt.title('Model Accuracy over Different Epochs')
plt.xlabel('Epochs')
plt.ylabel('Value')
plt.xticks(epochs)  
plt.grid(True)
plt.legend()
plt.show()

