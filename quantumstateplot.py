from qiskit.visualization import plot_state_city, plot_bloch_multivector
from qiskit.visualization import plot_state_paulivec, plot_state_hinton
from qiskit.visualization import plot_state_qsphere
from qiskit import QuantumCircuit, execute, Aer, BasicAer
from qiskit.visualization import plot_histogram, circuit_drawer
import qiskit.providers.aer.noise as noise
import matplotlib.pyplot as plt

# Error probabilities
prob_1 = 0.001  # 1-qubit gate
prob_2 = 0.01  # 2-qubit gate

# Depolarizing quantum errors
error_1 = noise.depolarizing_error(prob_1, 1)
error_2 = noise.depolarizing_error(prob_2, 2)

# Add errors to noise model
noise_model = noise.NoiseModel()
noise_model.add_all_qubit_quantum_error(error_1, ["u1", "u2", "u3"])
noise_model.add_all_qubit_quantum_error(error_2, ["cx"])

# Get basis gates from noise model
basis_gates = noise_model.basis_gates

# Make a circuit
circ = QuantumCircuit(3, 3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure([0, 1, 2], [0, 1, 2])

# execute the quantum circuit
result = execute(
    circ,
    Aer.get_backend("statevector_simulator"),
    basis_gates=basis_gates,
    noise_model=noise_model,
).result()
psi = result.get_statevector(circ)
counts = result.get_counts(0)

circ.draw(output="mpl")
plt.show()

plot_state_city(psi)
plot_state_hinton(psi)
plot_state_qsphere(psi)
plot_state_paulivec(psi)
plot_bloch_multivector(psi)

plot_histogram(counts, color="c")
