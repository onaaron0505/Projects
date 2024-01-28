from mamdani import Mamdani, Rule
import numpy as np
import matplotlib.pyplot as plt

###Service Example
rules = []

rule1 = Rule()
rule1.add_trapezoidal_antecedent("Service", "Poor",0, 0, 1, 4)
rule1.add_trapezoidal_antecedent("Food", "Rancid", 0, 0, 1, 4)
rule1.add_gaussian_consequent("Tip", "Low", 5, 3)
rules.append(rule1)

rule2 = Rule()
rule2.add_gaussian_antecedent("Service", "Ok", 4, 2)
rule2.add_gaussian_antecedent("Food", "Ok", 4, 2)
rule2.add_gaussian_consequent("Tip", "Medium", 16, 3)
rules.append(rule2)


rule3 = Rule()
rule3.add_gaussian_antecedent("Service", "Great", 7, 2)
rule3.add_gaussian_antecedent("Food", "Great", 7, 2)
rule3.add_trapezoidal_consequent("Tip", "Good", 20, 21, 24, 25)
rules.append(rule3)

rule4 = Rule()

rule4.add_trapezoidal_antecedent("Service", "Esquiste", 8, 9, 10, 10)
rule4.add_trapezoidal_antecedent("Food", "Esquiste", 8, 9, 10, 10)
rule4.add_trapezoidal_consequent("Tip", "Generous", 25, 26, 30, 30)
rules.append(rule4)

x = x = np.linspace(0, 10, 400)
conesquentx = np.linspace(0, 30, 400)

y11 = [rule1.antecedents[0]["membership"](value) for value in x]
y12 = [rule1.antecedents[1]["membership"](value) for value in x]
y13 = [rule1.consequent["membership"](value) for value in conesquentx]

y21 = [rule2.antecedents[0]["membership"](value) for value in x]
y22 = [rule2.antecedents[1]["membership"](value) for value in x]
y23 = [rule2.consequent["membership"](value) for value in conesquentx]

y31 = [rule3.antecedents[0]["membership"](value) for value in x]
y32 = [rule3.antecedents[1]["membership"](value) for value in x]
y33 = [rule3.consequent["membership"](value) for value in conesquentx]


y41 = [rule4.antecedents[0]["membership"](value) for value in x]
y42 = [rule4.antecedents[1]["membership"](value) for value in x]
y43 = [rule4.consequent["membership"](value) for value in conesquentx]


# plt.plot(x, y11, label='poor')
# plt.plot(x, y21, label='ok')
# plt.plot(x, y31, label='great')
# plt.plot(x, y41, label='exquisite')

# plt.title('Service')
# plt.xlabel('rating')
# plt.ylabel('membership')

# plt.legend()

# plt.show()

# plt.plot(x, y12, label='rancid')
# plt.plot(x, y22, label='ok')
# plt.plot(x, y32, label='great')
# plt.plot(x, y42, label='exquisite')

# plt.title('Food')
# plt.xlabel('rating')
# plt.ylabel('membership')

# plt.legend()

# plt.show()

# plt.plot(conesquentx, y13, label='low')
# plt.plot(conesquentx, y23, label='medium')
# plt.plot(conesquentx, y33, label='good')
# plt.plot(conesquentx, y43, label='generous')

# plt.title('Tip')
# plt.xlabel('amount')
# plt.ylabel('membership')

# plt.legend()

# plt.show()


inferences = []
fis = Mamdani(rules, [0,30])

inputs = [{"name": "Service", "value": 6}, {"name": "Food", "value": 4}]
mins = fis.fuzzify_min_inputs(inputs)
individual_functions = fis.implication(mins)
y_values, memberships = fis.aggregation(individual_functions)

print(mins)

y1 = [individual_functions[0](value) for value in conesquentx]
y2 = [individual_functions[1](value) for value in conesquentx]
y3 = [individual_functions[2](value) for value in conesquentx]
y4 = [individual_functions[3](value) for value in conesquentx]


plt.plot(conesquentx, y1, label='poor')
plt.plot(conesquentx, y2, label='ok')
plt.plot(conesquentx, y3, label='great')
plt.plot(conesquentx, y4, label='exquisite')

plt.title('Tip')
plt.xlabel('amount')
plt.ylabel('membership')

plt.legend()

plt.show()

fis.plot_membership(y_values, memberships)
print(fis.defuzzify(y_values, memberships))


for i in range(10):
    i_values = []
    for j in range(10):      
        inputs = [{"name": "Service", "value": i}, {"name": "Food", "value": j}]
        inference = fis.make_inference(inputs)
        i_values.append(round(inference, 2))
    inferences.append(i_values)
print(np.matrix(inferences))


