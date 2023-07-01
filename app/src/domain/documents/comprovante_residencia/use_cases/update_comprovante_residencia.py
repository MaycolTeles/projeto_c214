"""
Module containing the UpdateComprovanteResidencia Use Case.
"""

from datetime import datetime

from ..comprovante_residencia import ComprovanteResidencia
from ..request_model import ComprovanteResidenciaRequest
from ..response_model import ComprovanteResidenciaResponse
from ..types import ComprovanteResidenciaType
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class UpdateComprovanteResidencia(UseCase):
    """
    Use Case class to update a new ComprovanteResidencia.
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
        comprovante_residencia = self._update_comprovante_residencia(request)

        response = comprovante_residencia
        response_model = ComprovanteResidenciaResponse(
            success=success,
            response=response
        )

        return response_model

    def _update_comprovante_residencia(
        self,
        request: ComprovanteResidenciaRequest
    ) -> ComprovanteResidencia:
        """
        TODO
        """
        date_str = request.values.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d")

        comprovante = request.values.get("comprovante_type")
        comprovante_type = ComprovanteResidenciaType(comprovante)

        comprovante_residencia = ComprovanteResidencia(
            value=request.values.get("value"),
            date=date,
            comprovante_type=comprovante_type
        )

        request = {
            "type": "comprovante_residencia",
            "id": request.values.get("id"),
            "document": comprovante_residencia,
        }

        response = self._repository.update(request)

        return response
