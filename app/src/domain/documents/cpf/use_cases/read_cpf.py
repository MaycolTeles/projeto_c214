"""
Module containing the ReadCPF Use Case.
"""

from ..cpf import CPF
from ..request_model import CPFRequest
from ..response_model import CPFResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class ReadCPF(UseCase):
    """
    Use Case class to read a new CPF.
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
        cpf = self._read_cpf(request)

        response = cpf
        response_model = CPFResponse(
            success=success,
            response=response
        )

        return response_model

    def _read_cpf(
        self,
        request: CPFRequest
    ) -> CPF:
        """
        TODO
        """
        cpf_id = request.values.get("id")

        request = {
            "type": "cpf",
            "id": cpf_id,
        }
        response = self._repository.read(request)

        return response
