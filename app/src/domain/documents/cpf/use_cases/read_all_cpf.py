"""
Module containing the ReadAllCPF Use Case.
"""

from ..cpf import CPF
from ..request_model import CPFRequest
from ..response_model import CPFResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class ReadAllCPF(UseCase):
    """
    Use Case class to read all CPF.
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
        all_cpf = self._read_all_cpf(request)

        response = all_cpf
        response_model = CPFResponse(
            success=success,
            response=response
        )

        return response_model

    def _read_all_cpf(
        self,
        request: CPFRequest
    ) -> CPF:
        """
        TODO
        """
        request = {
            "type": "cpf",
        }
        response = self._repository.read_all(request)

        return response
