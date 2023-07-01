"""
Module containing the CreateComprovanteResidenciaTestCase Test Class.
"""

from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.domain.documents.comprovante_residencia import (
    # ComprovanteResidencia,
    ComprovanteResidenciaType,
    CreateComprovanteResidencia,
    ComprovanteResidenciaRequest,
    ComprovanteResidenciaResponse,
)


class CreateComprovanteResidenciaTestCase(TestCase):
    """
    Class to test the CreateComprovanteResidencia class.
    """

    def setUp(self) -> None:
        """
        Method to set the test up.
        """
        self._mock_repository()

        self._use_case = CreateComprovanteResidencia()
        self._test_value = "test_value"
        self._test_date = datetime.now()
        self._test_comprovante_type = ComprovanteResidenciaType.AGUA

    def tearDown(self) -> None:
        """
        Method to tear the test down.
        """
        self._patcher.stop()

    def _mock_repository(self) -> None:
        """TODO"""
        patcher_path = (
            "src.domain.documents.comprovante_residencia.use_cases."
            "create_comprovante_residencia.get_repository"
        )
        self._patcher = patch(patcher_path)
        mock_repository_factory = self._patcher.start()
        mock_repository = mock_repository_factory.return_value = MagicMock()
        self._mock_create: MagicMock = mock_repository.create

    def test_should_create_new_comprovante_residencia_in_repository(self):
        """TODO"""
        values = {
            "value": self._test_value,
            "date": self._test_date,
            "comprovante_type": self._test_comprovante_type
        }

        request_model = ComprovanteResidenciaRequest(values)

        actual = self._use_case.execute(request_model)
        expected = ComprovanteResidenciaResponse(
            True,
            "ComprovanteResidencia was successfully created."
        )

        self.assertEqual(actual, expected)
        # self._mock_create.assert_called_once()

    def test_should_not_create_comprovante_residencia_because_it_is_invalid(self):
        """TODO"""
        date_in_future = datetime.now() + timedelta(days=1)

        values = {
            "value": self._test_value,
            "date": date_in_future,
            "comprovante_type": self._test_comprovante_type
        }

        request_model = ComprovanteResidenciaRequest(values)

        actual = self._use_case.execute(request_model)

        expected_message = (
            "Comprovante de Residência is invalid. "
            f"Date can't be newer than current date (date={date_in_future})."
        )
        expected = ComprovanteResidenciaResponse(False, expected_message)

        self.assertEqual(actual, expected)
        # self._mock_create.assert_not_called()
