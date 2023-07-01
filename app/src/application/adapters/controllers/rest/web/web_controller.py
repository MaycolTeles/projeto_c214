"""
Module containing the "WebController" Class.
"""

from typing import Any

from src.application.adapters.presenters.rest.web import WebPresenter
from src.domain.documents.comprovante_residencia import (
    CreateComprovanteResidencia,
    ReadComprovanteResidencia,
    ReadAllComprovanteResidencia,
    UpdateComprovanteResidencia,
    DeleteComprovanteResidencia,
    ComprovanteResidenciaRequest,
    ComprovanteResidenciaResponse
)
from src.domain.documents.cpf import (
    CreateCPF,
    ReadCPF,
    ReadAllCPF,
    UpdateCPF,
    DeleteCPF,
    CPFRequest,
    CPFResponse
)
from src.domain.documents.rg import (
    CreateRG,
    ReadRG,
    ReadAllRG,
    UpdateRG,
    DeleteRG,
    RGRequest,
    RGResponse
)


class WebController:
    """
    TODO: FIX
    """
    _presenter: WebPresenter

    def __init__(self) -> None:
        """
        TODO
        """
        self._presenter = WebPresenter()

    def create_comprovante_residencia(self, params: dict[str, Any]):
        """
        TODO
        """
        request = ComprovanteResidenciaRequest(params)
        use_case = CreateComprovanteResidencia()
        response = use_case.execute(request)

        presenter_response = self._presenter.present(response)

        return presenter_response

    def read_comprovante_residencia(self, params: dict[str, Any]):
        """
        TODO
        """
        request = ComprovanteResidenciaRequest(params)
        use_case = ReadComprovanteResidencia()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def read_all_comprovante_residencia(self, params: dict[str, Any]):
        """
        TODO
        """
        request = ComprovanteResidenciaRequest(params)
        use_case = ReadAllComprovanteResidencia()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def update_comprovante_residencia(self, params: dict[str, Any]):
        """
        TODO
        """
        request = ComprovanteResidenciaRequest(params)
        use_case = UpdateComprovanteResidencia()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def delete_comprovante_residencia(self, params: dict[str, Any]):
        """
        TODO
        """
        request = ComprovanteResidenciaRequest(params)
        use_case = DeleteComprovanteResidencia()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def create_cpf(self, params: dict[str, Any]):
        """
        TODO
        """
        request = CPFRequest(params)
        use_case = CreateCPF()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def read_cpf(self, params: dict[str, Any]):
        """
        TODO
        """
        request = CPFRequest(params)
        use_case = ReadCPF()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def read_all_cpf(self, params: dict[str, Any]):
        """
        TODO
        """
        request = CPFRequest(params)
        use_case = ReadAllCPF()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def update_cpf(self, params: dict[str, Any]):
        """
        TODO
        """
        request = CPFRequest(params)
        use_case = UpdateCPF()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def delete_cpf(self, params: dict[str, Any]):
        """
        TODO
        """
        request = CPFRequest(params)
        use_case = DeleteCPF()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def create_rg(self, params: dict[str, Any]):
        """
        TODO
        """
        request = RGRequest(params)
        use_case = CreateRG()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def read_rg(self, params: dict[str, Any]):
        """
        TODO
        """
        request = RGRequest(params)
        use_case = ReadRG()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def read_all_rg(self, params: dict[str, Any]):
        """
        TODO
        """
        request = RGRequest(params)
        use_case = ReadAllRG()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def update_rg(self, params: dict[str, Any]):
        """
        TODO
        """
        request = RGRequest(params)
        use_case = UpdateRG()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 

    def delete_rg(self, params: dict[str, Any]):
        """
        TODO
        """
        request = RGRequest(params)
        use_case = DeleteRG()
        response = use_case.execute(request)
        presenter_response = self._presenter.present(response)

        return presenter_response 
