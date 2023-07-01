"""
Module containing the RGTestCase class.
"""

from datetime import datetime, timedelta
from unittest import TestCase

from src.domain.documents.cpf import CPF
from src.domain.documents.rg import RG, InvalidRGException


class RGTestCase(TestCase):
    """
    Class to test the RG class.
    """

    def test_should_create_valid_rg(self) -> None:
        """
        Method to assert the RG was correctly created because it has valid parameters.
        """
        test_valid_rg_string = "123456789"
        test_datetime = datetime.now()

        rg = RG(
            value=test_valid_rg_string,
            date=test_datetime
        )

        actual = isinstance(rg, RG)

        self.assertTrue(actual)

    def test_should_create_a_valid_rg_with_cpf(self) -> None:
        """
        Method to assert the RG was correctly created because it has valid parameters
        and it has a valid RG attached to it.
        """
        test_valid_rg_string = "123456789"
        test_datetime = datetime.now()
        test_cpf = CPF(
            value="11144477735",
            date=test_datetime
        )

        rg = RG(
            value=test_valid_rg_string,
            date=test_datetime,
            cpf=test_cpf
        )

        actual = isinstance(rg, RG)

        actual_cpf = rg.get_cpf()
        expected_cpf = test_cpf

        self.assertTrue(actual)
        self.assertEqual(actual_cpf, expected_cpf)

    def test_should_raise_an_error_when_creating_rg_with_invalid_date(self) -> None:
        """
        Method to assert the RG raised an error when trying to create it
        because it has invalid parameters (date is in the future).
        """
        test_invalid_rg_string = "1234567890"
        test_future_datetime = datetime.now() + timedelta(days=1)

        with self.assertRaises(InvalidRGException) as exception:
            RG(
                value=test_invalid_rg_string,
                date=test_future_datetime
            )

        actual = exception.exception.args[0]
        expected = f"RG is invalid. Date can't be newer than current date (date={test_future_datetime})."

        self.assertEqual(actual, expected)
