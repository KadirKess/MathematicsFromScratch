# Import
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import matplotlib.pyplot as plt
import time
from NaturalNumbers import NaturalNumbers
import numpy as np

# Function to time the mean value of a function
def time_function(func, *args, num_trials=50):
    times = []
    for _ in range(num_trials):
        start = time.time()
        func(*args)
        end = time.time()
        times.append(end - start)
    return np.mean(times)

# Test ranges
test_range = list(range(1, 60))

# Time lists for custom NaturalNumbers class methods and built-in operations
time_custom = {'add': [], 'sub': [], 'mul': [], 'pow': [], 'div': [], 'mod': []}
time_builtin = {'add': [], 'sub': [], 'mul': [], 'pow': [], 'div': [], 'mod': []}

# Populate the time lists
for i in test_range:
    custom_n1 = NaturalNumbers(i)
    custom_n2 = NaturalNumbers(max(1, i // 2))
    builtin_n1 = i
    builtin_n2 = max(1, i // 2)

    # Time the custom NaturalNumbers class operations
    for op in time_custom:
        if op == 'add':
            time_custom[op].append(time_function(custom_n1.__add__, custom_n2))
        elif op == 'sub':
            time_custom[op].append(time_function(custom_n1.__sub__, custom_n2))
        elif op == 'mul':
            time_custom[op].append(time_function(custom_n1.__mul__, custom_n2))
        elif op == 'div':
            time_custom[op].append(time_function(custom_n1.__truediv__, custom_n2))
        elif op == 'mod':
            time_custom[op].append(time_function(custom_n1.__mod__, custom_n2))
        elif op == 'pow':
            time_custom[op].append(time_function(custom_n1.__pow__, NaturalNumbers(2)))

    # Time the built-in operations
    for op in time_builtin:
        if op == 'add':
            time_builtin[op].append(time_function(lambda x, y: x + y, builtin_n1, builtin_n2))
        elif op == 'sub':
            time_builtin[op].append(time_function(lambda x, y: x - y, builtin_n1, builtin_n2))
        elif op == 'mul':
            time_builtin[op].append(time_function(lambda x, y: x * y, builtin_n1, builtin_n2))
        elif op == 'div':
            time_builtin[op].append(time_function(lambda x, y: x // y, builtin_n1, builtin_n2))
        elif op == 'mod':
            time_builtin[op].append(time_function(lambda x, y: x % y, builtin_n1, builtin_n2))
        elif op == 'pow':
            time_builtin[op].append(time_function(lambda x: x ** 2, builtin_n1))

# Plot the results
plt.figure(figsize=(15, 10))
subplot_titles = ['Addition', 'Subtraction', 'Multiplication', 'Power of 2', 'Division', 'Modulo']
for idx, op in enumerate(time_custom):
    plt.subplot(3, 2, idx + 1)
    plt.plot(test_range, time_custom[op], label=f'Custom {op.capitalize()}')
    plt.plot(test_range, time_builtin[op], label=f'Built-in {op.capitalize()}')
    plt.xlabel('Number')
    plt.ylabel('Time (seconds)')
    plt.title(f'{subplot_titles[idx]} Time Complexity')
    plt.legend()

plt.tight_layout()
plt.show()