"""
Module containing the CreateRG Use Case.
"""

from datetime import datetime

from ..exceptions import InvalidRGException
from ..request_model import RGRequest
from ..response_model import RGResponse
from ..rg import RG
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class CreateRG(UseCase):
    """
    Use Case class to create a new RG.
    """
    _repository: Repository

    def __init__(self) -> None:
        self._repository = get_repository()

    def execute(self, request: RGRequest) -> RGResponse:
        """
        Method to execute the use case.
        """
        success = True
        try:
            rg = self._create_rg(request)

        except InvalidRGException as error:
            # TODO> Log error
            print(error)
            success = False
            response = str(error)

            response_model = RGResponse(
                success=success,
                response=response
            )
            return response_model

        self._save_rg(rg)

        response = "RG was successfully created."
        response_model = RGResponse(
            success=success,
            response=response
        )

        return response_model

    def _create_rg(self, request: RGRequest) -> RG:
        """
        TODO
        """
        value = request.values.get("value")
        date_str = request.values.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d")

        rg = RG(value=value, date=date)

        return rg

    def _save_rg(self, rg: RG):
        """
        TODO: IMPLEMENT
        """
        request = {
            "type": "rg",
            "document": rg,
        }

        self._repository.create(request)
