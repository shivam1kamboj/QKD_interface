To make quantum key distribution (QKD) more accessible, I developed a web-based simulation using Flask and HTML/Jinja2, with Cirq handling quantum circuit simulations in the backend.

## Installation
To set up the project locally:
1. Clone the [repository](https://github.com/shivam1kamboj/QKD_interface.git)
2. Install the required dependencies
3. Navigate to directory QKD_interface
4. Run `python app.py` in your terminal to start the Flask server

The Jupyter file QKD.ipynb in this project is used for debugging. You can either discard this file or use it to take this QKD project to next level. 

## Eve's Interception in Quantum Key Distribution

In the realm of Quantum Key Distribution (QKD), one of the most fascinating aspects is its inherent security, which is guaranteed by the fundamental principles of quantum mechanics. A crucial feature of QKD is its ability to detect any eavesdropping attempts by an external party, commonly referred to as Eve. Here's how it works and how users can verify the disturbance in the correlation due to Eve's interception.

### Understanding Eve's Role

Eve aims to intercept the quantum key being shared between Alice and Bob. In a classic QKD setup, Alice sends qubits to Bob, each encoded in a particular quantum state. If Eve tries to measure these qubits to gain knowledge of the key, the act of measuring will inevitably alter their states due to the quantum no-cloning theorem and Heisenberg's uncertainty principle. This alteration can be detected by Alice and Bob.

### Detecting Eavesdropping

The security of QKD relies on the fact that any attempt to eavesdrop on the quantum channel will introduce anomalies in the correlation of the qubits' states between Alice and Bob. Here's how users can observe this phenomenon in the simulation:

1. #### Simulate with Eve's Interference: 
The simulation includes an option to introduce Eve into the key exchange process. By choosing this, users can simulate the effect of Eve trying to intercept the qubit states being exchanged.

2. #### Observing Disturbed Correlations: 
When Alice and Bob's bases match, their qubit states should be 100% correlated in the absence of eavesdropping. However, if Eve intercepts and measures the qubits, this correlation will be disturbed. After running the simulation with Eve's interference, users will notice discrepancies in the correlation when comparing Alice and Bob's qubit states for matching bases. This disturbance is a clear indicator of an interception attempt.

3. #### Analyzing the Results: 
The simulation results will provide detailed insights into the disturbed correlations, allowing users to directly observe the impact of Eve's interception. By comparing the shared key generated without Eve's interference to the one generated with her interference, users can see the stark differences, highlighting the quantum key distribution's security feature.