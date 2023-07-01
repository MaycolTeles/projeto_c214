"""
Module containing the CPFTestCase class.
"""

from datetime import datetime, timedelta
from unittest import TestCase

from src.domain.documents.cpf import CPF, InvalidCPFException


class CPFTestCase(TestCase):
    """
    Class to test the CPF class.
    """

    def test_should_create_valid_cpf(self) -> None:
        """
        Method to assert the CPF was correctly created because it has valid parameters.
        """
        test_valid_cpf_string = "11144477735"
        test_datetime = datetime.now()

        cpf = CPF(
            value=test_valid_cpf_string,
            date=test_datetime
        )

        actual = isinstance(cpf, CPF)

        self.assertTrue(actual)

    def test_should_raise_an_error_when_creating_cpf_with_wrong_length(self) -> None:
        """
        Method to assert the CPF raised an error when trying to create it
        because it has invalid parameters (cpf is smaller than it should be).
        """
        test_invalid_cpf_string = "1234567891"
        test_datetime = datetime.now()

        with self.assertRaises(InvalidCPFException) as exception:
            _ = CPF(
                value=test_invalid_cpf_string,
                date=test_datetime
            )

        actual = exception.exception.args[0]
        expected = f"CPF {test_invalid_cpf_string} is invalid. CPF must have exactly 11 numerical digits (current=10)"

        self.assertEqual(actual, expected)

    def test_should_raise_an_error_when_creating_cpf_with_invalid_first_digit(self) -> None:
        """
        Method to assert the CPF raised an error when trying to create it
        because it has invalid parameters (first cpf digit is invalid).
        """
        test_invalid_cpf_string = "11144477745"
        test_datetime = datetime.now()

        with self.assertRaises(InvalidCPFException) as exception:
            _ = CPF(
                value=test_invalid_cpf_string,
                date=test_datetime
            )

        actual = exception.exception.args[0]
        expected = f"CPF {test_invalid_cpf_string} is not a valid CPF."

        self.assertEqual(actual, expected)

    def test_should_raise_an_error_when_creating_cpf_with_invalid_second_digit(self) -> None:
        """
        Method to assert the CPF raised an error when trying to create it
        because it has invalid parameters (second cpf digit is invalid).
        """
        test_invalid_cpf_string = "11144477736"
        test_datetime = datetime.now()

        with self.assertRaises(InvalidCPFException) as exception:
            _ = CPF(
                value=test_invalid_cpf_string,
                date=test_datetime
            )

        actual = exception.exception.args[0]
        expected = f"CPF {test_invalid_cpf_string} is not a valid CPF."

        self.assertEqual(actual, expected)

    def test_should_raise_an_error_when_creating_cpf_with_future_date(self):
        """TODO"""
        test_valid_cpf_string = "11144477735"
        test_datetime = datetime.now() + timedelta(days=1)

        with self.assertRaises(InvalidCPFException) as exception:
            _ = CPF(
                value=test_valid_cpf_string,
                date=test_datetime
            )

        actual = exception.exception.args[0]
        expected = f"CPF is invalid. Date can't be newer than current date (date={test_datetime})."

        self.assertEqual(actual, expected)
