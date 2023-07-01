"""
Module containing the DeleteRG Use Case.
"""

from ..rg import RG
from ..request_model import RGRequest
from ..response_model import RGResponse
from src.dependencies.repositories import get_repository
from src.domain.interfaces import Repository, UseCase


class DeleteRG(UseCase):
    """
    Use Case class to delete a new RG.
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
        rg = self._delete_rg(request)

        response = rg
        response_model = RGResponse(
            success=success,
            response=response
        )

        return response_model

    def _delete_rg(
        self,
        request: RGRequest
    ) -> RG:
        """
        TODO
        """
        request = {
            "type": "rg",
            "id": request.values.get("id"),
        }

        response = self._repository.delete(request)

        return response
