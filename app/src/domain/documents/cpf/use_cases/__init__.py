"""
__init__ file to export the classes below.
"""

from .create_cpf import CreateCPF
from .read_cpf import ReadCPF
from .read_all_cpf import ReadAllCPF
from .update_cpf import UpdateCPF
from .delete_cpf import DeleteCPF


__all__ = [
    "CreateCPF",
    "ReadCPF",
    "ReadAllCPF",
    "UpdateCPF",
    "DeleteCPF",
]
