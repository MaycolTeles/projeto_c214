"""
Module containing the DeleteComprovanteResidencia Use Case.
"""

from ..comprovante_residencia import ComprovanteResidencia
from ..request_model import ComprovanteResidenciaRequest
from ..response_model import ComprovanteResidenciaResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class DeleteComprovanteResidencia(UseCase):
    """
    Use Case class to delete a new ComprovanteResidencia.
    """
    # _repository: ComprovanteResidenciaRepository

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
        comprovante_residencia = self._delete_comprovante_residencia(request)

        response = comprovante_residencia
        response_model = ComprovanteResidenciaResponse(
            success=success,
            response=response
        )

        return response_model

    def _delete_comprovante_residencia(
        self,
        request: ComprovanteResidenciaRequest
    ) -> ComprovanteResidencia:
        """
        TODO
        """
        request = {
            "type": "comprovante_residencia",
            "id": request.values.get("id"),
        }
        comprovante_residencia = self._repository.delete(request)

        return comprovante_residencia
