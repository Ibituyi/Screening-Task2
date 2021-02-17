#!/usr/bin/env python
# coding: utf-8

# In[1]:


from qiskit import QuantumRegister
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor

print('\nSign Flip Code')
print('----------------')

IBMQ.enable_account('7a14c59cb5d061ddf7b9287874a80aa122f1cae65910e33fa678220ec5d475a637b83a0e9f8f54a43e3a128d5e5154f084a924dbfdef0da5a3e777c940a15b55')
provider = IBMQ.get_provider(hub='ibm-q')

backend = provider.get_backend('ibmq_qasm_simulator')

q = QuantumRegister(3,'q')
c = ClassicalRegister(1,'c')

circuit = QuantumCircuit(q,c)

circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])

circuit.h(q[0])
circuit.h(q[1])
circuit.h(q[2]) 
circuit.z(q[0]) #Add this to simulate a sign flip error
circuit.h(q[0])
circuit.h(q[1])
circuit.h(q[2])

circuit.cx(q[0],q[1])
circuit.cx(q[0],q[2])
circuit.ccx(q[2],q[1],q[0])
circuit.measure(q[0],c[0])

job = execute(circuit, backend, shots=1000)

job_monitor(job)

counts = job.result().get_counts()

print("\nSign flip code with error")
print("----------------------")
print(counts)
input()


# In[ ]:




