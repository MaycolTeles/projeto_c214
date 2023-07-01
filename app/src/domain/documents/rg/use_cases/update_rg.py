"""
Module containing the UpdateRG Use Case.
"""

from datetime import datetime

from ..rg import RG
from ..request_model import RGRequest
from ..response_model import RGResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class UpdateRG(UseCase):
    """
    Use Case class to update a new RG.
    """
    _repository: Repository

    def __init__(self):
        """TODO"""
        self._repository = get_repository()

    def execute(
        self,
        request: RGRequest
    ) -> RGResponse:
        """
        Method to execute the use case.
        """
        success = True
        rg = self._update_rg(request)

        response = rg
        response_model = RGResponse(
            success=success,
            response=response
        )

        return response_model

    def _update_rg(
        self,
        request: RGRequest
    ) -> RG:
        """
        TODO
        """
        id = request.values.get("id")

        value = request.values.get("value")
        date_str = request.values.get("date")
        date = datetime.strptime(date_str, "%Y-%m-%d")

        rg = RG(value=value, date=date)

        request = {
            "type": "rg",
            "id": id,
            "document": rg
        }

        response = self._repository.update(request)

        return response
