"""
Module containing the DeleteCPF Use Case.
"""

from ..cpf import CPF
from ..request_model import CPFRequest
from ..response_model import CPFResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class DeleteCPF(UseCase):
    """
    Use Case class to delete a new CPF.
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
        cpf = self._delete_cpf(request)

        response = cpf
        response_model = CPFResponse(
            success=success,
            response=response
        )

        return response_model

    def _delete_cpf(
        self,
        request: CPFRequest
    ) -> CPF:
        """
        TODO
        """
        request = {
            "type": "cpf",
            "id": request.values.get("id"),
        }
        response = self._repository.delete(request)

        return response
