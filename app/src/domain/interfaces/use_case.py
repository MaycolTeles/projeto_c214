"""
Module containing the UseCase Interface.
"""

from abc import ABC, abstractmethod

from .request_model import RequestModel
from .response_model import ResponseModel


class UseCase(ABC):
    """
    Interface to represent a Use Case.

    This interface is used to define a single method to execute the use case,
    therefore applying the Command Pattern.
    """

    @abstractmethod
    def execute(self, request: RequestModel) -> ResponseModel:
        """
        Method to execute the Use Case.
        """
