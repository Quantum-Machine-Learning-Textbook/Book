# Single Qubit Gates

Unlike the gates (like AND and OR) in classical computation, quantum gates are reversible in nature, which means that they map a unique input to a unique output.
These gates are represented by using unitary matrices and conversely, any unitary matrix can be thought of as a valid quantum gate.

from qiskit import QuantumCircuit
from qiskit import execute, Aer
from qiskit.visualization import plot_histogram, plot_bloch_multivector
from math import pi

## Pauli Gates

Some of the commonly used single-qubit gates are:

\begin{equation}
    X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix} = |0\rangle\langle1| + |1\rangle\langle0| \quad\quad\quad\quad Y = \begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix} = -i|0\rangle\langle1| + i|1\rangle\langle0|
\end{equation}

\begin{equation}
    Z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix} = |0\rangle\langle0| - |1\rangle\langle1| \quad\quad\quad\quad H = \frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix} = \left(\frac{|0\rangle + |1\rangle}{\sqrt{2}}\right)\langle0| + \left(\frac{|0\rangle - |1\rangle}{\sqrt{2}}\right)\langle1|
\end{equation}


qcX = QuantumCircuit(1,1)
qcX.x(0)
qcX.measure(0,0)
qcX.draw()

backend = Aer.get_backend('qasm_simulator')
result = execute(qcX,backend).result()
counts = result.get_counts()
plot_histogram(counts)

qcY = QuantumCircuit(1)
qcY.y(0)
qcY.draw()

backend = Aer.get_backend('statevector_simulator')
result = execute(qcY,backend).result()
out_state = result.get_statevector()
print(out_state)

qcZ = QuantumCircuit(1)
qcZ.initialize([0,1],0)
qcZ.z(0)
qcZ.draw()

backend = Aer.get_backend('statevector_simulator')
result = execute(qcZ,backend).result()
out_state = result.get_statevector()
print(out_state)

qcH = QuantumCircuit(1,1)
qcH.h(0)
qcH.measure(0,0)
qcH.draw()

backend = Aer.get_backend('qasm_simulator')
result = execute(qcH,backend).result()
counts = result.get_counts()
plot_histogram(counts)

# Bloch Sphere

A convenient way of visualising a single qubit is the Bloch Sphere.
We can represent a single qubit state with 3 real numbers $\alpha$, $\beta$ and $\phi$, instead of only $\alpha$ and $\beta$ as complex numbers.
Note that this is possible because the global phase does not matter, and only the relative phase ($\phi$) matters.

\begin{equation}
    |\psi\rangle = \alpha|0\rangle + e^{i\phi}\beta|1\rangle
\end{equation}

For normalisation, we know that $\sqrt{\alpha^2 + \beta^2} = 1$.
Hence, we can describe $\alpha$ and $\beta$ using a single variable $\theta$ as $\alpha = \cos{\tfrac{\theta}{2}}$ and $\beta=\sin{\tfrac{\theta}{2}}$.

So, for real $\theta$ and $\phi$, we get

\begin{equation}
    |\psi\rangle = \cos{\tfrac{\theta}{2}}|0\rangle + e^{i\phi}\sin{\tfrac{\theta}{2}}|1\rangle
\end{equation}

Using $\theta$ and $\phi$ as the polar coordinates, we can map any single qubit state to a point on a sphere of radius $1$.
This sphere is called the Bloch Sphere.

plot_bloch_multivector([0,0,1,0])

plot_bloch_multivector([1/2**0.5,1/2**0.5])

## Rotation Gates

With respect to the Bloch Sphere (defined above), we have the rotation gates along the 3 axes, namely RX, RY and RZ.
These gates perform a rotation of the qubit vector along the specified axis by an angle $\theta$.

\begin{align}\begin{aligned}\newcommand{\th}{\frac{\theta}{2}}\\\begin{split}RX(\theta) = 
    \begin{pmatrix}
        \cos{\th}   & -i\sin{\th} \\
        -i\sin{\th} & \cos{\th}
    \end{pmatrix}\end{split}\end{aligned}
\end{align}

\begin{align}\begin{aligned}\\\begin{split}RY(\theta) =
    \begin{pmatrix}
        \cos{\th} & -\sin{\th} \\
        \sin{\th} & \cos{\th}
    \end{pmatrix}\end{split}\end{aligned}
\end{align}

\begin{align}\begin{aligned}\\\begin{split}RZ(\theta) =
    \begin{pmatrix}
        e^{-i\th} & 0 \\
        0 & e^{i\th}
    \end{pmatrix}\end{split}\end{aligned}
\end{align}


qcRX = QuantumCircuit(1)
qcRX.rx(pi/2,0)
qcRX.draw()

backend = Aer.get_backend('statevector_simulator')
result = execute(qcRX,backend).result()
out_state = result.get_statevector()
print(out_state)
plot_bloch_multivector(out_state)

qcRY = QuantumCircuit(1)
qcRY.ry(pi,0)
qcRY.draw()

backend = Aer.get_backend('statevector_simulator')
result = execute(qcRY,backend).result()
out_state = result.get_statevector()
print(out_state)
plot_bloch_multivector(out_state)

qcRZ = QuantumCircuit(1)
qcRZ.rz(pi/2,0)
qcRZ.draw()

backend = Aer.get_backend('statevector_simulator')
result = execute(qcRZ,backend).result()
out_state = result.get_statevector()
print(out_state)
plot_bloch_multivector(out_state)