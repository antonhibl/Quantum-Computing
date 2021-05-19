from qiskit import (
    QuantumCircuit,
    execute,
    Aer,
    QuantumRegister,
    ClassicalRegister,
    IBMQ,
)
from qiskit.visualization import plot_histogram
from qiskit.providers.aer.noise import NoiseModel
import matplotlib.pyplot as plt
from qiskit.visualization import plot_state_city, plot_bloch_multivector
from qiskit.visualization import plot_state_paulivec, plot_state_hinton
from qiskit.visualization import plot_state_qsphere
from qiskit.visualization import plot_histogram, circuit_drawer
import qiskit.providers.aer.noise as noise

# load my IBM Q acc and load a backend quantum cpu

# Error probabilities
prob_1 = 0.001  # 1-qubit gate
prob_2 = 0.01  # 2-qubit gate

# Depolarizing quantum errors
error_1 = noise.depolarizing_error(prob_1, 1)
error_2 = noise.depolarizing_error(prob_2, 2)

# creates the noise model from the backend's properties
noise_model = NoiseModel.from_backend(backend)
noise_model.add_all_qubit_quantum_error(error_1, ["u1", "u2", "u3"])
noise_model.add_all_qubit_quantum_error(error_2, ["cx"])

# Get coupling map from the backend
coupling_map = backend.configuration().coupling_map

# Get basis gates from the noise models we just loaded
basis_gates = noise_model.basis_gates


# create the quantum circuit that acts on 2 registers, 1 classical and 1 quantum
# the classical register is only initialized once but the bit/qubit is in that state
# twice during the course of the program. It starts as a classical bit, gets          initialized
# and quantized through the quantum register, and then the classical register brings  it
# back and collapses most of the qubit back to classical bit information; this
# essentially simulates real probabilities.
qreg_q = QuantumRegister(3, "q")
creg_c = ClassicalRegister(3, "c")
circuit = QuantumCircuit(qreg_q, creg_c)

# adds a Hadamard (H) Gate on qubit 0 inside of the quantum register
circuit.h(qreg_q[0])
circuit.cx(0, 1)
# Maps the qubits back to bits and "measures" them as most of the qubit
# collapses to definable bit information.
circuit.measure(qreg_q[0], creg_c[0])

# Execute this circuit on the backend we specified before
job = execute(circuit, backend, shots=1000)

# Grab results from the job
result = execute(
    circuit,
    Aer.get_backend("qasm_simulator"),
    coupling_map=coupling_map,
    basis_gates=basis_gates,
    noise_model=noise_model,
    shots=1000,
).result()
# Returns counts
counts = result.get_counts(circuit)
print(counts)

# Optionally draw the circuit and plot it(Best used while in the
# quantum interface for IBM
circuit.draw(output="mpl")
plt.show()
plot_histogram(counts, color="c")

# execute the quantum circuit
result = execute(
    circuit,
    Aer.get_backend("statevector_simulator"),
    coupling_map=coupling_map,
    basis_gates=basis_gates,
    noise_model=noise_model,
).result()

psi = result.get_statevector(circuit)
plot_state_city(psi)
plot_state_hinton(psi)
plot_state_qsphere(psi)
plot_state_paulivec(psi)
plot_bloch_multivector(psi)
