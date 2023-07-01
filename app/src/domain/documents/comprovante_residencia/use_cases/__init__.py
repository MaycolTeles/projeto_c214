"""
__init__ file to export the classes below.
"""

from .create_comprovante_residencia import CreateComprovanteResidencia
from .read_comprovante_residencia import ReadComprovanteResidencia
from .read_all_comprovante_residencia import ReadAllComprovanteResidencia
from .update_comprovante_residencia import UpdateComprovanteResidencia
from .delete_comprovante_residencia import DeleteComprovanteResidencia


__all__ = [
    "CreateComprovanteResidencia",
    "ReadComprovanteResidencia",
    "ReadAllComprovanteResidencia",
    "UpdateComprovanteResidencia",
    "DeleteComprovanteResidencia",
]
