import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define inputs and output
dirt = ctrl.Antecedent(np.arange(0, 101, 1), 'dirt')
load = ctrl.Antecedent(np.arange(0, 11, 1), 'load')
time = ctrl.Consequent(np.arange(0, 61, 1), 'time')

# Membership functions
dirt['low'] = fuzz.trimf(dirt.universe, [0, 0, 50])
dirt['high'] = fuzz.trimf(dirt.universe, [30, 100, 100])

load['small'] = fuzz.trimf(load.universe, [0, 0, 5])
load['large'] = fuzz.trimf(load.universe, [3, 10, 10])

time['short'] = fuzz.trimf(time.universe, [0, 0, 30])
time['long'] = fuzz.trimf(time.universe, [20, 60, 60])

# Fuzzy rules
rules = [
    ctrl.Rule(dirt['low'] & load['small'], time['short']),
    ctrl.Rule(dirt['high'] | load['large'], time['long'])
]

# Create fuzzy controller
system = ctrl.ControlSystem(rules)
sim = ctrl.ControlSystemSimulation(system)

# Input values
sim.input['dirt'] = 70
sim.input['load'] = 7

# Fuzzy output
sim.compute()
fuzzy_time = sim.output['time']

# Hybrid adaptive adjustment
adjustment = 1.05
final_time = min(60, fuzzy_time * adjustment)

print("Fuzzy Washing Time:", round(fuzzy_time, 2), "minutes")
print("Hybrid Washing Time:", round(final_time, 2), "minutes")
