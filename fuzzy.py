import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define inputs and output
dirt = ctrl.Antecedent(np.arange(0, 101, 1), 'dirt')
grease = ctrl.Antecedent(np.arange(0, 101, 1), 'grease')
time = ctrl.Consequent(np.arange(0, 61, 1), 'time')

# Membership functions
for var in [dirt, grease]:
    var['low'] = fuzz.trimf(var.universe, [0, 0, 50])
    var['medium'] = fuzz.trimf(var.universe, [0, 50, 100])
    var['high'] = fuzz.trimf(var.universe, [50, 100, 100])

time['short'] = fuzz.trimf(time.universe, [0, 0, 30])
time['medium'] = fuzz.trimf(time.universe, [15, 30, 45])
time['long'] = fuzz.trimf(time.universe, [30, 60, 60])

# Fuzzy rules
rules = [
    ctrl.Rule(dirt['low'] & grease['low'], time['short']),
    ctrl.Rule(dirt['medium'] | grease['medium'], time['medium']),
    ctrl.Rule(dirt['high'] | grease['high'], time['long'])
]

# Create controller
system = ctrl.ControlSystem(rules)
washing = ctrl.ControlSystemSimulation(system)

# Input values
washing.input['dirt'] = 70
washing.input['grease'] = 60

# Calculate washing time
washing.compute()
print("Washing Time:", round(washing.output['time'], 2), "minutes")
