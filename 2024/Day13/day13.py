#!/usr/bin/env python3
import sys
import numpy as np
from pprint import pprint

rows = open(sys.argv[1]).read().strip().split('\n')

for k, n in enumerate([0,10000000000000]):
    cost = np.array([3, 1])
    machines = []
    machine = {}
    for row in rows:
        if row == '':
            machines.append(machine)
            machine = {}
            continue

        a, b = row.split(':')
        x, y = b.split(',')
        try:
            x = int(x.split('+')[1])
            y = int(y.split('+')[1])
        except:
            x = int(x.split('=')[1]) + n
            y = int(y.split('=')[1]) + n
        
        machine[a] = np.array((x, y))
    machines.append(machine)

    def check_integers(array):
        return np.all(np.isclose(array, np.round(array), rtol=1.e-15))

    for i, machine in enumerate(machines):
        A = np.array([machine['Button A'], machine['Button B']]).T
        b = machine['Prize'].T
        X = np.linalg.solve(A, b)
        machines[i]['Score'] = X
        if check_integers(X):
            machines[i]['flag'] = True
            machines[i]['Cost'] = sum(X * cost)
        else:
            machines[i]['flag'] = False

    print(f'Part {k+1}: {int(sum(machine.get('Cost', 0) for machine in machines))}')