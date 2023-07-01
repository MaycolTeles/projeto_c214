"""
Class containing the "Document" Class.
"""

from abc import ABC, abstractmethod
from datetime import datetime


class Document(ABC):
    """
    Abstract Class to represent a generic Document.
    """
    _date: datetime

    def __init__(self, date: datetime) -> None:
        """TODO"""
        self._date = date

        self._validate_document()

    @abstractmethod
    def _validate_document(self) -> None:
        """
        Protected Method to validate the document by checking if it"s valid or not.
        raises an exception if it"s invalid.
        """

    @abstractmethod
    def to_dict(self):
        """
        Protected Method to convert the object to a dict.
        """
