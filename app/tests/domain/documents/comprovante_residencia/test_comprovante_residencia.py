"""
Module containing the ComprovanteResidenciaTestCase Test Class.
"""

from datetime import datetime, timedelta
from unittest import TestCase

from src.domain.documents.comprovante_residencia import (
    ComprovanteResidencia,
    ComprovanteResidenciaType,
    InvalidComprovanteResidenciaException
)


class ComprovanteResidenciaTestCase(TestCase):
    """
    Class to test the ComprovanteResidencia class.
    """

    def test_should_create_valid_comprovante_residencia(self) -> None:
        """
        Method to assert the ComprovanteResidencia was correctly created since it has valid parameters.
        """
        test_comprovante_residencia_value = "test_value"
        test_comprovante_residencia_type = ComprovanteResidenciaType.AGUA
        test_datetime = datetime.now()

        comprovante_residencia = ComprovanteResidencia(
            value=test_comprovante_residencia_value,
            date=test_datetime,
            comprovante_type=test_comprovante_residencia_type
        )

        actual = isinstance(comprovante_residencia, ComprovanteResidencia)

        self.assertTrue(actual)

    def test_should_raise_exception_when_creating_comprovante_residencia_with_future_date(self) -> None:
        """
        Method to assert the ComprovanteResidencia raised an exception when trying to create it
        because it has invalid parameters (date is newer than current date).
        """
        test_comprovante_residencia_value = "test_value"
        test_comprovante_residencia_type = ComprovanteResidenciaType.AGUA
        test_datetime = datetime.now() + timedelta(days=1)

        with self.assertRaises(InvalidComprovanteResidenciaException) as exception:
            _ = ComprovanteResidencia(
                value=test_comprovante_residencia_value,
                date=test_datetime,
                comprovante_type=test_comprovante_residencia_type
            )

        actual = exception.exception.args[0]
        expected = (
            "Comprovante de Residência is invalid. "
            f"Date can't be newer than current date (date={test_datetime})."
        )

        self.assertEqual(actual, expected)
