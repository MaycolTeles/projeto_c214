"""
Module containing the CreateCPF Use Case.
"""

from datetime import datetime

from ..cpf import CPF
from ..exceptions import InvalidCPFException
from ..request_model import CPFRequest
from ..response_model import CPFResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class CreateCPF(UseCase):
    """
    Use Case class to create a new CPF.
    """
    _repository: Repository

    def __init__(self) -> None:
        self._repository = get_repository()

    def execute(self, request: CPFRequest) -> CPFResponse:
        """
        Method to execute the use case.
        """
        success = True
        try:
            cpf = self._create_cpf(request)

        except InvalidCPFException as error:
            # TODO> Log error
            print(error)
            success = False
            response = str(error)

            response_model = CPFResponse(
                success=success,
                response=response
            )
            return response_model

        self._save_cpf(cpf)

        response = "CPF was successfully created."
        response_model = CPFResponse(
            success=success,
            response=response
        )

        return response_model

    def _create_cpf(self, request: CPFRequest) -> CPF:
        """
        TODO
        """
        value = request.values.get("value")
        date_str = request.values.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d")

        cpf = CPF(value=value, date=date)

        return cpf

    def _save_cpf(self, cpf: CPF):
        """
        TODO: IMPLEMENT
        """
        request = {
            "type": "cpf",
            "document": cpf,
        }

        self._repository.create(request)
