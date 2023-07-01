"""
Module containing the "CPF" class.
"""

from datetime import datetime

from .exceptions import InvalidCPFException
from src.domain.documents import Document


_CPF_LENGTH = 11


class CPF(Document):
    """
    Class to represent a CPF document.
    This class is responsible for validating a CPF.
    """
    _value: str

    def __init__(self, value: str, date: datetime) -> None:
        """
        Constructor of the class.

        Parameters
        ----------
        value : str
            The value of the CPF.

        date : datetime
            The date of the CPF.
        """
        cpf_only_numbers = self._get_only_cpf_numbers(value)
        self._value = cpf_only_numbers

        super().__init__(date)

    def _get_only_cpf_numbers(self, value: str) -> str:
        """
        Private Method to get only the CPF numbers.

        Parameters
        ----------
        value : str
            The value of the CPF.

        Returns
        -------
        str
            The CPF numbers.
        """
        cpf_numbers = "".join(filter(str.isdigit, value))
        return cpf_numbers

    def _validate_document(self) -> None:
        """
        Protected Method to validate the document by raising an exception if it"s not valid.
        """
        self._validate_cpf()

    def _validate_cpf(self) -> None:
        """
        Private Method to validate the cpf by raising an exception if it"s not valid.
        """
        self._validate_length()
        self._validate_digits()
        self._validate_date()

    def _validate_length(self) -> None:
        """
        Private Method to validate the CPF length by raising an InvalidCPFException exception
        if its length is not valid.

        Raises
        --------
        InvalidCPFException
            If the cpf length is not valid.
        """
        if len(self._value) == _CPF_LENGTH:
            return

        invalid_length_message = (
            f"CPF {self._value} is invalid. "
            f"CPF must have exactly 11 numerical digits (current={len(self._value)})"
        )

        raise InvalidCPFException(invalid_length_message)

    def _validate_digits(self) -> None:
        """
        Private Method to validate the cpf digits.
        """
        self._validate_first_digit()
        self._validate_second_digit()

    def _validate_first_digit(self) -> None:
        """
        Private Method to validate the cpf first digit.
        """
        cpf_without_digits = self._value[:-2]
        first_digit = self._value[-2]

        rest = self._calculate_cpf_rest(cpf_without_digits, 1)
        self._validate_rest(rest, first_digit)

    def _validate_second_digit(self) -> None:
        """
        Private Method to validate the cpf second digit.
        """
        cpf_without_last_digit = self._value[:-1]
        second_digit = self._value[-1]

        rest = self._calculate_cpf_rest(cpf_without_last_digit, 0)
        self._validate_rest(rest, second_digit)

    def _calculate_cpf_rest(self, cpf_numbers: str, start: int) -> int:
        """
        Private Method to calculate the cpf rest based on the cpf numbers and the start index.

        Parameters
        ----------
        cpf_numbers : str
            The cpf numbers to calculate the rest.

        start : int
            The start index to calculate the rest.

        Returns
        -------
        int
            The cpf rest.
        """
        numeric_digits_sum = 0

        for idx, digit in enumerate(cpf_numbers, start=start):
            digit_int = int(digit)
            digit_with_weight = digit_int * (_CPF_LENGTH - idx)
            numeric_digits_sum += digit_with_weight

        rest = (numeric_digits_sum) % _CPF_LENGTH

        return rest

    def _validate_rest(self, rest: int, actual_digit: str) -> None:
        """
        Private Method to validate the cpf rest by raising an InvalidCPFException exception
        if its digit is not valid.

        Parameters
        ----------
        rest : int
            The cpf rest.

        actual_digit : str
            The actual digit to validate.

        Raises
        --------
        InvalidCPFException
            If the cpf digit is not valid.
        """
        if rest < 2:
            expected_digit = 0

        else:
            expected_digit = _CPF_LENGTH - rest

        if int(actual_digit) == expected_digit:
            return

        invalid_length_message = f"CPF {self._value} is not a valid CPF."
        raise InvalidCPFException(invalid_length_message)

    def _validate_date(self) -> None:
        """
        Private Method to validate the cpf date by raising an InvalidCPFException exception
        if its date is not valid.

        Raises
        --------
        InvalidCPFException
            If the cpf date is not valid.
        """
        if self._date > datetime.now():
            invalid_date_message = (
                f"CPF is invalid. "
                f"Date can't be newer than current date (date={self._date})."
            )

            raise InvalidCPFException(invalid_date_message)

    def to_dict(self):
        return {
            "value": self._value,
            "date": self._date.strftime("%Y-%m-%d"),
        }
