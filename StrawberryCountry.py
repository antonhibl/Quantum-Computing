# y0ka1
# Made on July 14th, 2021

''' This is a script to run test-circuits to help me learn quantum computing, it will not have a certian structured circuit, 
    rather I will be testing many circuits so this will be constantly running while I run the code from a seperate terminal. '''

import qiskit
import strawberryfields as sf
import pennylane

from strawberryfields import ops

# Creating a 3-mode quantum program
prog = sf.Program(3)

with prog.context as q:
    ops.Sgate(0.54) | q[0]
    ops.Sgate(0.54) | q[1]
    ops.Sgate(0.54) | q[2]
    ops.BSgate(0.43, 0.1) | (q[0], q[2])
    ops.BSgate(0.43, 0.1) | (q[1], q[2])
    ops.MeasureFock() | q

