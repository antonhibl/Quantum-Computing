# y0ka1
# July 17th, 2021

''' This program is for learning some pyquil code mechanics and testing some quantum circuits. '''

# necessary pyquil modules
import pyquil
from pyquil import get_qc, Program
from pyquil.gates import *
from pyquil.api import local_forest_runtime
from pyquil.quilbase import Declare

# altair for plotting
import altair as alt

# Data science packages
import numpy as np
import pandas as pd
import matplotlib as mpl
import thewalrus

# Defining a circuit to run
quantumprog = Program(
        Declare("ro", "BIT", 4),    # This declares a classical register named ro with 4 bits to measure qubits with
        H(0),            
        CNOT(0, 1),
        CNOT(0, 2),
        CNOT(0, 3),
        CCNOT (1, 2, 3),             
        MEASURE(0, ("ro", 0)),
        MEASURE(1, ("ro", 1)),
        MEASURE(2, ("ro", 2)),
        MEASURE(3, ("ro", 3))
        ).wrap_in_numshots_loop(10)


# returning my circuit parameterizations and metrics
print("============================================================================")
print("CIRCUIT DEFINITIONS:")
print(quantumprog)
print("============================================================================")

# run the program on a QVM
qc = get_qc('9q-square-qvm')
result = qc.run(qc.compile(quantumprog)).readout_data.get("ro")

# return the results
print("Results:")
print(result)


alt.Chart(result).mark_circle().encode(
        x="result:Q",
        y="result:Q")
