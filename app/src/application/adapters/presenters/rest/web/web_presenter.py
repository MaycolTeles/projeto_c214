"""
Module containing the "WebPresenter" Class.
"""

from typing import Any, Dict
from dataclasses import asdict

from src.domain.interfaces.response_model import ResponseModel


class WebPresenter:
    """
    TODO: FIX
    TODO: CAN USE ONLY ONE METHOD THAT RECEIVES A RESPONSE MODEL (CREATE INTERFACE FOR IT) AND CONVERT IT TO DICT
    """

    def present(self, response_model: ResponseModel) -> Dict[str, Any]:
        """
        """
        response_model_dict = asdict(response_model)

        return response_model_dict
