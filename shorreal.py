# Made by Anton Hibl
# April 8th, 2021

# Demonstrates how shors algorithm works using Qiskit
from qiskit import (
        Aer,
        QuantumCircuit,
        execute,
        Aer,
        QuantumRegister,
        ClassicalRegister,
        IBMQ,
)
from qiskit.visualization import plot_histogram, circuit_drawer
import math
from qiskit.visualization import plot_state_city, plot_bloch_multivector
from qiskit.visualization import plot_state_paulivec, plot_state_hinton
from qiskit.visualization import plot_state_qsphere
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.tools.visualization import circuit_drawer, plot_histogram
from qiskit import BasicAer
from qiskit.providers.aer.noise import NoiseModel
import qiskit.providers.aer.noise as noise
import matplotlib.pyplot as plt

provider = IBMQ.load_account()
backend = provider.get_backend("ibmq_16_melbourne")

# Error probabilities
prob_1 = 0.001  # 1-qubit gate
prob_2 = 0.01  # 2-qubit gate

error_1 = noise.depolarizing_error(prob_1, 1)
error_2 = noise.depolarizing_error(prob_2, 2)

# creates the noise model from the backend's properties
noise_model = noise.NoiseModel()
noise_model.add_all_qubit_quantum_error(error_1, ["u1", "u2", "u3"])
noise_model.add_all_qubit_quantum_error(error_2, ["cx"])

# Get coupling map from the backend
coupling_map = backend.configuration().coupling_map

# Get basis gates from the noise models we just loaded
basis_gates = noise_model.basis_gates

input_register = QuantumRegister(4)
output_register = QuantumRegister(4)
c = ClassicalRegister(8)

qc = QuantumCircuit(input_register, output_register, c)
qc.h(input_register)
qc.barrier()

qc.x(output_register[0])
qc.barrier()

qc.cx(input_register[0], output_register[2])
qc.cx(input_register[0], output_register[3])
qc.barrier()

qc.cx(input_register[1], output_register[2])
qc.cx(input_register[1], output_register[0])
qc.barrier()

qc.ccx(input_register[0], input_register[1], output_register[3])
qc.ccx(input_register[0], input_register[1], output_register[2])
qc.ccx(input_register[0], input_register[1], output_register[1])
qc.ccx(input_register[0], input_register[1], output_register[0])
qc.barrier()

# measure the output
qc.measure([4, 5, 6, 7], [4, 5, 6, 7])
qc.barrier()


# Apply the Fourier Transform to the new state of the input register.
qc.h(input_register[0])
qc.cp(math.pi / float(2), input_register[0], input_register[1])
qc.cp(math.pi / float(2 ** 2), input_register[0], input_register[2])
qc.cp(math.pi / float(2 ** 3), input_register[0], input_register[3])
qc.barrier()

qc.h(input_register[1])
qc.cp(math.pi / float(2), input_register[1], input_register[2])
qc.cp(math.pi / float(2 ** 2), input_register[1], input_register[3])
qc.barrier()

qc.h(input_register[2])
qc.cp(math.pi / float(2), input_register[2], input_register[3])
qc.h(input_register[3])
qc.barrier()

qc.measure([0, 1, 2, 3], [0, 1, 2, 3])

job = execute(qc, backend, shots=1000)
result = execute(
    qc,
    Aer.get_backend("qasm_simulator"),
    coupling_map=coupling_map,
    basis_gates=basis_gates,
    noise_model=noise_model,
    shots=1000,
).result()
# Returns counts
counts = result.get_counts(qc)
print(counts)

# Optionally draw the circuit and plot it(Best used while in the
# quantum interface for IBM

plot_histogram(counts, figsize=(14, 10))
plt.show()
qc.draw(output='mpl')
plt.show()
