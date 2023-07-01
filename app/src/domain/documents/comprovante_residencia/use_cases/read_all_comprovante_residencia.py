"""
Module containing the ReadAllComprovanteResidencia Use Case.
"""

from ..comprovante_residencia import ComprovanteResidencia
from ..request_model import ComprovanteResidenciaRequest
from ..response_model import ComprovanteResidenciaResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class ReadAllComprovanteResidencia(UseCase):
    """
    Use Case class to read all ComprovanteResidencia.
    """
    _repository: Repository

    def __init__(self):
        """TODO"""
        self._repository = get_repository()

    def execute(
        self,
        request: ComprovanteResidenciaRequest
    ) -> ComprovanteResidenciaResponse:
        """
        Method to execute the use case.
        """
        success = True
        all_comprovante_residencia = self._read_all_comprovante_residencia(request)

        response = all_comprovante_residencia
        response_model = ComprovanteResidenciaResponse(
            success=success,
            response=response
        )

        return response_model

    def _read_all_comprovante_residencia(
        self,
        request: ComprovanteResidenciaRequest
    ) -> ComprovanteResidencia:
        """
        TODO
        """
        request = {
            "type": "comprovante_residencia",
        }
        comprovante_residencia = self._repository.read_all(request)

        return comprovante_residencia
