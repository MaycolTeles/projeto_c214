"""
Module containing the "RG" class.
"""

from typing import Optional
from datetime import datetime

from .exceptions import InvalidRGException
from src.domain.documents import Document
from src.domain.documents.cpf import CPF


class RG(Document):
    """
    Class to represent a RG.
    """
    _value: str
    _cpf: Optional[CPF]

    def __init__(self, value: str, date: datetime, cpf: Optional[CPF] = None) -> None:
        """
        Constructor of the class.

        Parameters
        ----------
        value : str
            The value of the RG.

        date : datetime
            The date of the RG.

        rg : Optional[CPF]
            The value of the CPF, by default None
        """
        self._value = value
        self._cpf = cpf

        super().__init__(date)

    def get_cpf(self) -> Optional[CPF]:
        """
        Public Method to get the RG.
        """
        return self._cpf

    def _validate_document(self) -> None:
        """
        Protected method to validate the document by raising an exception if it"s not valid.
        """
        self._validate_rg()

    def _validate_rg(self) -> None:
        """
        Private method to validate the RG.
        """
        self._validate_date()

    def _validate_date(self) -> None:
        """
        Private Method to validate the RG date by raising an InvalidRGException exception
        if its date is not valid.
        """
        current_date = datetime.now()

        if self._date <= current_date:
            return

        invalid_date_message = (
            "RG is invalid. "
            f"Date can't be newer than current date (date={self._date})."
        )
        raise InvalidRGException(invalid_date_message)

    def to_dict(self):
        """
        Method to convert the object to a dict.
        """
        return {
            "value": self._value,
            "date": self._date.strftime("%Y-%m-%d"),
            "cpf": self._cpf.to_dict() if self._cpf else None
        }
