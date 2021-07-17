# y0ka1
# July 16th, 2021

from pyquil import get_qc, Program
from pyquil.gates import CNOT, Z, MEASURE, H
from pyquil.api import local_forest_runtime
from pyquil.quilbase import Declare

local_forest_runtime()

# defining my first quil program
prog = Program(
    Declare("ro", "BIT", 2),
    Z(1),
    CNOT(1, 0),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(10)

# runs the first program
with local_forest_runtime():
    qvm = get_qc('9q-square-qvm')
    bitstrings = qvm.run(qvm.compile(prog)).readout_data.get("ro")

# construct a Bell State program
prog2 = Program(
    Declare("ro", "BIT", 2),
    H(0),
    CNOT(0, 1),
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(10)

# run the first program on a QVM
qc = get_qc('9q-square-qvm')
result = qc.run(qc.compile(prog2)).readout_data.get("ro")
print(result[0])
print(result[1])

