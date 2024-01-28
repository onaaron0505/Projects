from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from mamdani import Mamdani, Rule

iris = datasets.load_iris()

train_samples = 105
test_samples = len(iris.data) - train_samples
print(test_samples)
x_train, x_test, y_train, y_test = train_test_split(iris.data[:, :], iris.target, train_size=train_samples, random_state=42)

# plt.figure(figsize=(12, 4))
# plt.suptitle('Features')
# plt.subplots_adjust(wspace=0.4, bottom=0.33)

# plt.subplot(1, 4, 1)
# plt.scatter(x_train[:, 0], range(train_samples), c=y_train)
# plt.xlabel(iris.feature_names[0])
# plt.ylabel("Sample Number")

# plt.subplot(1, 4, 2)
# plt.scatter(x_train[:, 1], range(train_samples), c=y_train)
# plt.xlabel(iris.feature_names[1])
# plt.ylabel("Sample Number")

# plt.subplot(1, 4, 3)
# plt.scatter(x_train[:, 2], range(train_samples), c=y_train)
# plt.xlabel(iris.feature_names[2])
# plt.ylabel("Sample Number")

# plt.subplot(1, 4, 4)
# sc = plt.scatter(x_train[:, 3], range(train_samples), c=y_train)
# plt.xlabel(iris.feature_names[3])
# plt.ylabel("Sample Number")
# # plt.legend(labels=[iris.target_names[0], iris.target_names[1], iris.target_names[2]], loc='upper right')
# plt.figlegend(handles=sc.legend_elements()[0], labels=[iris.target_names[0], iris.target_names[1], iris.target_names[2]], loc='lower center')

mu = []
sigma = []


targets = np.unique(y_train)
for target in targets:
    idx = np.where(y_train == target)
    target_data = np.transpose(x_train[idx])
    target_mu = []
    target_sigma = []
    for row in target_data:
        target_mu.append(np.average(row))
        target_sigma.append(np.std(row))
    mu.append(target_mu)
    sigma.append(target_sigma)

print(np.matrix(mu))
print(np.matrix(sigma))

plt.show()

rules = []

def class0(x):
    return 1 if round(x, 2) == 0 else 0

def class1(x):
    return 1 if round(x, 2) == 1 else 0  

def class2(x):
    return 1 if round(x, 2) == 2 else 0

# # petal width
rule1 = Rule()
rule1.add_trapezoidal_antecedent("petal width", "small", 0, 0, 0.5, 0.8)
rule1.add_custom_consequent("target", iris.target_names[0], class0)
rules.append(rule1)

rule2 = Rule()
rule2.add_gaussian_antecedent("petal width", "medium", mu[1][3], sigma[1][3])
rule2.add_custom_consequent("target", iris.target_names[1], class1)
rules.append(rule2)

rule3 = Rule()
rule3.add_gaussian_antecedent("petal width", "large", mu[2][3], sigma[2][3])
rule3.add_custom_consequent("target", iris.target_names[2], class2)
rules.append(rule3)

# petal length
# rule1 = Rule()
# rule1.add_trapezoidal_antecedent("petal length", "small", 0, 0, 2, 2.5)
# rule1.add_custom_consequent("target", iris.target_names[0], class0)
# rules.append(rule1)

# rule2 = Rule()
# rule2.add_gaussian_antecedent("petal length", "medium", mu[1][2], sigma[1][2])
# rule2.add_custom_consequent("target", iris.target_names[1], class1)
# rules.append(rule2)

# rule3 = Rule()
# rule3.add_gaussian_antecedent("petal length", "large", mu[2][2], sigma[2][2])
# rule3.add_custom_consequent("target", iris.target_names[2], class2)
# rules.append(rule3)


fis = Mamdani(rules, [0, 3], defuzzification_method='max')

confusion_matrix = np.zeros([3,3])

# using test data
# for i in range(len(x_test)):
#     # inputs = [{"name": "petal width", "value": x_test[i, 3]}]
#     inputs = [{"name": "petal length", "value": x_test[i, 2]}]
#     # inputs = [{"name": "petal width", "value": x_test[i, 3]}, {"name": "petal length", "value": x_test[i, 2]}]
#     output = fis.make_inference(inputs)
#     confusion_matrix[y_test[i], round(output)] += 1 

# using all data
for i in range(len(iris.data)):
    inputs = [{"name": "petal width", "value": iris.data[i, 3]}]
    # inputs = [{"name": "petal length", "value": iris.data[i, 2]}]
    # inputs = [{"name": "petal width", "value": iris.data[i, 3]}, {"name": "petal length", "value": iris.data[i, 2]}]
    output = fis.make_inference(inputs)
    confusion_matrix[iris.target[i], round(output)] += 1 

print(confusion_matrix)
