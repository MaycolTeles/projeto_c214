"""
Class containing the "ComprovanteDeResidencia" Class.
"""

from datetime import datetime

from .types import ComprovanteResidenciaType
from .exceptions import InvalidComprovanteResidenciaException
from src.domain.documents import Document


class ComprovanteResidencia(Document):
    """
    Class to represent a "ComprovanteResidencia" document.
    This class is responsible for validating a "ComprovanteResidencia".
    """
    _type: ComprovanteResidenciaType

    def __init__(self, value: str, date: datetime, comprovante_type: ComprovanteResidenciaType) -> None:
        """
        Constructor of the class.

        Parameters
        ----------
        value : str
            The value of the ComprovanteResidencia.

        date : datetime
            The date of the ComprovanteResidencia.
        """
        self._value = value
        self._type = comprovante_type

        super().__init__(date)

    def _validate_document(self) -> None:
        """
        Protected Method to validate the document by raising an exception if it"s not valid.
        """
        self._validate_comprovante_residencia()

    def _validate_comprovante_residencia(self) -> None:
        """
        Private Method to validate the ComprovanteResidencia by raising an exception if it"s not valid.
        """
        self._validate_date()

    def _validate_date(self) -> None:
        """
        Private Method to validate the date by raising an InvalidComprovanteResidenciaException exception
        if its date is not valid.
        """
        if self._date > datetime.now():
            exception_message = (
                "Comprovante de Residência is invalid. "
                f"Date can't be newer than current date (date={self._date})."
            )
            raise InvalidComprovanteResidenciaException(exception_message)

    def to_dict(self):
        """
        Method to convert the object to a dict.
        """
        return {
            "value": self._value,
            "date": self._date.strftime("%Y-%m-%d"),
            "comprovante_type": self._type.value
        }
