import torch
import torch.nn as nn
import pandas as pd
from torch.utils.data import TensorDataset, DataLoader

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

class Perceptron(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Perceptron, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.Tanh()
        self.fc2 = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        return out

def preprocess(data):
    features = data.iloc[:, :-1].values  
    labels = data.iloc[:, -1].values     
    scaler = StandardScaler()
    features = scaler.fit_transform(features) 
    return torch.tensor(features, dtype=torch.float32), torch.tensor(labels, dtype=torch.float32)


print("Loading data...")
data = pd.read_csv('regression_data/winequality-red.csv', sep=';')
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

print("Preprocessing data...")
train_features, train_labels = preprocess(train_data)
test_features, test_labels = preprocess(test_data)

print("Creating data loaders...")
batch_size = 64
train_loader = DataLoader(TensorDataset(train_features, train_labels), batch_size=batch_size, shuffle=True)
test_loader = DataLoader(TensorDataset(test_features, test_labels), batch_size=batch_size, shuffle=False)




input_size = train_features.shape[1]
print(input_size)
hidden_size = 6


learningRates = [0.1, 0.01, 0.001, 0.0001]
overall_results = []
for i in learningRates:
    results = []
    print(i)
    print("Initializing model...")
    model = Perceptron(input_size, hidden_size)
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=i, momentum=0.5)

    print("Training model...")
    model.eval()
    total_mse = 0
    with torch.no_grad():
        for features, labels in test_loader:
            outputs = model(features)
            mse = criterion(outputs.squeeze(), labels)
            total_mse += mse.item()

    average_mse = total_mse / len(test_loader)
    # print(f"Mean Squared Error on Test Set: {average_mse:.4f}")
    results.append(average_mse)
    num_epochs = 51
    for epoch in range(1, num_epochs):
        model.train()
        for features, labels in train_loader:
            outputs = model(features)
            loss = criterion(outputs.squeeze(), labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        # print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')


        # print("Evaluating model...")
        model.eval()
        total_mse = 0
        with torch.no_grad():
            for features, labels in test_loader:
                outputs = model(features)
                mse = criterion(outputs.squeeze(), labels)
                total_mse += mse.item()

        average_mse = total_mse / len(test_loader)
        # print(f"Mean Squared Error on Test Set: {average_mse:.4f}")
        results.append(average_mse)
    overall_results.append(results)

print(overall_results)
import matplotlib.pyplot as plt


epochs = range(1, num_epochs+1)  

plt.figure(figsize=(10, 6))

for i, lr_results in enumerate(overall_results):
    plt.plot(epochs, lr_results, marker='o', linestyle='-', linewidth=2, markersize=6, label=f'LR={learningRates[i]}')

plt.title('Mean Squared Error over Epochs for Different Learning Rates')
plt.xlabel('Epoch')
plt.ylabel('Mean Squared Error')
plt.xticks(epochs)
plt.grid(True)
plt.legend()

plt.show()