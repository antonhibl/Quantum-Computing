# necessary pyquil modules
import pyquil
from pyquil import get_qc, Program
from pyquil.gates import *
from pyquil.api import local_forest_runtime
from pyquil.quilbase import Declare
import numpy as np

# Defining a circuit to run
quantumprog = Program(
        Declare("ro", "BIT", 2),    # This declares a classical register named ro with 4 bits to measure qubits with
        RX( np.pi/4, 0),            
        Z(0),
        H(0), 
        H(1),
        MEASURE(0, ("ro", 0)),
        MEASURE(1, ("ro", 1)),
        ).wrap_in_numshots_loop(10)


# returning my circuit parameterizations and metrics
print("=====================================================\n")
print("CIRCUIT DEFINITIONS:")
print(quantumprog)
print("=====================================================\n")

# run the program on a QVM
qc = get_qc('9q-square-qvm')
result = qc.run(qc.compile(quantumprog)).readout_data.get("ro")

# return the results
print("Results:")
print(result)

