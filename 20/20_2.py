#!/usr/bin/env python

"""
The final machine responsible for moving the sand down to Island Island has a module attached named rx. The machine turns on when a single low pulse is sent to rx.

Reset all modules to their default states. Waiting for all pulses to be fully handled after each button press, what is the fewest number of button presses required to deliver a single low pulse to the module named rx?

"""

class Flip_flop():
	def __init__(self, name, children):
		self.name = name
		self.children = children
		self.state = False

	def pulse(self, pulse, name):
		if pulse == 'low':
			return self.low_pulse(name)
		return self.high_pulse(name)

	def low_pulse(self, name=''):
		if self.state:
			self.state = not self.state
			return [(child, 'low', self.name) for child in self.children]
		else: 
			self.state = not self.state
			return [(child, 'high', self.name) for child in self.children]

	def high_pulse(self, name=''):
		return []

class Conjunction():
	def __init__(self, name, children):
		self.name = name
		self.children = children
		self.state = {}

	def pulse(self, pulse, name):
		if pulse == 'low':
			return self.low_pulse(name)
		return self.high_pulse(name)

	def low_pulse(self, name=''):
		self.state[name] = 'low'
		return self.send_pulse()

	def high_pulse(self, name=''):
		self.state[name] = 'high'
		return self.send_pulse()

	def send_pulse(self):
		if 'low' not in self.state.values():
			return [(child, 'low', self.name) for child in self.children]
		else:
			return [(child, 'high', self.name) for child in self.children]

class Broadcaster():
	def __init__(self, children):
		self.name = 'broadcaster'
		self.children = children

	def pulse(self, pulse, name):
		if pulse == 'low':
			return self.low_pulse(name)
		return self.high_pulse(name)

	def low_pulse(self, name=''):
		return [(child, 'low', self.name) for child in self.children]

	def high_pulse(self, name=''):
		return [(child, 'high', self.name) for child in self.children]

class Button():
	def __init__(self):
		self.children = []

	def push(self):
		return [('broadcaster', 'low', 'button')]

def push_button(modules):
	pulses_queue = modules['button'].push()
	to_return = []
	while len(pulses_queue) > 0:
		pulse = pulses_queue.pop(0)
		#print(pulse)
		if pulse[0] == 'ft' and pulse[1] == 'high':
			to_return += [pulse[2]]

		if pulse[0] != 'rx':
			new_pulses = modules[pulse[0]].pulse(pulse[1],pulse[2])
			pulses_queue += new_pulses
	return to_return

def setup(lines):
	modules = {}
	con_mod = []
	for line in lines:
		if line[0] == '%':
			modules[line[1:3]] = Flip_flop(line[1:3], line[7:].split(', '))
		elif line[0] == '&':
			modules[line[1:3]] = Conjunction(line[1:3], line[7:].split(', '))
			con_mod += [line[1:3]]
		else:
			modules['broadcaster'] = Broadcaster(line[line.index('>') + 2:].split(', '))

	modules['button'] = Button()
	#initialize con_module
	for mod in con_mod:
		for module in modules.values():
			if mod in module.children:
				modules[mod].state[module.name] = 'low'

	return modules

with open('input','r') as f:
	lines = f.read().splitlines()

modules = setup(lines)


#There's gonna be a cycle somewhere
rx_parent = [line[1:3] for line in lines if 'rx' in line][0]
rx_parent_parent = set([line[1:3] for line in lines if rx_parent in line and 'rx' not in line])

i = 1
cycle = {}
while rx_parent_parent != set(cycle.keys()):
	new_cycles = push_button(modules)
	for new_cycle in new_cycles:
		if new_cycle not in cycle:
			cycle[new_cycle] = i
	i += 1


import numpy as np
print(np.lcm.reduce(list(cycle.values())))
