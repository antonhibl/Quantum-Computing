# y0ka1
# July 16th, 2021

import strangeworks.qiskit
from strangeworks.qiskit.provider import StrangeworksProvider

# Define a provider for runtime
provider = StrangeworksProvider(
    hub="strangeworks-hub",
    group="qc-com",
    project="runtime")

# define progam inputs for runtime
program_inputs = {
    'iterations': 10
}


options = {'backend_name': "ibmq_qasm_simulator"}

# This deals with Interim results, some programs call you back on every iteration
def interim_result_callback(job_id, interim_result):
    # In this case, `interim_result` contains a dictionary of counts, and the iteration number.
    strangeworks.histogram(
        interim_result["counts"], 
        label=f"Iteration {interim_result['iteration']}"
        )

# Run the program
job = provider.runtime.run(program_id="sample-program",
                           options=options,
                           inputs=program_inputs,
                           callback=interim_result_callback
                           )

result = job.result()

strangeworks.print(f"Results: {result}", type="plaintext", label="Final Result")
