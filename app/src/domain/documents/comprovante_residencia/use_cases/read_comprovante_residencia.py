"""
Module containing the ReadComprovanteResidencia Use Case.
"""

from ..comprovante_residencia import ComprovanteResidencia
from ..request_model import ComprovanteResidenciaRequest
from ..response_model import ComprovanteResidenciaResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class ReadComprovanteResidencia(UseCase):
    """
    Use Case class to read a new ComprovanteResidencia.
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
        comprovante_residencia = self._read_comprovante_residencia(request)

        response = comprovante_residencia
        response_model = ComprovanteResidenciaResponse(
            success=success,
            response=response
        )

        return response_model

    def _read_comprovante_residencia(
        self,
        request: ComprovanteResidenciaRequest
    ) -> ComprovanteResidencia:
        """
        TODO
        """
        comprovante_residencia_id = request.values.get("id")

        request = {
            "type": "comprovante_residencia",
            "id": comprovante_residencia_id,
        }
        comprovante_residencia = self._repository.read(request)

        return comprovante_residencia
