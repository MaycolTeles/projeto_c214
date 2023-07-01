"""TODO"""

from typing import Any
from abc import ABC, abstractmethod


class Repository(ABC):
    """
    Interface to represent a Repository.
    """

    @abstractmethod
    def create(self, request: Any) -> Any:
        """
        Method to execute the Repository.
        """

    @abstractmethod
    def read(self, request: Any) -> Any:
        """
        Method to execute the Repository.
        """

    @abstractmethod
    def read_all(self, request: Any) -> Any:
        """
        Method to execute the Repository.
        """

    @abstractmethod
    def update(self, request: Any) -> Any:
        """
        Method to execute the Repository.
        """

    @abstractmethod
    def delete(self, request: Any) -> Any:
        """
        Method to execute the Repository.
        """
