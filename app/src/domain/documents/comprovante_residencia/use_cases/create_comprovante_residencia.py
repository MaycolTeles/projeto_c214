"""
Module containing the CreateComprovanteResidencia Use Case.
"""

from datetime import datetime

from ..comprovante_residencia import ComprovanteResidencia
from ..exceptions import InvalidComprovanteResidenciaException
from ..request_model import ComprovanteResidenciaRequest
from ..response_model import ComprovanteResidenciaResponse
from ..types import ComprovanteResidenciaType
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class CreateComprovanteResidencia(UseCase):
    """
    Use Case class to create a new ComprovanteResidencia.
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
        try:
            comprovante_residencia = self._create_comprovante_residencia(request)

        except InvalidComprovanteResidenciaException as error:
            # TODO> Log error
            print(error)
            success = False
            response = str(error)

            response_model = ComprovanteResidenciaResponse(
                success=success,
                response=response
            )
            return response_model

        self._save_comprovante_residencia_in_repository(comprovante_residencia)

        response = "ComprovanteResidencia was successfully created."
        response_model = ComprovanteResidenciaResponse(
            success=success,
            response=response
        )

        return response_model

    def _create_comprovante_residencia(
        self,
        request: ComprovanteResidenciaRequest
    ) -> ComprovanteResidencia:
        """
        TODO
        """
        value = request.values.get("value")
        date_str = request.values.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d")
        comprovante_str = request.values.get("comprovante_type")
        comprovante_type = ComprovanteResidenciaType(comprovante_str)

        comprovante_residencia = ComprovanteResidencia(
            value=value,
            date=date,
            comprovante_type=comprovante_type
        )

        return comprovante_residencia

    def _save_comprovante_residencia_in_repository(self, comprovante_residencia: ComprovanteResidencia):
        """
        TODO: IMPLEMENT
        """
        request = {
            "type": "comprovante_residencia",
            "document": comprovante_residencia,
        }

        self._repository.create(request)
