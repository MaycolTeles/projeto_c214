"""
Module containing the UpdateCPF Use Case.
"""

from datetime import datetime

from ..cpf import CPF
from ..request_model import CPFRequest
from ..response_model import CPFResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class UpdateCPF(UseCase):
    """
    Use Case class to update a new CPF.
    """
    _repository: Repository

    def __init__(self):
        """TODO"""
        self._repository = get_repository()

    def execute(
        self,
        request: CPFRequest
    ) -> CPFResponse:
        """
        Method to execute the use case.
        """
        success = True
        cpf = self._update_cpf(request)

        response = cpf
        response_model = CPFResponse(
            success=success,
            response=response
        )

        return response_model

    def _update_cpf(
        self,
        request: CPFRequest
    ) -> CPF:
        """
        TODO
        """
        id = request.values.get("id")

        value = request.values.get("value")
        date_str = request.values.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d")

        cpf = CPF(value=value, date=date)

        request = {
            "type": "cpf",
            "id": id,
            "document": cpf
        }
        response = self._repository.update(request)

        return response
