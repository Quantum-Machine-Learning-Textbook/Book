# Multiple Qubit Gates

A unitary transformation on multiple qubits is considered a multiple qubit gate.
Such multiple qubit gates can be a gate in themselves or be a tensor product of single qubit gates applied simultaneously on individual qubits.

Below is an example of multiple qubit gate applied as single qubit gates $X$ and $Z$.

\begin{equation}
X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}
Z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} \\
X \otimes Z = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} \otimes \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}
= \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \\ 1 & 0 & 0 & 0 \\ 0 & -1 & 0 & 0 \end{bmatrix}
\end{equation}

Below is an example of an arbitrary two-qubit gate.

\begin{equation}
U = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & \frac{1}{\sqrt{2}} & \frac{-1}{\sqrt{2}} & 0 \\ 0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\ 0 & 0 & 0 & 1\end{bmatrix}
\end{equation}

from qiskit import QuantumCircuit
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram

qc = QuantumCircuit(2)
qc.x(0)
qc.h(1)
qc.draw()

backend = Aer.get_backend('statevector_simulator')
result = execute(qc,backend).result()
out_state = result.get_statevector()
print(out_state)

## Controlled Gates

A commonly used class of multi-qubit gates is the controlled gates.
Controlled gates have a set of source qubits and a set of target qubits.
The desired operation is applied on target qubits only when the source qubits are set and, hence, "controlled" by them.

The controlled gate named $CNOT$ is a widely used one.
It applies the $NOT$ gate ($X$ gate) on the target qubit iff the source qubit is set.
It has the following matrix representation:
\begin{equation}
CNOT = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0\end{bmatrix}
\end{equation}

qc2 = QuantumCircuit(2)
qc2.h(0)
qc2.cx(0,1)
qc2.draw()

backend = Aer.get_backend('statevector_simulator')
result = execute(qc2,backend).result()
out_state = result.get_statevector()
print(out_state)