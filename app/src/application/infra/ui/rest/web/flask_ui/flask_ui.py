"""
Module containing the "FlaskUI" Class.
"""

from flask import Flask

from .constants import FLASK_SECRET_KEY
from .endpoints import endpoints
from ....interfaces import UI


class FlaskUI(UI):
    """
    Class to represent the User Interface using Flask.
    """
    _flask: Flask

    def __init__(self) -> None:
        """
        Constructor to set up some variables.
        """
        self._flask = Flask(__name__)

    def execute(self) -> None:
        """
        TODO
        """
        self._configure()
        self._create_routes()

        self._flask.run(host="0.0.0.0", port=5_000)

    def _configure(self) -> None:
        """
        TODO
        """
        self._configure_secret_key()
        self._create_routes()

    def _configure_secret_key(self) -> None:
        """"""
        self._flask.config["SECRET_KEY"] = FLASK_SECRET_KEY

    def _create_routes(self) -> None:
        """
        TODO
        """
        self._flask.add_url_rule("/api/", "index", endpoints.index)
        self._flask.add_url_rule("/api/comprovante-residencia", "comprovante-residencia", endpoints.comprovante_residencia, methods=["GET", "POST"])
        self._flask.add_url_rule("/api/comprovante-residencia/<int:comprovante_residencia_id>", "comprovante-residencia-with-id", endpoints.comprovante_residencia, methods=["GET", "PUT", "DELETE"])
        self._flask.add_url_rule("/api/cpf", "cpf", endpoints.cpf, methods=["GET", "POST"])
        self._flask.add_url_rule("/api/cpf/<int:cpf_id>", "cpf-with-id", endpoints.cpf, methods=["GET", "PUT", "DELETE"])
        self._flask.add_url_rule("/api/rg", "rg", endpoints.rg, methods=["GET", "POST"])
        self._flask.add_url_rule("/api/rg/<int:rg_id>", "rg-with-id", endpoints.rg, methods=["GET", "PUT", "DELETE"])
