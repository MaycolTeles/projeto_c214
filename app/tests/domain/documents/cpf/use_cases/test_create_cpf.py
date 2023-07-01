"""
Module containing the CreateCPFTestCase Test Class.
"""

from datetime import datetime, timedelta
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.domain.documents.cpf import (
    # CPF,
    CreateCPF,
    CPFRequest,
    CPFResponse
)


class CreateCPFTestCase(TestCase):
    """
    Class to test the CreateCPF class.
    """

    def setUp(self) -> None:
        """
        Method to set the test up.
        """
        self._mock_repository()

        self._use_case = CreateCPF()
        self._test_value = "11144477735"
        self._test_date = datetime.now()

    def tearDown(self) -> None:
        """
        Method to tear the test down.
        """
        self._patcher.stop()

    def _mock_repository(self) -> None:
        """TODO"""
        patcher_path = ("src.domain.documents.cpf.use_cases.create_cpf.get_repository")
        self._patcher = patch(patcher_path)
        mock_repository_factory = self._patcher.start()
        mock_repository = mock_repository_factory.return_value = MagicMock()
        self._mock_create: MagicMock = mock_repository.create

    def test_should_create_new_cpf_in_repository(self):
        """TODO"""
        values = {
            "value": self._test_value,
            "date": self._test_date,
        }

        request = CPFRequest(values)

        actual = self._use_case.execute(request)
        expected = CPFResponse(True, "CPF was successfully created.")

        self.assertEqual(actual, expected)
        # self._mock_create.assert_called_once()

    def test_should_not_create_cpf_because_it_is_invalid(self):
        """TODO"""
        date_in_future = datetime.now() + timedelta(days=1)

        values = {
            "value": self._test_value,
            "date": date_in_future,
        }

        request = CPFRequest(values)

        actual = self._use_case.execute(request)

        expected_message = f"CPF is invalid. Date can't be newer than current date (date={date_in_future})."
        expected = CPFResponse(False, expected_message)

        self.assertEqual(actual, expected)
        # self._mock_create.assert_not_called()
