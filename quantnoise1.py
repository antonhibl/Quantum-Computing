from qiskit import QuantumCircuit, execute
from qiskit import IBMQ, Aer
from qiskit.visualization import plot_histogram
from qiskit.providers.aer.noise import NoiseModel
import matplotlib.pyplot as plt
import matplotlib

# Build noise model from backend properties
provider = IBMQ.load_account()
backend = provider.get_backend("ibmq_quito", hub=None)
noise_model = NoiseModel.from_backend(backend)

# Get coupling map from backend
coupling_map = backend.configuration().coupling_map

# Get basis gates from noise model
basis_gates = noise_model.basis_gates

# Make a circuit
circ = QuantumCircuit(3, 3)
circ.h(0)
circ.cx(0, 1)
circ.cx(1, 2)
circ.measure([0, 1, 2], [0, 1, 2])

# Perform a noise simulation
result = execute(
    circ,
    Aer.get_backend("qasm_simulator"),
    coupling_map=coupling_map,
    basis_gates=basis_gates,
    noise_model=noise_model,
).result()
counts = result.get_counts(0)
print(counts)

# Draws the circuit and plots a histogram of probabilities using matplotlib
circ.draw(output="mpl")
plt.show()
plot_histogram(counts, color="c")
