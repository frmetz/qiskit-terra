"""
controlled-NOT gate.

Author: Andrew Cross
"""
from qiskit_sdk import QuantumRegister
from qiskit_sdk import Program
from qiskit_sdk import Gate
from qiskit_sdk import InstructionSet
from qiskit_sdk import CompositeGate


class CnotGate(Gate):
    """controlled-NOT gate."""

    def __init__(self, ctl, tgt):
        """Create new CNOT gate."""
        super(CnotGate, self).__init__("cx", [], [ctl, tgt])

    def qasm(self):
        """Return OPENQASM string."""
        ctl = self.arg[0]
        tgt = self.arg[1]
        return "cx %s[%d],%s[%d];" % (ctl[0].name, ctl[1],
                                      tgt[0].name, tgt[1])

    def inverse(self):
        """Invert this gate."""
        return self  # self-inverse


def cx(self, i, j):
    """Apply CNOT from i to j in this register."""
    self._check_bound()
    gs = InstructionSet()
    self.check_range(i)
    self.check_range(j)
    for p in self.bound_to:
        gs.add(p.cx((self, i), (self, j)))
    return gs


QuantumRegister.cx = cx


def cx(self, ctl, tgt):
    """Apply CNOT from ctl to tgt."""
    self._check_qreg(ctl[0])
    ctl[0].check_range(ctl[1])
    self._check_qreg(tgt[0])
    tgt[0].check_range(tgt[1])
    return self._attach(CnotGate(ctl, tgt))


Program.cx = cx


def cx(self, ctl, tgt):
    """Apply CNOT from ctl to tgt."""
    self._check_qubit(ctl)
    self._check_qubit(tgt)
    ctl[0].check_range(ctl[1])
    tgt[0].check_range(tgt[1])
    return self._attach(CnotGate(ctl, tgt))


CompositeGate.cx = cx
