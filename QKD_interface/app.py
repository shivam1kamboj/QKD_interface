from flask import Flask, render_template, request
from quantum_functions import *
from Eves_intercept import *
import cirq
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    simulation_output = ""
    if request.method == 'POST':
        alice_bits = request.form.get('alice_bits')
        # Assuming alice_bits is a string of 0s and 1s
        total_qubits = len(alice_bits)
        simulation_output = QKD_simulator(total_qubits)  # Modify QKD_simulator to return its outputs
    return render_template('home.html', simulation_output=simulation_output)

@app.route('/eves_interfere', methods=['GET', 'POST'])
def eves_interfere():
    simulation_output = ""
    if request.method == 'POST':
        alice_bits = request.form.get('alice_bits')
        total_qubits = len(alice_bits)
        simulation_output = QKD_simulator_with_intruder(total_qubits)  
    return render_template('eves_interfere.html', simulation_output=simulation_output)

if __name__ == '__main__':
    app.run(debug=True)