#!/usr/bin/env python
# coding: utf-8

# In[1]:


import qiskit as qk

# Creating Qubits
q = qk.QuantumRegister(2)
# Creating qubits
circuit = qk.QuantumCircuit(q)
# Hadamard Gate on the first Qubit
circuit.h(q[0])
# CNOT Gate on the first and second Qubits
circuit.cx(q[0], q[1])
print (circuit)


# In[ ]:




