"""
Module containing the ReadRG Use Case.
"""

from ..rg import RG
from ..request_model import RGRequest
from ..response_model import RGResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class ReadRG(UseCase):
    """
    Use Case class to read a new RG.
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
        rg = self._read_rg(request)

        response = rg
        response_model = RGResponse(
            success=success,
            response=response
        )

        return response_model

    def _read_rg(
        self,
        request: RGRequest
    ) -> RG:
        """
        TODO
        """
        rg_id = request.values.get("id")

        request = {
            "type": "rg",
            "id": rg_id,
        }

        response = self._repository.read(request)

        return response
