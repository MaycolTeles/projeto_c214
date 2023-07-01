"""
TODO
"""

from typing import Any, Optional, Union
from contextlib import contextmanager

import mysql.connector as mysql

from .constants import HOST, USER, PASSWORD, PORT, DATABASE
from src.domain.documents import Document
from src.domain.interfaces import Repository


@contextmanager
def connect():
    """
    Function to connect to the database.

    This function should be used as a context manager.
    """
    try:
        connection = mysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            port=PORT,
            database=DATABASE
        )

        cursor = connection.cursor()

        yield cursor

    except mysql.Error as error:
        print("ERROR!")
        print(error)

    else:
        connection.commit()
        cursor.close()
        connection.close()


class MySQLRepository(Repository):
    """
    TODO
    """

    def _execute_query(
        self,
        query: str,
        params: Optional[list[Union[str, int]]]=None
    ) -> Any:
        """
        Method to execute the query received as argument with the parameters
        (If any - The default is an empty list for select"s, for example)
        received as argument.

        Parameters
        -----------
        query : str
            The query to be executed.

        params : List[str, int], optional
            The parameters to be used in the query.
            The default value is an empty list.

        Returns
        --------
        Any
            - The data if the query was successafully executed;
            - False otherwise.
        """
        if params is None:
            params = []

        response = None

        with connect() as cursor:
            cursor.execute(query, params)

            response = cursor.fetchall()

        return response

    def create(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")

        query = f"""
            INSERT INTO {document} (
                `value`,
                `date`
            ) VALUES (%s, %s)
        """
        value = request.get("document")._value
        date = request.get("document")._date

        values = [value, date]

        response = self._execute_query(query, values)
        return response

    def read(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")
        
        query = f"""
            SELECT * FROM {document}
            WHERE
                `id` = %s
        """
        id = int(request.get("id", 0)) + 1
        values = [id]

        response = self._execute_query(query, values)
        return response

    def read_all(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")

        query = f"""
            SELECT * FROM {document}
        """

        response = self._execute_query(query)
        return response

    def update(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")
        id = int(request.get("id")) + 1

        query = f"""
            UPDATE `{document}`
            SET
                `value` = %s,
                `date` = %s
            WHERE
                `id` = %s
        """
        value = request.get("document")._value
        date = request.get("document")._date

        values = [value, date, id]

        response = self._execute_query(query, values)
        return response

    def delete(self, request: dict[str, Union[str, Document]]) -> Any:
        """
        TODO
        """
        document = request.get("type")
        id = int(request.get("id")) + 1

        query = f"""
            DELETE FROM `{document}`
            WHERE
                `id` = %s
        """
        values = [id]

        response = self._execute_query(query, values)
        return response
