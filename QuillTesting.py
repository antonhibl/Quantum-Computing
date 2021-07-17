# y0ka1
# July 16th, 2021

from pyquil import get_qc, Program
from pyquil.gates import *
from pyquil.api import local_forest_runtime
from pyquil.quilbase import Declare


# Defining my quantum program
quantumprog = Program(
        Declare("ro", "BIT", 2),    # This declares a classical register named ro with 2 bits to measure qubits with
        H(0),               # places my first bit into a state of super position between states |0> and |1>
        CNOT(0, 1),         # This entangles the two bits into a connected super position
        X(1),               # Because I have entangled these qubits I can apply X to their linear combo
        MEASURE(0, ("ro", 0)),
        MEASURE(1, ("ro", 1))
        ).wrap_in_numshots_loop(10)

# Defining a second program
quantumprog2 = Program(
        Declare("co", "BIT", 2),
        H(0),
        CNOT(0,  1),
        Z(0),
        X(0),
        MEASURE(0, ("co", 0)),
        MEASURE(1, ("co", 1))
        ).wrap_in_numshots_loop(10)

# returning my circuit parameterizations and metrics
print("============================================================================")
print("CIRCUIT DEFINITIONS:")
print(quantumprog)
print("============================================================================")

# run the program on a QVM
qc = get_qc('9q-square-qvm')
result = qc.run(qc.compile(quantumprog)).readout_data.get("ro")
result2 = qc.run(qc.compile(quantumprog2)).readout_data.get("co")

# return the results
print(result[0])
print(result[1])

print(result2[0])
print(result2[1])
