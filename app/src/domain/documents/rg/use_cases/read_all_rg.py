"""
Module containing the ReadAllRG Use Case.
"""

from ..rg import RG
from ..request_model import RGRequest
from ..response_model import RGResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class ReadAllRG(UseCase):
    """
    Use Case class to read all RG.
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
        all_rg = self._read_all_rg(request)

        response = all_rg
        response_model = RGResponse(
            success=success,
            response=response
        )

        return response_model

    def _read_all_rg(
        self,
        request: RGRequest
    ) -> RG:
        """
        TODO
        """
        request = {
            "type": "rg",
        }

        response = self._repository.read_all(request)

        return response
