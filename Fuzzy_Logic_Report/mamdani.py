import math
import matplotlib.pyplot as plt
import numpy as np

class Rule: #just support for AND
    def __init__(self):
        self.antecedents = []
        self.consequent = None

    def add_gaussian_antecedent(self, antecedent, value, mu, sigma):
        def gaussian(x):
            exponential = -(x - mu)**2 / (2 * sigma**2)
            return math.exp(exponential)
        self.antecedents.append({ "name": antecedent, "value": value, "membership": gaussian})

    def add_trapezoidal_antecedent(self, antecedent, value, a, b, c, d):
        def trapezoid(x):
            if x < a or x > d:
                return 0
            elif a <= x < b:
                return (x - a) / (b - a)
            elif b <= x <= c:
                return 1
            elif c < x <= d:
                return (d - x) / (d - c)
        self.antecedents.append({ "name": antecedent, "value": value, "membership": trapezoid})

    def add_custom_antecedent(self, antecedent, value, membership_function):
        return self.antecedents.append({ "name": antecedent, "value": value, "membership": membership_function})
    
    def add_gaussian_consequent(self, consequent, value, mu, sigma):
        def gaussian(x):
            exponential = -(x - mu)**2 / (2 * sigma**2)
            return math.exp(exponential)
        self.consequent = { "name": consequent, "value": value, "membership": gaussian}

    def add_trapezoidal_consequent(self, consequent, value, a, b, c, d):
        def trapezoid(x):
            if x < a or x > d:
                return 0
            elif a <= x < b:
                return (x - a) / (b - a)
            elif b <= x <= c:
                return 1
            elif c < x <= d:
                return (d - x) / (d - x)
        self.consequent = { "name": consequent, "value": value, "membership": trapezoid}

    def add_custom_consequent(self, consequent, value, membership_function):
        self.consequent = { "name": consequent, "value": value, "membership": membership_function}

class Mamdani: #just support for AND
    def __init__(self, rules, range, aggregation_method = None, defuzzification_method = None):
        if not isinstance(rules, list):
            raise TypeError("The rules must be a list.")
        if not all(isinstance(rule, Rule) for rule in rules):
            raise TypeError("Each item in rules must be a Rule.")
        if any(len(rule.antecedents) == 0 or rule.consequent == None for rule in rules):
            raise TypeError("Each rule in rules must have atleast one antecedent and a consequent")
        
        self.rules = rules
        self.range = range
        self.aggregation_method = aggregation_method
        self.defuzzification_method = defuzzification_method

        if self.aggregation_method == None: #default = max
            def aggregation(values):
                return max(values)
            self.aggregation_method = aggregation

        if self.defuzzification_method == None:
            self.defuzzification_method = 'centroid'
    
    
    def fuzzify_min_inputs(self, inputs): #fuzzify and apply fuzzy operation of and(min)
        values = []
        for rule in self.rules:
            rule_values = []
            for antecedent in rule.antecedents:
                for input in inputs:
                    if(antecedent["name"] == input["name"]):
                        rule_values.append(antecedent["membership"](input["value"]))
            values.append(min(rule_values))    
        return values
    
    def implication(self, mins):
        functions = []
        for idx, min in enumerate(mins):
            functions.append(self.generate_implication_func(min, idx))
        return functions

    def generate_implication_func(self, min, idx): # hacky way of getting around last value of min being used when calling function
            def implication_func(x):
                output = self.rules[idx].consequent["membership"](x)
                if output > min:
                    return min
                else:
                    return output
            return implication_func

    def aggregation(self, functions):
        start = self.range[0]
        end = self.range[1]
        step = 0.01
        i = start

        aggregated_func_x = []
        aggregated_func_y = []
        while i <= end:
            aggregated_func_x.append(i)
            aggregated_func_y.append(self.aggregation_method([func(i) for func in functions]))
            i += step
        return aggregated_func_x, aggregated_func_y

    def defuzzify(self, y_values, memberships): #centroid
        if self.defuzzification_method == 'centroid':
            weighted = sum([y_values[idx] * memberships[idx] for idx in range(len(y_values))])
            total_membership = sum(memberships)
            
            return weighted / total_membership
        elif self.defuzzification_method == 'max':
            idx = np.argmax(memberships)
            return y_values[idx]

    def make_inference(self, inputs): #inputs is a list of dictionaries in the form of {"name": "x", "value": y}}
        mins = self.fuzzify_min_inputs(inputs)
        individual_functions = self.implication(mins)
        y_values, memberships = self.aggregation(individual_functions)

        # self.plot_membership(y_values, memberships)

        return self.defuzzify(y_values, memberships)
    


    def plot_membership(self, y_values, memberships):
        plt.plot(y_values, memberships, label='Line Function')

        plt.xlabel('Values')
        plt.ylabel('Membership')
        plt.title('Membership vs Values')
        plt.show()
    
    
