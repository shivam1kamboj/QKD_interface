import cirq
import numpy as np
from copy import deepcopy  

# Function to generate a random bit string
def random_bits(n):
    return np.random.randint(2, size=n) 

# Preparing qubits and encoding them based on Alice's random bits and bases
def prepare_qubits(bit_string, basis_string, qubits):
    for i, bit in enumerate(bit_string):
        if basis_string[i] == 0:  # Prepare in computational basis
            if bit == 1:
                yield cirq.X(qubits[i])
        else:  # Prepare in Hadamard basis
            if bit == 1:
                yield cirq.X(qubits[i])
            yield cirq.H(qubits[i])

# Bob's measurement in random bases
def measure_in_basis(qubits, basis_string):
    for i, basis in enumerate(basis_string):
        if basis == 1:
            yield cirq.H(qubits[i])
        yield cirq.measure(qubits[i], key=f'q{i}')

def QKD_simulator(total_qubits):

    # Step 1: Alice generates random bits and bases
    alice_bits = random_bits(total_qubits)
    alice_bases = random_bits(total_qubits)

    # Step 2: Bob generates random bases
    bob_bases = random_bits(total_qubits)

    # Step 3: Preparing qubits based on Alice's bits and bases
    qubits = [cirq.LineQubit(i) for i in range(total_qubits)]
    circuit = cirq.Circuit()
    circuit += prepare_qubits(alice_bits, alice_bases, qubits)
    Alice_circuit = deepcopy(circuit)  # Making a deep copy for later printing Alice's Quantum circuit


    # Step 4: Bob measures the qubits in his bases
    circuit += measure_in_basis(qubits, bob_bases)
    Bob_circuit = deepcopy(circuit)  # Making a deep copy for later printing Bob's Quantum Circuit

    # Simulating the circuit
    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1)

    # Extracting Bob's measurement results
    bob_results = [int(result.measurements[f'q{i}'][0]) for i in range(total_qubits)]

    # Step 5: Generating the shared key
    shared_key = []
    for i in range(total_qubits):
        if alice_bases[i] == bob_bases[i]:
            shared_key.append(bob_results[i])

    output = {
        "alice_bits": alice_bits,
        "alice_bases": alice_bases,
        "bob_bases": bob_bases,
        "bob_results": bob_results,
        "shared_key": shared_key
    }

    str_Alice = str(Alice_circuit)
    str_Bob = str(Bob_circuit)
    output["Alice's Circuit"] = str_Alice
    output["Bob's Circuit"] = str_Bob

    return output
