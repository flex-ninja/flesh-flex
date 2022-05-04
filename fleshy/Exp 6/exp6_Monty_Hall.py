# !pip install pomegranate

import numpy as np
from pomegranate import *

guest =DiscreteDistribution({ 'A': 1/3, 'B': 1/3, 'C': 1/3 })
prize =DiscreteDistribution({ 'A': 1/3, 'B': 1/3, 'C': 1/3 })

monty = ConditionalProbabilityTable(
    	[['A', 'A', 'A', 0.0],
     	['A', 'A', 'B', 0.5],
     	['A', 'A', 'C', 0.5],
     	['A', 'B', 'A', 0.0],
     	['A', 'B', 'B', 0.0],
     	['A', 'B', 'C', 1.0],
     	['A', 'C', 'A', 0.0],
     	['A', 'C', 'B', 1.0],
     	['A', 'C', 'C', 0.0],
     	['B', 'A', 'A', 0.0],
     	['B', 'A', 'B', 0.0],
     	['B', 'A', 'C', 1.0],
     	['B', 'B', 'A', 0.5],
     	['B', 'B', 'B', 0.0],
     	['B', 'B', 'C', 0.5],
     	['B', 'C', 'A', 1.0],
     	['B', 'C', 'B', 0.0],
     	['B', 'C', 'C', 0.0],
     	['C', 'A', 'A', 0.0],
     	['C', 'A', 'B', 1.0],
     	['C', 'A', 'C', 0.0],
     	['C', 'B', 'A', 1.0],
     	['C', 'B', 'B', 0.0],
     	['C', 'B', 'C', 0.0],
     	['C', 'C', 'A', 0.5],
     	['C', 'C', 'B', 0.5],
     	['C', 'C', 'C', 0.0]], [guest, prize])

s1 = Node(guest, name="guest")
s2 = Node(prize, name="prize")
s3 = Node(monty, name="monty")

model = BayesianNetwork("Monty Hall")
model.add_states(s1, s2, s3)
model.add_edge(s1, s3)
model.add_edge(s2, s3)
model.bake()

beliefs = model.predict_proba({ 'guest' : 'A' })
for i,b in enumerate(beliefs):
	print(model.states[i].name)
	print(b.parameters) if hasattr(b, 'parameters') else print(b)
	print("")

beliefs = model.predict_proba({ 'guest' : 'A', 'monty' : 'B' })
for i,b in enumerate(beliefs):
	print(model.states[i].name)
	print(b.parameters) if hasattr(b, 'parameters') else print(b)
	print("")


# Aim:
#     To solve the Monty Hall problem using python language.

# Algorithm:
#     1) Run single trial of Monty Hall game problem with or without switching. 
#     2) After the show host reveals a goat & the host knows where car is. 
#     3) Make a switch by changing any other door. 
#     4) Selected one and the one just opened to reveal goat.
#     5) Run trials in iterations with or without switching, returning number 
#     of resulting in winning the car by picking door.