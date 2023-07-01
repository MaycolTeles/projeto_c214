"""
TODO
"""

from typing import Any, Union

from src.domain.documents import Document
from src.domain.interfaces import Repository


class InMemoRepository(Repository):
    """
    TODO
    """
    _data: dict[str, list[Any]] = {
        "comprovante_residencia": [],
        "cpf": [],
        "rg": [],
    }

    def create(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")
        data = request.get("document").to_dict()

        self._data[document].append(data)

    def read(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")
        id = request.get("id")

        return self._data[document][id]

    def read_all(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")
        return self._data[document]

    def update(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")
        id = request.get("id")
        data = request.get("document").to_dict()

        self._data[document][id] = data

        return data

    def delete(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")
        id = request.get("id")

        del self._data[document][id]
