
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

# Eve's interception and measurement in random bases
def eve_intercept_measure(qubits, eve_bases):
    for i, basis in enumerate(eve_bases):
        if basis == 1:
            yield cirq.H(qubits[i])
        yield cirq.measure(qubits[i], key=f'eve_q{i}')
        if basis == 1:
            yield cirq.H(qubits[i])  # To revert to the original basis

def QKD_simulator_with_intruder(total_qubits):
    # Same initial steps as before
    alice_bits = random_bits(total_qubits)
    alice_bases = random_bits(total_qubits)
    bob_bases = random_bits(total_qubits)

    qubits = [cirq.LineQubit(i) for i in range(total_qubits)]
    circuit = cirq.Circuit()
    circuit += prepare_qubits(alice_bits, alice_bases, qubits)

      # Eve generates random bases for interception
    eve_bases = random_bits(total_qubits)

    # Eve intercepts and measures the qubits
    circuit += eve_intercept_measure(qubits, eve_bases)

    # Bob measures the qubits in his bases
    circuit += measure_in_basis(qubits, bob_bases)

    simulator = cirq.Simulator()
    result = simulator.run(circuit, repetitions=1)

    # Extracting Bob's measurement results
    bob_results = [int(result.measurements[f'q{i}'][0]) for i in range(total_qubits)]

    # Generating the shared key
    shared_key = []
    for i in range(total_qubits):
        if alice_bases[i] == bob_bases[i]:
            shared_key.append(bob_results[i])

    # Output results including Eve's interference
    output = {
        "alice_bits": alice_bits,
        "alice_bases": alice_bases,
        "bob_bases": bob_bases,
        "bob_results": bob_results,
        "shared_key": shared_key,
        "eve_bases": eve_bases,
    }

    return output
